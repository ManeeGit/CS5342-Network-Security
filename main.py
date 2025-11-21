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
from duckduckgo_search import DDGS
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
    """Fallback web search - tries DuckDuckGo then Wikipedia"""
    
    # Try DuckDuckGo first
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            
            if results:
                web_results = []
                for r in results:
                    content = f"{r.get('title', '')}\n\n{r.get('body', '')}"
                    web_results.append({
                        'text': content,
                        'source': r.get('href', 'Unknown'),
                        'page': 'Web',
                        'score': 0.8
                    })
                return web_results
    except:
        pass
    
    # Fallback to Wikipedia
    st.info("Searching Wikipedia...")
    wiki_results = search_wikipedia(query)
    
    if wiki_results:
        return wiki_results
    
    st.error("All web search methods failed")
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
    """Generate quiz with LLM"""
    
    context_text = "\n\n".join([
        f"[Source: {c['source']}, Page {c['page']}]\n{c['text'][:600]}"
        for c in context[:3]
    ])
    
    prompt = f"""You are a quiz generator. Based on the following context about "{topic}", create {num_q} multiple choice questions.

CONTEXT:
{context_text}

INSTRUCTIONS:
- Create exactly {num_q} questions
- Each question must have 4 options (A, B, C, D)
- Only ONE option should be correct
- Provide explanation with source reference
- Use EXACTLY this format for each question:

QUESTION [number]:
[Your question text here]
A) [Option A]
B) [Option B]
C) [Option C]
D) [Option D]
CORRECT: [A/B/C/D]
EXPLANATION: [Why this is correct and which page/source it comes from]

---

Now generate the quiz:"""
    
    ollama_available = check_ollama()
    
    if ollama_available:
        st.info("Generating quiz with local LLM (qwen2.5:7b-instruct)...")
        response = generate_with_ollama(prompt)
        if response:
            parsed = parse_quiz(response, context)
            if parsed and len(parsed) > 0:
                st.success(f"Generated {len(parsed)} questions from LLM")
                return parsed
            else:
                st.warning("Failed to parse LLM output. Using template quiz.")
        else:
            st.warning("LLM generation failed. Using template quiz.")
    else:
        st.warning("Ollama not connected. Using template-based quiz.")
    
    return create_template_quiz(topic, context, num_q)


def create_template_quiz(topic, context, num_q):
    """Generate quiz from context content"""
    quiz = []
    
    for i in range(min(num_q, len(context))):
        ctx = context[i]
        text = ctx['text']
        
        # Extract sentences
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 30]
        if len(sentences) < 2:
            continue
        
        # Use first meaningful sentence as basis
        main_fact = sentences[0]
        
        # Create question
        question = f"According to {ctx['source']} (page {ctx['page']}), {topic}:"
        
        # Create options with variations
        options = [
            f"A) {main_fact[:150]}" if len(main_fact) > 150 else f"A) {main_fact}",
            f"B) Is not discussed in this context",
            f"C) Is mentioned but with different details",
            f"D) Contradicts the source material"
        ]
        
        quiz.append({
            'question': question,
            'options': options,
            'correct': 'A',
            'explanation': f"Based on {ctx['source']}, page {ctx['page']}: {main_fact}",
            'source': ctx['source'],
            'page': ctx['page']
        })
    
    return quiz if quiz else [{
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


def parse_quiz(text, context):
    """Parse LLM output into structured quiz format"""
    import re
    
    quiz = []
    
    # Split by question blocks
    question_blocks = re.split(r'QUESTION \d+:', text)
    question_blocks = [q.strip() for q in question_blocks if q.strip()]
    
    for block in question_blocks:
        try:
            # Split by separator if present
            block = block.split('---')[0].strip()
            
            # Extract question (everything before first option)
            lines = block.split('\n')
            question_text = []
            options = []
            correct = None
            explanation = ""
            
            i = 0
            # Get question text
            while i < len(lines) and not lines[i].strip().startswith(('A)', 'B)', 'C)', 'D)')):
                if lines[i].strip():
                    question_text.append(lines[i].strip())
                i += 1
            
            # Get options
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
            
            # Validate and add question
            if question_text and len(options) >= 4 and correct in ['A', 'B', 'C', 'D']:
                quiz.append({
                    'question': ' '.join(question_text),
                    'options': options[:4],
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
    """Grade quiz answers with detailed feedback"""
    score = 0
    feedback = []
    
    for i, (q, ans) in enumerate(zip(quiz, answers)):
        correct = q['correct']
        question_num = i + 1
        
        if ans == correct:
            score += 1
            source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
            feedback.append(f"**Question {question_num}: CORRECT**\n{q['explanation']}\n*Source: {source_ref}*")
        else:
            correct_option = [opt for opt in q['options'] if opt.startswith(correct + ')')][0] if q['options'] else "N/A"
            source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
            feedback.append(
                f"**Question {question_num}: INCORRECT**\n"
                f"Your answer: {ans}\n"
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
        
        col1, col2 = st.columns([3, 1])
        with col1:
            topic = st.text_input("Topic:", placeholder="e.g., TCP Protocol")
        with col2:
            num_q = st.slider("Questions:", 1, 10, 5)
        
        if st.button("Generate Quiz", type="primary"):
            if topic:
                with st.spinner("Generating..."):
                    context, src_type = get_context(topic, collection)
                    
                    if context:
                        quiz = generate_quiz(topic, context, num_q)
                        st.session_state.quiz = quiz
                        st.session_state.quiz_context = context
                        st.session_state.src_type = src_type
                        st.session_state.user_answers = {}  # Reset answers
                        st.rerun()
        
        # Display quiz if available (OUTSIDE button condition)
        if 'quiz' in st.session_state and st.session_state.quiz:
            quiz = st.session_state.quiz
            
            st.success(f"Quiz from {st.session_state.get('src_type', 'local')} sources")
            st.markdown("---")
            
            # Form to prevent rerun on every interaction
            with st.form("quiz_form"):
                answers = []
                for i, q in enumerate(quiz):
                    st.markdown(f"### Question {i+1}")
                    st.markdown(f"**{q['question']}**")
                    
                    ans = st.radio(
                        "Select your answer:",
                        q['options'],
                        key=f"q_{i}",
                        index=None
                    )
                    answers.append(ans[0] if ans else None)
                
                submitted = st.form_submit_button("Submit Answers", type="primary")
                
                if submitted:
                    if None in answers:
                        st.warning("Please answer all questions before submitting")
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
