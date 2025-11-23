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


# ----------------------
# Text sanitization helper
# ----------------------
def sanitize_text(t: str) -> str:
    """Clean raw text extracted from PDFs or web to remove bullets, odd chars, and collapse whitespace."""
    import re
    if not t:
        return ""
    # remove common bullet characters and leading bullets at line starts
    t = re.sub(r"^[\s\u2022\-\*]+", "", t, flags=re.MULTILINE)
    # remove stray bullets inside text
    t = t.replace('\u2022', ' ').replace('•', ' ')
    # collapse multiple whitespace/newlines
    t = re.sub(r"\s+", " ", t)
    # strip weird leading/trailing punctuation
    t = t.strip(' \n\t\r\f\v\u2022\u2023.,:;-')
    return t


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
    """Generate quiz with LLM"""
    # Ensure minimum questions to include required types
    num_q = max(num_q, 3)
    # Build numbered context blocks so LLM can cite like [Source 1, Page X]
    context_blocks = []
    for idx, c in enumerate(context[:6], start=1):
        raw = c.get('text', '') or ''
        excerpt = sanitize_text(raw[:800])
        context_blocks.append(f"[Source {idx}] {c.get('source','Unknown')}, Page {c.get('page','N/A')}:\n{excerpt}")
    context_text = "\n\n".join(context_blocks)
    
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
    # Improved prompt: request mixed types and strict machine-parseable format
    prompt = f"""You are a quiz generator. Based ONLY on the CONTEXT below about \"{topic}\", produce exactly {num_q} questions. Use the context's source markers when citing.

CONTEXT:
{context_text}

REQUIREMENTS:
- Produce at least 2 True/False questions (type `tf`) and at least 1 open-ended fill-in-the-blank question (type `open`) among the {num_q} questions.
- Remaining questions may be multiple-choice (`mcq`) with four options A/B/C/D and exactly one correct answer.
- Use ONLY information present in the CONTEXT. Do NOT invent facts.
- For each question include an explicit TYPE line: `TYPE: mcq` or `TYPE: tf` or `TYPE: open`.
- For `mcq` include options A) B) C) D). For `tf` include options `A) True` and `B) False`. For `open` include no options and put the expected answer in `CORRECT:` as the text answer.
- Always include a `SOURCE:` line that cites the context like `[Source 1, Page X]` (use the source numbers provided in the CONTEXT block).
- Follow this exact machine-parsable format for every question (no extra commentary):
 - Options must be meaningful natural-language choices. Do NOT output step labels like `Step1`, `Step2`, or file names such as `Lecture_13_slides` as options.
 - Avoid single-word placeholders (e.g., `encryption`) for open answers where possible; prefer multi-word technical phrases or clearly defined terms from the context.
 - Keep options as descriptive short phrases (2-10 words) for readability.
 - For `mcq` include options A) B) C) D). For `tf` include options `A) True` and `B) False`. For `open` include no options and put the expected answer in `CORRECT:` as the text answer.

QUESTION [number]:
TYPE: [mcq|tf|open]
[Question text]
A) [Option A]    (only for mcq or tf)
B) [Option B]    (only for mcq or tf)
C) [Option C]    (only for mcq)
D) [Option D]    (only for mcq)
CORRECT: [A/B/C/D] or for TF use A or B, for OPEN use the exact expected answer text
EXPLANATION: [Short explanation and cite SOURCE]
SOURCE: [Source 1, Page X]

Now generate the quiz strictly in that format:
"""
    
    ollama_available = check_ollama()
    
    if ollama_available:
        st.info("Generating quiz with local LLM (qwen2.5:7b-instruct)...")
        response = generate_with_ollama(prompt)
        if response:
            parsed = parse_quiz(response, context)
            if parsed and len(parsed) > 0:
                st.success(f"Generated {len(parsed)} questions from LLM")
                # Ensure minimum composition: at least 2 True/False and 1 open-ended
                tf_count = sum(1 for q in parsed if q.get('type') == 'tf')
                open_count = sum(1 for q in parsed if q.get('type') == 'open')
                additions = []
                if tf_count < 2:
                    for _ in range(2 - tf_count):
                        additions.append(create_template_tf(context))
                if open_count < 1:
                    additions.append(create_template_open(topic, context))

                if additions:
                    parsed.extend(additions)

                # Validate parsed questions: avoid options that are just filenames or source names
                cleaned = []
                for q in parsed:
                    bad = False
                    if q.get('type') == 'mcq':
                        for opt in q.get('options', []):
                            # if option contains 'Lecture' or 'slides' or 'Lecture_' treat as bad
                            if any(tok.lower() in opt.lower() for tok in ['lecture', 'slides', '.pdf', 'lecture_']):
                                bad = True
                                break
                        if bad:
                            # replace with a template MCQ based on context
                            repl = create_template_quiz(topic, context, 1)
                            if repl:
                                r = repl[0]
                                r['type'] = 'mcq'
                                cleaned.append(r)
                            else:
                                cleaned.append(q)
                    else:
                        cleaned.append(q)

                # Ensure we have exactly num_q questions
                if len(cleaned) > num_q:
                    # Trim excess while keeping required types
                    tf_qs = [q for q in cleaned if q.get('type') == 'tf']
                    open_qs = [q for q in cleaned if q.get('type') == 'open']
                    mcq_qs = [q for q in cleaned if q.get('type') == 'mcq']
                    
                    final = []
                    final.extend(tf_qs[:2])  # Keep 2 TF
                    final.extend(open_qs[:1])  # Keep 1 open
                    remaining = num_q - len(final)
                    final.extend(mcq_qs[:remaining])  # Fill rest with MCQ
                    cleaned = final
                elif len(cleaned) < num_q:
                    # Pad with additional MCQs from template
                    needed = num_q - len(cleaned)
                    extra_mcqs = create_template_quiz(topic, context, needed)
                    for extra in extra_mcqs[:needed]:
                        if extra.get('type') != 'tf' and extra.get('type') != 'open':
                            extra['type'] = 'mcq'
                    cleaned.extend(extra_mcqs[:needed])

                return cleaned
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
    context_idx = 0
    
    while len(quiz) < num_q and context_idx < len(context):
        ctx = context[context_idx]
        context_idx += 1
        
        raw_text = ctx.get('text', '')
        text = sanitize_text(raw_text)
        
        # Extract sentences
        sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 30]
        if len(sentences) < 2:
            continue
        
        # Use first meaningful sentence as basis
        main_fact = sentences[0]
        
        # Create question
        question = f"According to {ctx.get('source','Unknown')} (page {ctx.get('page','N/A')}), {topic}:"
        
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
            'explanation': f"Based on {ctx.get('source','Unknown')}, page {ctx.get('page','N/A')}: {main_fact}",
            'source': ctx.get('source','Unknown'),
            'page': ctx.get('page','N/A')
            ,'type': 'mcq'
        })
    
    # If no quiz generated, create a fallback question
    if not quiz:
        quiz = [{
            'question': f"What information is available about {topic}?",
            'options': [
                f"A) {sanitize_text(context[0].get('text','')[:150])}...",
                "B) No information found",
                "C) Conflicting information",
                "D) Unclear from sources"
            ],
            'correct': 'A',
            'explanation': f"See {context[0].get('source','Unknown')}, page {context[0].get('page','N/A')}",
            'source': context[0].get('source','Unknown'),
            'page': context[0].get('page','N/A'),
            'type': 'mcq'
        }]
    
    # Ensure at least 2 TF and 1 open if num_q allows
    if num_q >= 3:
        tf_count = sum(1 for q in quiz if q.get('type') == 'tf')
        open_count = sum(1 for q in quiz if q.get('type') == 'open')
        
        # Add required TF questions
        while tf_count < 2 and len(quiz) < num_q:
            quiz.append(create_template_tf(context))
            tf_count += 1
        
        # Add required open question
        if open_count < 1 and len(quiz) < num_q:
            quiz.append(create_template_open(topic, context))
    
    # Trim to exactly num_q if we exceeded
    if len(quiz) > num_q:
        # Prioritize keeping required types (2 TF, 1 open)
        tf_questions = [q for q in quiz if q.get('type') == 'tf']
        open_questions = [q for q in quiz if q.get('type') == 'open']
        mcq_questions = [q for q in quiz if q.get('type') == 'mcq']
        
        # Keep at least 2 TF and 1 open, fill rest with MCQ
        final = []
        final.extend(tf_questions[:2])
        final.extend(open_questions[:1])
        remaining = num_q - len(final)
        final.extend(mcq_questions[:remaining])
        quiz = final
    
    return quiz


def create_template_tf(context):
    """Create a True/False question from context"""
    # Use first chunk as basis
    c = context[0]
    raw = c.get('text','')
    s = sanitize_text(raw)
    text = s.split('.')
    fact = text[0] if text and text[0] else s[:120]

    question = f"True or False: {fact.strip()}"
    options = ["A) True", "B) False"]
    # Assume True as correct for template (user should verify)
    return {
        'question': question,
        'options': options,
        'correct': 'A',
        'explanation': f"See {c.get('source','Unknown')}, page {c.get('page','N/A')}.",
        'source': c.get('source','Unknown'),
        'page': c.get('page', 0),
        'type': 'tf'
    }


def create_template_open(topic, context):
    """Create an open-ended fill-in-the-blank question"""
    c = context[0]
    import re
    # sanitize the context text
    raw = c.get('text','')
    s = sanitize_text(raw)

    # Pick a meaningful sentence from context (prefer longer, informative sentences)
    sentences = [ss.strip() for ss in re.split(r'[\.\n]', s or '') if len(ss.strip()) > 30]
    sent = sentences[0] if sentences else (s or '').strip()
    if not sent:
        # fallback to source or topic
        sent = c.get('source', '') or topic or 'Complete the following'


    # Choose candidate phrase: prefer multi-word technical phrases (2-3 words) located after first two tokens
    words = re.findall(r"\w+", sent)
    keyword = None
    # search for 3-word then 2-word windows where words are reasonably long
    for window in (3, 2):
        for i in range(2, max(0, len(words) - window + 1)):
            w = words[i:i+window]
            if all(len(x) > 3 for x in w) and any(len(x) > 5 for x in w):
                keyword = ' '.join(w)
                break
        if keyword:
            break

    # fallback to single long word (not in first two tokens)
    if not keyword:
        candidates = [w for idx, w in enumerate(words) if idx > 1 and len(w) > 5]
        if candidates:
            keyword = candidates[0]
        elif words:
            keyword = max(words, key=len)
        else:
            keyword = (topic.split()[0] if topic and len(topic.split()) > 0 else 'answer')

    # Avoid numeric or trivial keyword
    if isinstance(keyword, str) and (keyword.isdigit() or len(keyword) < 2):
        keyword = (topic.split()[0] if topic else 'answer')

    # Replace only first occurrence (case-insensitive), safe fallback
    try:
        pattern = re.compile(re.escape(keyword), re.IGNORECASE)
        sentence_with_blank = pattern.sub('____', sent, count=1)
    except Exception:
        sentence_with_blank = sent + ' ____'

    # If the blank is at the very start or results in an unhelpful fragment,
    # rephrase to include the full sentence for context; do NOT include inline filename citation
    if sentence_with_blank.strip().startswith('____') or len(sentence_with_blank.split()) < 4:
        question = f"Fill in the blank: In the sentence '{sent}', the missing term is: ____"
    else:
        question = f"Fill in the blank: {sentence_with_blank}"

    return {
        'question': question,
        'options': [],
        'correct': keyword,
        'explanation': f"See {c.get('source','Unknown')}, page {c.get('page','N/A')}: {sent[:300]}",
        'source': c.get('source','Unknown'),
        'page': c.get('page', 0),
        'type': 'open'
    }


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
            qtype = None
            source = None
            explanation = ""
            
            i = 0
            # Read TYPE if present on first lines
            while i < len(lines) and lines[i].strip() == '':
                i += 1
            if i < len(lines) and lines[i].strip().upper().startswith('TYPE:'):
                qtype = lines[i].split(':',1)[1].strip().lower()
                i += 1
            # Get question text
            while i < len(lines) and not lines[i].strip().startswith(('A)', 'B)', 'C)', 'D)')):
                if lines[i].strip():
                    # sanitize question text line
                    question_text.append(sanitize_text(lines[i].strip()))
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
                elif line.upper().startswith('TYPE:'):
                    qtype = line.split(':',1)[1].strip().lower()
                elif line.upper().startswith('SOURCE:'):
                    source = line.split(':',1)[1].strip()
                i += 1
            
            # Validate and add question
            q_obj = None
            if question_text:
                q_text = ' '.join(question_text)
                # Determine type: mcq, tf, open
                if len(options) >= 4 and correct in ['A', 'B', 'C', 'D']:
                    q_obj = {
                        'question': q_text,
                        'options': options[:4],
                        'correct': correct,
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0,
                        'type': 'mcq'
                    }
                elif any('True' in o or 'False' in o for o in options):
                    # True/False question
                    # Normalize to A) True, B) False
                    opt_true = next((o for o in options if 'True' in o), 'A) True')
                    opt_false = next((o for o in options if 'False' in o), 'B) False')
                    corr = None
                    if correct and ('TRUE' in correct or 'T' == correct):
                        corr = 'A'
                    elif correct and ('FALSE' in correct or 'F' == correct):
                        corr = 'B'
                    else:
                        # try to read CORRECT: A/B
                        corr = correct if correct in ['A', 'B'] else 'A'

                    q_obj = {
                        'question': q_text,
                        'options': [f"A) True", f"B) False"],
                        'correct': corr,
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0,
                        'type': 'tf'
                    }
                elif (not options) and correct and len(correct) > 0:
                    # Open-ended question where CORRECT contains the answer text
                    q_obj = {
                        'question': q_text,
                        'options': [],
                        'correct': correct.strip(),
                        'explanation': explanation if explanation else "See context above.",
                        'source': context[0]['source'] if context else "Unknown",
                        'page': context[0]['page'] if context else 0,
                        'type': 'open'
                    }

            if q_obj:
                # attach parsed type/source if LLM provided them
                if qtype and 'type' not in q_obj:
                    q_obj['type'] = qtype
                if source and 'source' in q_obj and q_obj.get('source') == 'Unknown':
                    q_obj['source'] = source
                # sanitize options text to remove bullets and file-like labels
                if 'options' in q_obj and q_obj['options']:
                    clean_opts = []
                    for o in q_obj['options']:
                        if not o:
                            clean_opts.append(None)
                            continue
                        o_clean = sanitize_text(o)
                        # collapse things like 'Step1' or 'Step 1' into a bad marker
                        if re.match(r"^Step\s*\d+", o_clean, flags=re.IGNORECASE) or re.search(r"lecture|slides|\.pdf", o_clean, flags=re.IGNORECASE) or o_clean.strip() == '':
                            o_clean = None
                        # remove leading bullet-like characters
                        if o_clean and o_clean.lstrip().startswith(('•','-','*')):
                            o_clean = o_clean.lstrip('•-* ').strip()
                        clean_opts.append(o_clean)
                    # If any option is None or too short, mark question as bad to be replaced later
                    if any(co is None or len(co.strip()) < 3 for co in clean_opts):
                        q_obj['bad_options'] = True
                    else:
                        q_obj['options'] = [co for co in clean_opts]
                quiz.append(q_obj)
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
        qtype = q.get('type', 'mcq')
        if qtype in ['mcq', 'tf']:
            if ans == correct:
                score += 1
                source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
                feedback.append(f"**Question {question_num}: CORRECT**\n{q['explanation']}\n*Source: {source_ref}*")
            else:
                correct_option = [opt for opt in q.get('options', []) if opt.startswith(correct + ')')]
                correct_option = correct_option[0] if correct_option else correct
                source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
                feedback.append(
                    f"**Question {question_num}: INCORRECT**\n"
                    f"Your answer: {ans}\n"
                    f"Correct answer: {correct_option}\n"
                    f"{q['explanation']}\n"
                    f"*Source: {source_ref}*"
                )
        elif qtype == 'open':
            # Simple string/token overlap check for open answers
            user = (ans or '').strip().lower()
            expected = (correct or '').strip().lower()
            is_correct = False
            if not expected:
                is_correct = False
            elif user == expected:
                is_correct = True
            else:
                user_tokens = set([t.strip('.,') for t in user.split() if t])
                exp_tokens = set([t.strip('.,') for t in expected.split() if t])
                if len(exp_tokens) > 0:
                    overlap = len(user_tokens & exp_tokens) / len(exp_tokens)
                    is_correct = overlap >= 0.6

            if is_correct:
                score += 1
                source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
                feedback.append(f"**Question {question_num}: CORRECT**\n{q['explanation']}\n*Source: {source_ref}*")
            else:
                source_ref = f"[{q.get('source', 'Unknown')}, Page {q.get('page', 'N/A')}]"
                feedback.append(
                    f"**Question {question_num}: INCORRECT**\n"
                    f"Your answer: {ans}\n"
                    f"Expected: {correct}\n"
                    f"{q.get('explanation','')}\n"
                    f"*Source: {source_ref}*"
                )
        else:
            # Default fallback
            if ans == correct:
                score += 1
            feedback.append(f"**Question {question_num}: Reviewed**\n{q.get('explanation','')}\n")
    
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
                        # Reset answers and any previous question widgets to avoid retained selections
                        st.session_state.user_answers = {}
                        # Remove any keys that start with quiz question widget prefixes
                        keys_to_remove = [k for k in list(st.session_state.keys()) if str(k).startswith('q_')]
                        for k in keys_to_remove:
                            del st.session_state[k]
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
                    qtype = q.get('type', 'mcq')
                    if qtype in ['mcq', 'tf']:
                        # Render radio options with no default selection (index=None)
                        ans = st.radio(
                            "Select your answer:",
                            q.get('options', []),
                            key=f"q_{i}",
                            index=None
                        )
                        # Extract letter from selected option (e.g., 'A' from 'A) ...')
                        answers.append(ans[0] if ans and len(ans) > 0 else None)
                    elif qtype == 'open':
                        # Render text input for open-ended / fill-in-the-blank
                        ans = st.text_input("Your answer:", key=f"q_{i}_open")
                        answers.append(ans.strip() if ans else "")
                    else:
                        # Fallback to radio with no default
                        ans = st.radio(
                            "Select your answer:",
                            q.get('options', []),
                            key=f"q_{i}",
                            index=None
                        )
                        answers.append(ans[0] if ans and len(ans) > 0 else None)
                
                submitted = st.form_submit_button("Submit Answers", type="primary")
                
                if submitted:
                    # Validate all answers present
                    missing_indices = []
                    for i, q in enumerate(quiz):
                        qtype = q.get('type', 'mcq')
                        a = answers[i]
                        if qtype in ['mcq', 'tf'] and (a is None or a == ''):
                            missing_indices.append(i+1)
                        if qtype == 'open' and (a is None or str(a).strip() == ''):
                            missing_indices.append(i+1)

                    if missing_indices:
                        st.warning(f"Please answer all questions before submitting. Missing: Question(s) {', '.join(map(str, missing_indices))}")
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
                # Clear main quiz state and any question widget keys
                for key in ['quiz', 'quiz_context', 'user_answers', 'src_type']:
                    if key in st.session_state:
                        del st.session_state[key]
                keys_to_remove = [k for k in list(st.session_state.keys()) if str(k).startswith('q_')]
                for k in keys_to_remove:
                    del st.session_state[k]
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
