# RAG System Architecture

## System Overview

```

                     LOCAL RAG: QUIZ & TUTOR SYSTEM                  
                         (Streamlit Web App)                         

```

## High-Level Architecture

```

   User Input     
  (Web Browser)   

         
         

                      STREAMLIT UI LAYER                             

                                     
    Quiz Mode                                Tutor Mode          
                                                                 
   - Topic Input                            - Question           
   - # Questions                              Input              
   - MCQ Form                               - Explanation        
   - Grading                                - Citations          
                                     
                                                                   

                                                    
          
                         

                    CONTEXT RETRIEVAL LAYER                          

                                                                     
        
               get_context(query, threshold)                      
        
                                                                   
                                         
                                                                  
                                    
     LOCAL                   WEB/WIKI                           
     SEARCH                  FALLBACK                           
                                                                
   Score > 0.4?    No       - DuckGo                            
                  - Wikipedia                         
     Yes                                                       
                                    
                                                                  
                                         
                                                                    
                                                  
             Context List                                          
            [{text, source,                                        
              page, score}]                                        
                                                  

                     
                     

                    GENERATION LAYER                                 

                                                                     
                            
     Quiz Gen                         Explanation Gen           
                                                                
                                
      Ollama                           Ollama               
      LLM API                          LLM API              
    qwen2.5:7b                       qwen2.5:7b             
                                
                                                              
      Available?                         Available?             
                                            
     Yes     No                         Yes     No              
                                                            
                                                            
    LLM    Template                    LLM    Raw               
    Quiz   Quiz                        Text   Context           
                            
                                                                
                                                    
                                                                   
                                      
     Parsed Quiz                       Explanation              
      Questions                         + Context               
                                      

                                                 
                                                 

                    PRESENTATION LAYER                               

                            
    Quiz Display                      Explanation View          
                                                                
   - Questions                        - Formatted Text          
   - Radio Options                    - Source Links            
   - Submit Button                    - Page Numbers            
                                      - Expandable              
                        Citations               
      Grading                               
                                                                 
    - Score                                                      
    - Feedback                                                   
    - Citations                                                  
                                                   
                                                 

```

## Data Flow

### 1. PDF Processing Flow
```
Source/*.pdf
    
     PyMuPDF Extract Text
           
            Page-by-page extraction
            Save to processed_docs/*.md
    
     ChromaDB Vectorization
            
             Chunk documents
             Generate embeddings (default)
             Store in vectordb/
```

### 2. Quiz Generation Flow
```
User Topic Input
    
    
Search Local KB (ChromaDB)
    
     Score > 0.4? Yes Use Local Context
                               
     Score < 0.4? Yes Search Web
                                
                                 Try DuckDuckGo
                                 Fallback: Wikipedia
    
    
Context Ready
    
    
Check Ollama Status
    
     Running? Yes Generate with LLM
                           
                            Prompt Engineering
                            API Call (120s timeout)
                            Parse Response
    
     Not Running?  Template Quiz
                           
                            Extract from Context
    
    
Display Quiz (Streamlit Form)
    
    
User Submits Answers
    
    
Grade Answers
    
     Compare with correct answers
     Generate feedback
     Show citations
```

### 3. Tutor Mode Flow
```
User Question Input
    
    
Search Context (same as Quiz)
    
    
Generate Explanation
    
     Ollama Available?
       
        Yes: LLM generates detailed explanation
                
                 Prompt with context
                     Request citations
       
        No: Format raw context nicely
    
    
Display Results
    
     Main explanation text
     Source citations (expandable)
     Content previews
```

## Component Details

### Storage Layer
```

  FILE SYSTEM                                

  Source/                                    
     *.pdf (71 files)                      
                                             
  processed_docs/                            
     *.md (71 markdown files)              
                                             
  vectordb/                                  
     ChromaDB persistent storage           
        1072 document chunks               
          - Embeddings (cosine similarity)   
          - Metadata (source, page)          

```

### Vector Database (ChromaDB)
```

  CHROMADB COLLECTION: knowledge_base        

  Configuration:                             
    - HNSW Index (cosine distance)           
    - Default embeddings                     
    - Persistent storage: ./vectordb         
                                             
  Document Structure:                        
    {                                        
      id: "filename_pN",                     
      text: "page content",                  
      metadata: {                            
        source: "document_name",             
        page: N                              
      }                                      
    }                                        
                                             
  Operations:                                
    - add(): Batch insert (100 docs/batch)   
    - query(): Semantic search (top_k=5)     
    - count(): Get total documents           

```

### LLM Integration (Ollama)
```

  OLLAMA LOCAL LLM                           

  Endpoint: http://localhost:11434          
  Model: qwen2.5:7b-instruct                 
                                             
  API Calls:                                 
    GET  /api/tags      - Check status       
    POST /api/generate  - Generate text      
                                             
  Parameters:                                
    - temperature: 0.7                       
    - num_predict: 2000 tokens               
    - timeout: 120 seconds                   
                                             
  Health Check:                              
    - 5 second timeout                       
    - Fallback: Template generation          

```

### Web Search Fallback
```

  MULTI-SOURCE WEB SEARCH                    

  Priority Order:                            
                                             
  1. DuckDuckGo Search                       
     - Max results: 5                        
     - Timeout: default                      
     - Score: 0.8                            
                                             
  2. Wikipedia (Fallback)                    
     - Language: English                     
     - Max articles: 3                       
     - Content: First 2000 chars             
     - Score: 0.9                            
                                             
  Trigger: Local score < 0.4 threshold       

```

## Technology Stack

```

  LAYER                TECHNOLOGY                        

  Frontend UI          Streamlit 1.28+                   
  Vector Database      ChromaDB 0.4+                     
  PDF Processing       PyMuPDF (fitz) 1.23+              
  LLM Engine           Ollama (qwen2.5:7b-instruct)      
  Web Search 1         DuckDuckGo Search 4.0+            
  Web Search 2         Wikipedia API 1.4+                
  HTTP Client          Requests                          
  Language             Python 3.12                       
  Embeddings           ChromaDB Default (all-MiniLM)     

```

## Key Features

### 1. Robust Search Strategy
- **Primary**: Local vector search with relevance threshold (0.4)
- **Secondary**: DuckDuckGo web search
- **Tertiary**: Wikipedia fallback
- **Result**: Never fails to find information

### 2. Dual Generation Modes
- **LLM Mode**: Uses local Ollama for intelligent generation
- **Template Mode**: Extracts content directly when LLM unavailable
- **Graceful Degradation**: Automatic fallback without user intervention

### 3. Citation Accuracy
- Source document name preserved
- Page number tracked through entire pipeline
- Citations included in:
  - Quiz explanations
  - Tutor responses
  - Grading feedback

### 4. Session Management
- Streamlit session state for persistence
- Form-based quiz (prevents rerun issues)
- Stateful context storage
- Clean state reset on new queries

## Performance Characteristics

```

  OPERATION             APPROXIMATE TIME                 

  PDF Processing        ~30-60s for 71 PDFs              
  Vector Search         < 1s (ChromaDB HNSW)             
  LLM Generation        10-60s (depends on question)     
  Web Search            2-5s (DuckDuckGo)                
  Wikipedia Search      1-3s (direct API)                
  Quiz Display          Instant (cached in session)      

```

## Security & Privacy

- **100% Local Processing**: All PDFs stay on local machine
- **No External APIs**: LLM runs locally via Ollama
- **Selective Web Search**: Only when local content insufficient
- **No Data Logging**: Streamlit runs in local mode
- **No Authentication**: Single-user local deployment

## Scalability Considerations

### Current Capacity
- **Documents**: 71 PDFs (1072 chunks)
- **Vector DB Size**: ~50-100 MB
- **RAM Usage**: ~500 MB (Streamlit + ChromaDB)
- **LLM RAM**: ~4-6 GB (Qwen 2.5 7B)

### Scaling Options
1. Increase chunk size for larger documents
2. Batch processing for more PDFs
3. Add more powerful LLM models
4. Implement caching for frequent queries
5. Add document categorization

## Error Handling

```

  FAILURE POINT          FALLBACK STRATEGY  

  Ollama Down            Template Mode      
  DuckDuckGo Fails       Wikipedia Search   
  Wikipedia Fails        Show Error + Tips  
  Local Search Empty     Try Web Search     
  LLM Timeout            Fallback Template  
  Parse Failure          Use Raw Context    
  No PDFs Found          Show Setup Guide   

```

## Deployment

### Requirements
- Python 3.12+
- 8 GB RAM minimum (16 GB recommended)
- Ollama installed and running
- Internet connection (for web fallback)

### Installation
```bash
pip install -r requirements.txt
ollama pull qwen2.5:7b-instruct
```

### Running
```bash
streamlit run main.py
```

### Access
- Local: http://localhost:8501
- Network: http://[IP]:8501

---

**Architecture Version**: 1.0  
**Last Updated**: November 21, 2025  
**System Status**: Production Ready
