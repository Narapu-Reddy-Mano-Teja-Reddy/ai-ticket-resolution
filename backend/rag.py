from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
import json

class KnowledgeBaseEngine:
    def __init__(self):
        # Lazy load these to avoid startup hanging if Ollama is asleep
        self._llm = None
        self._embeddings = None
        self.retriever = None
        self.initialized = False
        self.index_path = os.path.join("data", "faiss_index")

    @property
    def llm(self):
        if not self._llm:
            self._llm = ChatOllama(
                model="llama3.2:1b",
                # Optimize for speed: faster generation, lower context memory
                num_predict=100,  # Reduced from 150
                num_ctx=1024,     # Reduced from 2048
                temperature=0.1   # Reduced for deterministic/faster output
            )
        return self._llm

    @property
    def embeddings(self):
        if not self._embeddings:
            self._embeddings = OllamaEmbeddings(model="llama3.2:1b")
        return self._embeddings

    def ensure_kb_initialized(self):
        if self.initialized: return
        print("Initializing Knowledge Base...")
        
        # Load from JSON file
        kb_path = os.path.join("data", "knowledge_base.json")
        self.docs = []
        
        try:
            if os.path.exists(kb_path):
                with open(kb_path, "r") as f:
                    data = json.load(f)
                    self.docs = [{"topic": item['topic'], "content": item['content']} for item in data]
            else:
                print(f"Warning: {kb_path} not found. Using fallback data.")
                self.docs = [
                    {"topic": "Password Reset", "content": "Go to Settings > Security > Reset Password."},
                    {"topic": "System Slow", "content": "Clear cache/cookies and restart."},
                    {"topic": "VPN Issues", "content": "Restart Cisco AnyConnect."},
                    {"topic": "Software Request", "content": "Submit IT ticket."},
                    {"topic": "Wifi", "content": "Connect to CorpNet-Secure."}
                ]

            # Try to load existing vector store or create new one
            try:
                if os.path.exists(self.index_path):
                    print("Loading cached vector store...")
                    vectorstore = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
                    self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
                else:
                    print("Creating new vector store (this may take a moment)...")
                    texts = [f"{d['topic']}: {d['content']}" for d in self.docs]
                    vectorstore = FAISS.from_texts(texts, self.embeddings)
                    vectorstore.save_local(self.index_path)
                    self.retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
            except Exception as e:
                print(f"Vector store init failed, using fallback search: {e}")
                self.retriever = None
            
            self.initialized = True
            print(f"KB Initialized with {len(self.docs)} articles.")
        except Exception as e:
            print(f"KB Init Failed: {e}")

    def categorize_ticket(self, text):
        self.ensure_kb_initialized()
        try:
            if self.retriever:
                # FAST: Use Vector Search for categorization instead of LLM
                docs = self.retriever.invoke(text)
                if docs:
                    top_match = docs[0].page_content
                    category = top_match.split(":")[0] if ":" in top_match else "General Support"
                    return category
            else:
                # Fallback: keyword match
                query_lower = text.lower()
                for doc in self.docs:
                    if any(word in doc['topic'].lower() for word in query_lower.split()):
                        return doc['topic']
            return "General Support"
        except Exception as e:
            return "General Support"

    def recommend_articles(self, text):
        self.ensure_kb_initialized()
        try:
            if self.retriever:
                return [d.page_content for d in self.retriever.invoke(text)] if self.retriever else []
            else:
                # Fallback: simple keyword matching
                query_lower = text.lower()
                matches = []
                for doc in self.docs:
                    if any(word in doc['topic'].lower() or word in doc['content'].lower() for word in query_lower.split()):
                        matches.append(f"{doc['topic']}: {doc['content']}")
                return matches[:3]  # top 3
        except: return []

    def generate_solution(self, text):
        self.ensure_kb_initialized()
        try:
            title_docs = self.recommend_articles(text)
            if not title_docs: return "I couldn't find any specific articles for this issue."
            
            # Use only the top 1 document for the solution
            best_doc = title_docs[0]
            
            if self._llm:
                return (ChatPromptTemplate.from_template(
                    "Answer briefly based on:\n{c}\n"
                    "Question: {t}"
                ) | self.llm | StrOutputParser()).invoke({"t": text, "c": best_doc})
            else:
                # Fallback: return the content directly
                return best_doc
        except Exception as e:
            return f"Error generating solution: {e}"

    def analyze_full_ticket(self, text):
        """
        Performs retrieval ONCE and generates category, recommendations, and solution.
        Returns: (category, recommendations_list, solution_text)
        """
        self.ensure_kb_initialized()
        try:
            # 1. Retrieval (Done ONCE)
            docs = []
            if self.retriever:
                docs = self.retriever.invoke(text)
            
            # Fallback if no docs or no retriever
            if not docs:
                # Use keyword fallback logic from recommend_articles
                query_lower = text.lower()
                matches = []
                for d in self.docs:
                    if any(word in d['topic'].lower() or word in d['content'].lower() for word in query_lower.split()):
                        matches.append(f"{d['topic']}: {d['content']}")
                recs = matches[:3]
                best_doc = recs[0] if recs else None
            else:
                recs = [d.page_content for d in docs]
                best_doc = recs[0] if recs else None

            # 2. Categorization
            category = "General Support"
            if best_doc:
                category = best_doc.split(":")[0] if ":" in best_doc else "General Support"
            elif not self.retriever: # If fallback was used
                 for d in self.docs:
                    if any(word in d['topic'].lower() for word in text.lower().split()):
                        category = d['topic']
                        break

            # 3. Solution Generation
            solution = "I couldn't find any specific articles for this issue."
            if best_doc:
                if self._llm:
                    solution = (ChatPromptTemplate.from_template(
                        "Answer based on:\n{c}\nQ: {t}"
                    ) | self.llm | StrOutputParser()).invoke({"t": text, "c": best_doc})
                else:
                    solution = best_doc

            return category, recs, solution

        except Exception as e:
            return "Error", [], f"Analysis failed: {e}"

    def detect_gaps(self, queries):
        topics = ["password", "billing", "vpn", "software", "meeting", "slack"]
        return list({q for q in queries if not any(t in q.lower() for t in topics)})

kb_engine = KnowledgeBaseEngine()
