# CS5342  Network Security Project
## Round-2 Prototype Submission  README
### Local Network-Security Tutor & Quiz Agent (Privacy-Preserving)

---

# 1. Project Statement

Network security courses include hundreds of pages of slides, textbook content, and quizzes. Manually searching these documents is time-consuming, and using online LLMs (ChatGPT, Gemini) violates **data privacy requirements** because documents cannot be uploaded to the cloud.

To solve this, we built a **local, privacy-preserving AI Tutor & Quiz Generator** that:

- Runs fully **offline**
- Processes **local network security documents only**
- Answers questions with **document-level citations**
- Generates **MCQs with auto-grading**
- Provides **detailed feedback with page numbers**
- Protects student data using a **local vector database + local LLM**

This meets **all Round-2 CS5342 project requirements**.

---

#  **2. Project Description**

Our system has **two core agents**:

### **1 Q&A Tutor Agent**
- Takes any network-security question
- Converts the question into embeddings
- Retrieves relevant document chunks from ChromaDB
- Generates a response using Ollama (qwen2.5:7b-instruct)
- Displays **citation (document + page number)**
- Works 100% offline

### **2 Quiz Agent**
- Generates **topic-specific quizzes**
- Supports:
  - Multiple Choice Questions (MCQs)
  - 4 options per question
  - Detailed explanations
- Grades user answers automatically
- Provides feedback + correct answers + citations
- Falls back to template mode if LLM unavailable

---

#  **3. System Environment**

### **Operating Systems**
- macOS
- Windows
- Linux

### **Python Version**
- Python **3.12** (recommended)
- Python **3.9 or above** (minimum)

### **Hardware Requirements**
- 8GB RAM minimum (16GB recommended)
- CPU-only supported (no GPU required)
- 10GB disk space for models and database

---

#  **4. Adopted Libraries**

| Library | Purpose |
|--------|---------|
| **streamlit** | Modern web-based UI framework |
| **chromadb** | Local vector database for embeddings |
| **pymupdf (fitz)** | Extract text from PDF documents |
| **ollama** | Local LLM API client |
| **wikipedia** | Fallback web search (optional) |
| **duckduckgo-search** | Web search fallback |

Install all dependencies:

```bash
pip install streamlit chromadb pymupdf ollama wikipedia duckduckgo-search
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

---

#  **5. Ollama Setup (Local LLM)**

### **Installation**

**Windows/macOS/Linux:**
```bash
# Download from https://ollama.ai/
# Or use package manager

# Windows (PowerShell)
winget install Ollama.Ollama

# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh
```

### **Download Model**

```bash
# Pull the qwen2.5:7b-instruct model (recommended)
ollama pull qwen2.5:7b-instruct

# Start Ollama service
ollama serve
```

The service runs at `http://localhost:11434`

---

#  **6. Virtual Environment Setup**

### **macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **Windows**
```powershell
python -m venv venv
venv\Scripts\activate
```

If PowerShell gives permission error:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

#  **7. Project Structure**

```
RAG/
 main.py                          # Main application (single file)
 requirements.txt                 # Python dependencies
 ARCHITECTURE.md                  # System architecture documentation
 architecture-diagram.mmd         # Mermaid diagram source
 README.md                        # This file
 .gitignore                       # Git ignore file

 Source/                          # Input PDFs (71 documents)
    Lecture 1_slides.pdf
    Lecture 2_slides.pdf
    ... (network security materials)

 processed_docs/                  # Extracted markdown files
    Lecture 1_slides.md
    Lecture 2_slides.md
    ... (71 markdown files)

 vectordb/                        # ChromaDB persistent storage
     (1072 document chunks with embeddings)
```

---

#  **8. Training Data & Data Format**

### **Knowledge Documents**
Stored in:

```
Source/
```

Includes:
- CS5342 lecture slides (25 lectures)
- Network security textbooks (3 books)
- Homework assignments (3 files)
- Total: **71 PDF documents**

### **Chunking Method**
- PDFs extracted using **PyMuPDF (fitz)**
- Each page converted to text independently
- No overlap chunking (page-level granularity)
- Preserves page numbers for accurate citations

### **Embedding Model**
- **ChromaDB Default Embeddings** (all-MiniLM-L6-v2)
- Embedding vector size: **384 dimensions**
- Distance metric: **Cosine similarity**
- Index type: **HNSW** (Hierarchical Navigable Small World)

### **ChromaDB Collection Structure**

Each entry contains:
```python
{
    "id": "filename_pN",           # Unique identifier
    "text": "page content...",      # Full page text
    "metadata": {
        "source": "document_name",  # PDF filename
        "page": N                   # Page number
    },
    "embedding": [0.1, -0.3, ...]  # 384-dim vector
}
```

**Total Storage:**
- **1072 document chunks** (one per page)
- **~50-100 MB** vector database size

---

#  **9. Execution Flow**

### **Step 1  Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 2  Setup Ollama**
```bash
# Download and install from https://ollama.ai/
ollama pull qwen2.5:7b-instruct
ollama serve  # Keep this running
```

### **Step 3  Add PDFs**
Place all documents into:
```
Source/
```

### **Step 4  Launch the Application**
```bash
streamlit run main.py
```

### **Step 5  Process PDFs (First Time Only)**
1. Open the web interface at `http://localhost:8501`
2. Click **"Process PDFs"** in the sidebar
3. Wait for processing to complete (~2-5 minutes for 71 PDFs)
4. Database will be created automatically in `vectordb/`

### **Step 6  Use the System**
- Select **Quiz** or **Tutor** mode from sidebar
- Enter your query/topic
- Get responses with citations

---

#  **10. System Architecture Diagram**

See `ARCHITECTURE.md` for complete system documentation.

View the interactive diagram:
```bash
# Open architecture-diagram.mmd in:
# - VS Code (with Mermaid extension)
# - https://mermaid.live/
# - GitHub (renders automatically)
```

**High-Level Flow:**

```
User Input (Streamlit UI)
    
Context Retrieval Layer
     ChromaDB Vector Search (local)
       Score > 0.4?  Use local context
     Web Search Fallback
        DuckDuckGo (primary)
        Wikipedia (secondary)
    
Generation Layer
     Ollama LLM (if available)
       qwen2.5:7b-instruct
     Template Mode (fallback)
    
Response with Citations
     Display in UI
```

---

#  **11. Core Features**

###  Q&A Tutor Agent
- Detailed explanations with context
- Source citations with page numbers
- Expandable source previews
- Local + web search hybrid

###  Quiz Agent
- Topic-specific quiz generation
- Multiple choice questions (4 options)
- LLM-generated questions (when available)
- Template-based fallback

###  Offline, Privacy-Preserving
- 100% local processing
- No cloud API calls (except optional web search)
- Data never leaves your machine
- GDPR/Privacy compliant

###  Auto-Grading
- Exact match for MCQs
- Detailed feedback
- Shows correct answers
- Source citations in explanations

###  Citations Included
- Document name + page number
- Relevance scores
- Content previews
- Direct source linking

---

#  **12. Issues & Solutions**

### **Issue  Ollama not running**
**Solution:**
```bash
ollama serve
```
Check status: `http://localhost:11434`

### **Issue  No PDFs processed**
**Solution:**
1. Place PDFs in `Source/` folder
2. Click "Process PDFs" in sidebar
3. Wait for completion (progress bar shown)

### **Issue  ChromaDB error**
**Solution:**
```bash
# Delete and recreate database
Remove-Item -Recurse -Force vectordb
# Then restart app and process PDFs again
```

### **Issue  Streamlit not found**
**Solution:**
```bash
pip install streamlit
# Or reinstall all dependencies
pip install -r requirements.txt
```

### **Issue  Port already in use**
**Solution:**
```bash
# Use different port
streamlit run main.py --server.port 8502
```

### **Issue  LLM generation slow**
**Solution:**
- Expected: 10-60 seconds per generation
- System will fall back to template mode if timeout
- Consider using smaller model: `ollama pull llama2`

---

#  **13. Suggestions & Feedback**

### **Future Enhancements**
- Add support for more question types (True/False, Fill-in-blank)
- Implement semantic grading for open-ended questions
- Add quiz history and performance tracking
- Export quiz results to PDF/CSV
- Add dark mode theme
- Support for batch quiz generation
- Integration with Wireshark for practical exercises

### **Performance Optimizations**
- Cache frequently asked questions
- Implement progressive loading for large documents
- Add GPU acceleration for faster embeddings
- Optimize vector search parameters

### **UI Improvements**
- Better mobile responsiveness
- Drag-and-drop PDF upload
- Real-time search suggestions
- Interactive source highlighting

---

#  **14. Commands Summary**

```bash
# Install dependencies
pip install -r requirements.txt

# Setup Ollama
ollama pull qwen2.5:7b-instruct
ollama serve

# Run application
streamlit run main.py

# Access UI
http://localhost:8501

# Alternative: Run with custom port
streamlit run main.py --server.port 8502

# Check Ollama status
curl http://localhost:11434/api/tags

# Clean database (if needed)
Remove-Item -Recurse -Force vectordb
Remove-Item -Recurse -Force processed_docs
```

---

#  **15. References**

1. **ChromaDB Documentation**  https://docs.trychroma.com/
2. **Ollama Documentation**  https://ollama.ai/
3. **Streamlit Documentation**  https://docs.streamlit.io/
4. **PyMuPDF Documentation**  https://pymupdf.readthedocs.io/
5. **RAG Architecture Patterns**  LangChain Blog
6. **Vector Database Best Practices**  Pinecone Blog
7. **Local LLM Deployment**  HuggingFace Tutorials
8. **Privacy-Preserving AI**  Research Papers on Federated Learning

---

**Built with  for CS5342 Network Security Course**

**Last Updated**: November 21, 2025  
**Version**: 1.0  
**Status**: Production Ready
