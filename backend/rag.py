from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

class KnowledgeBaseEngine:
    def __init__(self):
        # Lazy load these to avoid startup hanging if Ollama is asleep
        self._llm = None
        self._embeddings = None
        self.retriever = None
        self.initialized = False

    @property
    def llm(self):
        if not self._llm:
            from langchain_ollama import ChatOllama
            self._llm = ChatOllama(
                model="llama3.2:1b",
                # Optimize for speed: faster generation, lower context memory
                num_predict=150, 
                num_ctx=2048,
                temperature=0.3
            )
        return self._llm

    @property
    def embeddings(self):
        if not self._embeddings:
            from langchain_ollama import OllamaEmbeddings
            self._embeddings = OllamaEmbeddings(model="llama3.2:1b")
        return self._embeddings

    def ensure_kb_initialized(self):
        if self.initialized: return
        print("Initializing Knowledge Base...")
        
        # Load from JSON file
        import json, os
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

            # Try to initialize vector store
            try:
                texts = [f"{d['topic']}: {d['content']}" for d in self.docs]
                self.retriever = FAISS.from_texts(texts, self.embeddings).as_retriever(search_kwargs={"k": 3})
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
                    "Short, direct answer for user based on this info:\n{c}\n"
                    "Question: {t}"
                ) | self.llm | StrOutputParser()).invoke({"t": text, "c": best_doc})
            else:
                # Fallback: return the content directly
                return best_doc
        except Exception as e:
            return f"Error generating solution: {e}"

    def detect_gaps(self, queries):
        topics = ["password", "billing", "vpn", "software", "meeting", "slack"]
        return list({q for q in queries if not any(t in q.lower() for t in topics)})

kb_engine = KnowledgeBaseEngine()
