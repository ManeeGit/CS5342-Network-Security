"""
Complete Local RAG System - Quiz Generator & Tutor
Single file, robust, accurate with proper citations
"""

import streamlit as st
import chromadb
import fitz
import os
import json
from pathlib import Path
from ddgs import DDGS
import requests
import wikipedia


# Configuration
SOURCE_DIR = "Source"
VECTOR_DB_DIR = "./vectordb"
PROCESSED_DIR = "./processed_md"
COLLECTION_NAME = "knowledge_base"
OLLAMA_URL = "http://localhost:11434"


# ============================================================================
# PDF Processing
# ============================================================================

def process_pdfs():
    """Convert PDFs to markdown and create vector embeddings"""
    
    # Create directories
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)
    
    # Get PDF files
    pdf_files = list(Path(SOURCE_DIR).glob("*.pdf"))
    if not pdf_files:
        st.error(f"No PDFs found in {SOURCE_DIR}")
        return None
    
    st.info(f"Found {len(pdf_files)} PDF files")
    
    # Initialize ChromaDB
    client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
    
    # Recreate collection
    try:
        client.delete_collection(COLLECTION_NAME)
    except:
        pass
    
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    
    # Process each PDF
    all_chunks = []
    progress_bar = st.progress(0)
    
    for idx, pdf_path in enumerate(pdf_files):
        st.text(f"Processing: {pdf_path.name}")
        
        # Extract text from PDF
        pdf = fitz.open(pdf_path)
        doc_name = pdf_path.stem
        
        # Save as markdown
        md_content = f"# {doc_name}\n\n"
        
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            text = page.get_text()
            
            if text.strip():
                md_content += f"## Page {page_num + 1}\n\n{text}\n\n"
                
                # Create chunk
                all_chunks.append({
                    'id': f"{doc_name}_p{page_num + 1}",
                    'text': text,
                    'source': doc_name,
                    'page': page_num + 1
                })
        
        pdf.close()
        
        # Save markdown
        md_path = Path(PROCESSED_DIR) / f"{doc_name}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        progress_bar.progress((idx + 1) / len(pdf_files))
    
    # Add to vector database
    st.info("Creating embeddings...")
    
    batch_size = 100
    for i in range(0, len(all_chunks), batch_size):
        batch = all_chunks[i:i + batch_size]
        
        collection.add(
            documents=[c['text'] for c in batch],
            metadatas=[{'source': c['source'], 'page': c['page']} for c in batch],
            ids=[c['id'] for c in batch]
        )
    
    st.success(f"Processed {len(pdf_files)} PDFs, {len(all_chunks)} pages indexed")
    return collection


# ============================================================================
# Search & Retrieval
# ============================================================================

def search_local(query, collection, top_k=5):
    """Search local knowledge base"""
    try:
        results = collection.query(
            query_texts=[query],
            n_results=top_k
        )
        
        if not results['documents'] or not results['documents'][0]:
            return []
        
        retrieved = []
        for i in range(len(results['documents'][0])):
            retrieved.append({
                'text': results['documents'][0][i],
                'source': results['metadatas'][0][i]['source'],
                'page': results['metadatas'][0][i]['page'],
                'score': 1 - results['distances'][0][i]
            })
        
        return retrieved
    except:
        return []


def search_wikipedia(query):
    """Search Wikipedia for information"""
    try:
        wikipedia.set_lang("en")
        
        # Search for pages
        search_results = wikipedia.search(query, results=3)
        
        if not search_results:
            return []
        
        wiki_results = []
        for title in search_results[:3]:
            try:
                page = wikipedia.page(title, auto_suggest=False)
                
                # Get summary (first 1000 chars)
                summary = page.content[:2000]
                
                wiki_results.append({
                    'text': f"{page.title}\n\n{summary}",
                    'source': page.url,
                    'page': 'Wikipedia',
                    'score': 0.9
                })
            except:
                continue
        
        return wiki_results
    except Exception as e:
        return []


def search_web(query):
    """Comprehensive web search - fetches from internet using DuckDuckGo"""
    
    web_results = []
    
    # Try DuckDuckGo text search
    try:
        st.info("Searching the internet...")
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=10))
            
            if results:
                for r in results:
                    content = f"{r.get('title', '')}\n\n{r.get('body', '')}"
                    web_results.append({
                        'text': content,
                        'source': r.get('href', 'Unknown'),
                        'page': 'Web Search',
                        'score': 0.85
                    })
                
                if web_results:
                    st.success(f"Found {len(web_results)} results from internet")
                    return web_results
    except Exception as e:
        st.warning(f"DuckDuckGo search error: {str(e)[:100]}")
    
    # If DuckDuckGo fails, try Wikipedia as last resort
    st.info("Trying Wikipedia as fallback...")
    wiki_results = search_wikipedia(query)
    
    if wiki_results:
        st.success(f"Found {len(wiki_results)} results from Wikipedia")
        return wiki_results
    
    st.error("All internet search methods failed")
    return []


def get_context(query, collection, threshold=0.4):
    """Get context from local or web"""
    local = search_local(query, collection)
    
    if local and len(local) > 0 and local[0]['score'] > threshold:
        return local, "local"
    
    st.warning("Topic not in local sources, searching web...")
    web = search_web(query)
    
    if not web or len(web) == 0:
        st.error("Web search returned no results")
        return [], "none"
    
    return web, "web"


# ============================================================================
# LLM Integration
# ============================================================================

def check_ollama():
    """Check if Ollama is running"""
    try:
        response = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if response.status_code == 200:
            return True
        st.warning(f"Ollama returned status {response.status_code}")
        return False
    except Exception as e:
        st.error(f"Cannot connect to Ollama: {str(e)[:100]}")
        st.info("Start Ollama by running: **ollama serve**")
        return False


def generate_with_ollama(prompt, model="qwen2.5:7b-instruct"):
    """Generate response with Ollama"""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": model, 
                "prompt": prompt, 
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 2000
                }
            },
            timeout=120
        )
        if response.status_code == 200:
            return response.json()['response']
        else:
            st.error(f"Ollama returned status {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Ollama error: {e}")
        st.info("Run 'ollama serve' in a terminal to start Ollama")
        return None


# ============================================================================
# Quiz Generation
# ============================================================================

def generate_quiz(topic, context, num_q=5):
    """Generate quiz with LLM - includes MCQ, True/False, and Fill-in-the-blank"""
    
    context_text = "\n\n".join([
        f"[Source: {c['source']}, Page {c['page']}]\n{c['text'][:1000]}"
        for c in context[:5]
    ])
    
    # Calculate question distribution
    num_mcq = max(1, num_q - 3)  # At least 1 MCQ
    num_tf = 2  # Exactly 2 True/False
    num_fib = 1  # Exactly 1 Fill-in-the-blank
    
    prompt = f"""You are an expert quiz generator. Create a high-quality quiz about "{topic}" using ONLY the information from the context below. Do NOT make up information.

CONTEXT:
{context_text}

CRITICAL RULES:
1. Extract SPECIFIC facts, definitions, and technical details from the context
2. Use EXACT terminology and numbers from the sources
3. Create CLEAR, UNAMBIGUOUS questions WITHOUT mentioning source names in the question text
4. Make wrong options plausible but clearly incorrect
5. For True/False: use complete factual statements WITHOUT source references in the statement
6. For Fill-in-the-blank: create natural sentences WITHOUT mentioning sources
7. Keep source references ONLY in explanations, NOT in questions

YOU MUST GENERATE EXACTLY {num_mcq} MULTIPLE CHOICE + {num_tf} TRUE/FALSE + {num_fib} FILL-IN-THE-BLANK = {num_q} TOTAL QUESTIONS.

FORMAT FOR MULTIPLE CHOICE:
QUESTION [number]: MCQ
What is [specific technical aspect] of {topic}? [DO NOT mention sources here]
A) [Correct answer with specific details from context]
B) [Plausible wrong answer]
C) [Plausible wrong answer]
D) [Plausible wrong answer]
CORRECT: A
EXPLANATION: According to [Source], page [X]: [Quote the relevant sentence]

---

FORMAT FOR TRUE/FALSE:
QUESTION [number]: TF
[Complete factual statement - NO source mentions in the statement itself]
A) True
B) False
CORRECT: A
EXPLANATION: This is true according to [Source], page [X]: [Quote supporting text]

---

FORMAT FOR FILL-IN-THE-BLANK:
QUESTION [number]: FIB
[Natural sentence with _____ for the blank - NO source mentions in the sentence]
CORRECT: [The exact term that was removed]
EXPLANATION: Complete sentence from [Source], page [X]: [Full original sentence]

---

EXAMPLE MCQ:
QUESTION 1: MCQ
What is the key size used in AES-128?
A) 128 bits
B) 64 bits
C) 256 bits
D) 192 bits
CORRECT: A
EXPLANATION: According to Network-security-essentials, page 45: AES-128 uses a 128-bit key.

Now generate the quiz with SPECIFIC details from the context:"""
    
    ollama_available = check_ollama()
    
    if not ollama_available:
        st.error("Ollama is not running. Please start Ollama to generate contextual questions.")
        st.info("Run: **ollama serve** in a terminal")
        return None
    
    st.info("Generating quiz with local LLM (qwen2.5:7b-instruct)...")
    
    # Try up to 2 times to get all questions
    for attempt in range(2):
        response = generate_with_ollama(prompt)
        
        if not response:
            st.error("LLM failed to generate response")
            if attempt == 0:
                st.info("Retrying...")
                continue
            return None
        
        parsed = parse_quiz(response, context, num_q)
        
        if parsed and len(parsed) >= num_q:
            st.success(f"Generated {len(parsed)} contextual questions")
            return parsed[:num_q]
        elif parsed and len(parsed) > 0:
            st.warning(f"LLM only generated {len(parsed)}/{num_q} questions")
            if attempt == 0:
                st.info("Retrying to get all 5 questions...")
                continue
            else:
                st.error(f"Could only generate {len(parsed)} questions after 2 attempts")
                return parsed  # Return what we got
        else:
            st.error("Failed to parse LLM output")
            if attempt == 0:
                st.info("Retrying...")
                continue
            return None
    
    return None


def create_template_quiz(topic, context, num_q):
    """Generate high-quality quiz from context content with MCQ, TF, and FIB questions"""
    quiz = []
    
    num_mcq = max(1, num_q - 3)
    num_tf = 2
    num_fib = 1
    
    # Generate MCQ questions - extract specific facts
    for i in range(min(num_mcq, len(context))):
        ctx = context[i]
        text = ctx['text']
        
        # Extract complete sentences with technical content
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 40 and any(char.isupper() for char in s)]
        if len(sentences) < 1:
            continue
        
        # Use the most informative sentence
        main_fact = sentences[0] if len(sentences[0]) < 200 else sentences[0][:197] + "..."
        
        # Extract a key term to make question about
        words = main_fact.split()
        key_terms = [w for w in words if len(w) > 4 and w[0].isupper()]
        topic_word = key_terms[0] if key_terms else topic
        
        # Create specific question without source reference
        question = f"Which statement about {topic} is correct?"
        
        # Create more realistic options
        options = [
            f"A) {main_fact}",
            f"B) {topic} is not mentioned in security literature",
            f"C) {topic} has been deprecated and is no longer used",
            f"D) {topic} is only used in legacy systems"
        ]
        
        quiz.append({
            'type': 'MCQ',
            'question': question,
            'options': options,
            'correct': 'A',
            'explanation': f"Correct. The source states: '{main_fact}' ({ctx['source']}, page {ctx['page']})",
            'source': ctx['source'],
            'page': ctx['page']
        })
    
    # Generate True/False questions - use factual statements
    for i in range(min(num_tf, len(context))):
        ctx_idx = min(i + num_mcq, len(context) - 1)
        ctx = context[ctx_idx]
        sentences = [s.strip() for s in ctx['text'].split('.') if 30 < len(s.strip()) < 150]
        
        if sentences:
            # Pick a clear factual statement
            statement = sentences[0]
            quiz.append({
                'type': 'TF',
                'question': f"{statement}.",
                'options': ['A) True', 'B) False'],
                'correct': 'A',
                'explanation': f"True. This is stated in {ctx['source']}, page {ctx['page']}",
                'source': ctx['source'],
                'page': ctx['page']
            })
    
    # Generate Fill-in-the-blank question - remove technical term
    if len(context) > 0:
        ctx = context[0]
        sentences = [s.strip() for s in ctx['text'].split('.') if 40 < len(s.strip()) < 150]
        if sentences:
            sentence = sentences[0]
            words = sentence.split()
            
            # Find a good word to blank out (technical term or number)
            blank_idx = -1
            blank_word = ""
            
            # Prefer capitalized technical terms or numbers
            for idx, word in enumerate(words):
                if len(word) > 3 and (word[0].isupper() or word.isdigit()):
                    blank_idx = idx
                    blank_word = word
                    break
            
            # Fallback to middle word
            if blank_idx == -1 and len(words) > 5:
                blank_idx = len(words) // 2
                blank_word = words[blank_idx]
            
            if blank_idx >= 0:
                words[blank_idx] = '_____'
                quiz.append({
                    'type': 'FIB',
                    'question': ' '.join(words) + ".",
                    'options': [],
                    'correct': blank_word.strip('.,!?;:()[]'),
                    'explanation': f"Complete sentence: '{sentence}' ({ctx['source']}, page {ctx['page']})",
                    'source': ctx['source'],
                    'page': ctx['page']
                })
    
    return quiz if quiz else [{
        'type': 'MCQ',
        'question': f"What information is available about {topic}?",
        'options': [
            f"A) {context[0]['text'][:150]}...",
            "B) No information found",
            "C) Conflicting information",
            "D) Unclear from sources"
        ],
        'correct': 'A',
        'explanation': f"See {context[0]['source']}, page {context[0]['page']}",
        'source': context[0]['source'],
        'page': context[0]['page']
    }]


def parse_quiz(text, context, num_q):
    """Parse LLM output into structured quiz format with MCQ, TF, and FIB support"""
    import re
    
    quiz = []
    
    # Split by question blocks
    question_blocks = re.split(r'QUESTION \d+:', text)
    question_blocks = [q.strip() for q in question_blocks if q.strip()]
    
    for block in question_blocks:
        try:
            # Split by separator if present
            block = block.split('---')[0].strip()
            
            # Determine question type
            q_type = 'MCQ'  # default
            if block.startswith('TF'):
                q_type = 'TF'
                block = block[2:].strip()
            elif block.startswith('FIB'):
                q_type = 'FIB'
                block = block[3:].strip()
            elif block.startswith('MCQ'):
                block = block[3:].strip()
            
            # Extract question (everything before first option)
            lines = block.split('\n')
            question_text = []
            options = []
            correct = None
            explanation = ""
            
            i = 0
            # Get question text
            while i < len(lines) and not lines[i].strip().startswith(('A)', 'B)', 'C)', 'D)', 'CORRECT:')):
                if lines[i].strip():
                    question_text.append(lines[i].strip())
                i += 1
            
            # Get options (for MCQ and TF)
            if q_type in ['MCQ', 'TF']:
                while i < len(lines):
                    line = lines[i].strip()
                    if line.startswith(('A)', 'B)', 'C)', 'D)')):
                        options.append(line)
                    elif line.startswith('CORRECT:'):
                        correct = line.split(':', 1)[1].strip().upper()
                    elif line.startswith('EXPLANATION:'):
                        explanation = line.split(':', 1)[1].strip()
                        # Get rest of explanation
                        i += 1
                        while i < len(lines) and not lines[i].strip().startswith('QUESTION'):
                            if lines[i].strip():
                                explanation += " " + lines[i].strip()
                            i += 1
                        break
                    i += 1
            else:  # FIB - just get correct answer and explanation
                while i < len(lines):
                    line = lines[i].strip()
                    if line.startswith('CORRECT:'):
                        correct = line.split(':', 1)[1].strip()
                    elif line.startswith('EXPLANATION:'):
                        explanation = line.split(':', 1)[1].strip()
                        i += 1
                        while i < len(lines) and not lines[i].strip().startswith('QUESTION'):
                            if lines[i].strip():
                                explanation += " " + lines[i].strip()
                            i += 1
                        break
                    i += 1
            
            # Validate and add question
            if question_text and correct:
                if q_type == 'MCQ' and len(options) >= 4 and correct in ['A', 'B', 'C', 'D']:
                    quiz.append({
                        'type': 'MCQ',
                        'question': ' '.join(question_text),
                        'options': options[:4],
                        'correct': correct,
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0
                    })
                elif q_type == 'TF' and len(options) >= 2 and correct in ['A', 'B']:
                    quiz.append({
                        'type': 'TF',
                        'question': ' '.join(question_text),
                        'options': options[:2],
                        'correct': correct,
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0
                    })
                elif q_type == 'FIB' and correct:
                    quiz.append({
                        'type': 'FIB',
                        'question': ' '.join(question_text),
                        'options': [],
                        'correct': correct,
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0
                    })
        except Exception as e:
            st.warning(f"Failed to parse question: {str(e)[:100]}")
            continue
    
    if len(quiz) == 0:
        st.error("Failed to parse any questions from LLM output")
        return None
    
    return quiz


def grade_answers(quiz, answers):
    """Grade quiz answers with detailed feedback - supports MCQ, TF, and FIB"""
    score = 0
    feedback = []
    
    for i, (q, ans) in enumerate(zip(quiz, answers)):
        correct = q['correct']
        question_num = i + 1
        q_type = q.get('type', 'MCQ')
        
        # Check if correct
        is_correct = False
        if q_type == 'FIB':
            # Case-insensitive comparison for fill-in-the-blank
            is_correct = ans and ans.strip().lower() == correct.strip().lower()
        else:
            is_correct = ans == correct
        
        if is_correct:
            score += 1
            source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
            feedback.append(f"**Question {question_num}: CORRECT**\n{q['explanation']}\n*Source: {source_ref}*")
        else:
            source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
            
            if q_type == 'FIB':
                feedback.append(
                    f"**Question {question_num}: INCORRECT**\n"
                    f"Your answer: {ans if ans else '(blank)'}\n"
                    f"Correct answer: {correct}\n"
                    f"{q['explanation']}\n"
                    f"*Source: {source_ref}*"
                )
            else:
                correct_option = [opt for opt in q['options'] if opt.startswith(correct + ')')][0] if q['options'] else correct
                feedback.append(
                    f"**Question {question_num}: INCORRECT**\n"
                    f"Your answer: {ans if ans else '(not answered)'}\n"
                    f"Correct answer: {correct_option}\n"
                    f"{q['explanation']}\n"
                    f"*Source: {source_ref}*"
                )
    
    return score, feedback


# ============================================================================
# Tutor Mode
# ============================================================================

def generate_explanation(topic, context):
    """Generate detailed explanation with citations"""
    
    # Prepare context with source info
    context_blocks = []
    for i, c in enumerate(context[:5], 1):
        context_blocks.append(
            f"[Source {i}] {c['source']}, Page {c['page']}:\n{c['text'][:800]}"
        )
    
    context_text = "\n\n".join(context_blocks)
    
    if check_ollama():
        st.info("Generating explanation with local LLM...")
        
        prompt = f"""You are an expert tutor. Provide a detailed, accurate explanation of: "{topic}"

Use ONLY the information from these sources:

{context_text}

INSTRUCTIONS:
- Explain the concept clearly and thoroughly
- Use specific details from the sources
- Cite sources in your explanation like [Source 1, Page X]
- Organize information logically
- Use examples from the sources when available
- Be accurate - don't add information not in the sources

Provide your explanation:"""
        
        response = generate_with_ollama(prompt)
        if response:
            st.success("Explanation generated")
            return response, context
        else:
            st.warning("LLM generation failed. Showing raw context.")
    
    # Fallback: Format context nicely
    formatted = f"# Information about: {topic}\n\n"
    for i, c in enumerate(context[:5], 1):
        formatted += f"## Source {i}: {c['source']} (Page {c['page']})\n\n"
        formatted += f"{c['text'][:1000]}\n\n"
        formatted += "---\n\n"
    
    return formatted, context


# ============================================================================
# Streamlit UI
# ============================================================================

def main():
    st.set_page_config(page_title="RAG System", layout="wide")
    
    st.title("Local RAG: Quiz & Tutor")
    
    # Initialize
    if 'collection' not in st.session_state:
        try:
            client = chromadb.PersistentClient(path=VECTOR_DB_DIR)
            collection = client.get_collection(COLLECTION_NAME)
            st.session_state.collection = collection
            st.sidebar.success(f"{collection.count()} documents loaded")
        except:
            st.sidebar.warning("Database not initialized")
            if st.sidebar.button("Process PDFs"):
                with st.spinner("Processing..."):
                    collection = process_pdfs()
                    if collection:
                        st.session_state.collection = collection
                        st.rerun()
            return
    
    collection = st.session_state.collection
    
    # Check Ollama
    ollama_status = check_ollama()
    st.sidebar.info(f"Ollama: {'Running' if ollama_status else 'Not running'}")
    if not ollama_status:
        st.sidebar.caption("Install: `ollama pull llama2`")
    
    # Mode selection
    mode = st.sidebar.radio("Mode", ["Quiz", "Tutor"])
    
    # Quiz Mode
    if mode == "Quiz":
        st.header("Quiz Generator")
        
        topic = st.text_input("Topic:", placeholder="e.g., TCP Protocol, RSA Encryption")
        
        if st.button("Generate Quiz", type="primary"):
            if topic:
                with st.spinner("Generating 5-question quiz..."):
                    context, src_type = get_context(topic, collection)
                    
                    if context:
                        quiz = generate_quiz(topic, context, 5)
                        if quiz and len(quiz) > 0:
                            st.session_state.quiz = quiz
                            st.session_state.quiz_context = context
                            st.session_state.src_type = src_type
                            st.session_state.user_answers = {}  # Reset answers
                            st.rerun()
                        else:
                            st.error("Failed to generate quiz. Please ensure Ollama is running and try again.")
                    else:
                        st.error("No context found for this topic")
        
        # Display quiz if available (OUTSIDE button condition)
        if 'quiz' in st.session_state and st.session_state.quiz:
            quiz = st.session_state.quiz
            
            st.success(f"Quiz from {st.session_state.get('src_type', 'local')} sources")
            st.markdown("---")
            
            # Form to prevent rerun on every interaction
            with st.form("quiz_form"):
                answers = []
                for i, q in enumerate(quiz):
                    q_type = q.get('type', 'MCQ')
                    st.markdown(f"### Question {i+1} ({q_type})")
                    # Display question text without extra markdown formatting
                    st.write(q['question'])
                    
                    if q_type == 'FIB':
                        # Fill-in-the-blank: text input
                        ans = st.text_input(
                            "Your answer:",
                            key=f"q_{i}",
                            value="",
                            placeholder="Type your answer here"
                        )
                        answers.append(ans)
                    else:
                        # MCQ and TF: radio buttons (no default selection)
                        ans = st.radio(
                            "Select your answer:",
                            q['options'],
                            key=f"q_{i}",
                            index=None
                        )
                        answers.append(ans[0] if ans else None)
                
                submitted = st.form_submit_button("Submit Answers", type="primary")
                
                if submitted:
                    # Check if all questions are answered
                    unanswered = []
                    for i, (q, ans) in enumerate(zip(quiz, answers)):
                        if q.get('type') == 'FIB':
                            if not ans or not ans.strip():
                                unanswered.append(i + 1)
                        else:
                            if ans is None:
                                unanswered.append(i + 1)
                    
                    if unanswered:
                        st.warning(f"Please answer all questions before submitting. Unanswered: {unanswered}")
                    else:
                        score, feedback = grade_answers(quiz, answers)
                        st.markdown(f"## Score: {score}/{len(quiz)}")
                        st.markdown("---")
                        for fb in feedback:
                            st.markdown(fb)
                            st.markdown("---")
            
            # Citations
            if 'quiz_context' in st.session_state:
                with st.expander("Sources"):
                    for c in st.session_state.quiz_context[:5]:
                        st.markdown(f"- **{c['source']}** (Page {c['page']})")
            
            if st.button("New Quiz"):
                for key in ['quiz', 'quiz_context', 'user_answers', 'src_type']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
    
    # Tutor Mode
    else:
        st.header("AI Tutor")
        
        topic = st.text_area(
            "Ask anything:", 
            placeholder="e.g., Explain how RSA encryption works",
            height=100
        )
        
        if st.button("Get Explanation", type="primary"):
            if topic:
                with st.spinner("Searching knowledge base..."):
                    context, src_type = get_context(topic, collection)
                    
                    if context and len(context) > 0 and src_type != "none":
                        st.session_state.tutor_response = None
                        st.session_state.tutor_context = context
                        st.session_state.tutor_src_type = src_type
                        
                        explanation, ctx = generate_explanation(topic, context)
                        st.session_state.tutor_response = explanation
                        st.rerun()
                    else:
                        st.error("No relevant information found in local sources or web")
                        st.info("Tips: Try different keywords, check your internet connection, or add relevant PDFs to the Source folder")
        
        # Display explanation if available
        if 'tutor_response' in st.session_state and st.session_state.tutor_response:
            st.markdown("---")
            
            # Show source type
            src_badge = st.session_state.get('tutor_src_type', 'local')
            st.success(f"Information from {src_badge} sources")
            
            # Display explanation
            st.markdown("## Explanation")
            st.markdown(st.session_state.tutor_response)
            
            # Citations
            st.markdown("---")
            st.markdown("### Source Citations")
            
            if 'tutor_context' in st.session_state:
                for i, c in enumerate(st.session_state.tutor_context[:5], 1):
                    with st.expander(f"Source {i}: {c['source']} (Page {c['page']})"):
                        st.markdown(f"**Relevance Score:** {c.get('score', 'N/A')}")
                        st.markdown("**Content Preview:**")
                        st.text(c['text'][:500] + "...")
            
            if st.button("Ask Another Question"):
                for key in ['tutor_response', 'tutor_context', 'tutor_src_type']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()


if __name__ == "__main__":
    main()
