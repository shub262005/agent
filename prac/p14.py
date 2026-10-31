from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# 1. Load the text file
loader = TextLoader("data.txt", encoding="utf-8")
docs_data = loader.load()

# 2. Embeddings
embeddings = OllamaEmbeddings(model="embeddinggemma")

# 3. Create FAISS index from documents (notice from_documents instead of from_texts)
db = FAISS.from_documents(docs_data, embeddings)

# 4. Search
question = input("Enter your question: ")
docs = db.similarity_search(question, k=1)

print("\nAGENT RETRIEVED:")
print(docs[0].page_content)
