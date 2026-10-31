from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings

loader = TextLoader("data.txt", "utf-8")
data_docs = loader.load()

embeddings = OllamaEmbeddings(model="embeddinggemma")

db = FAISS.from_documents(data_docs, embeddings)
question = input("ENter your question : ")
result = db.similarity_search(question, k=1)
print("\nResult")
print(result[0].page_content)
