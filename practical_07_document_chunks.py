from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the document
loader = TextLoader("data.txt", encoding="utf-8")
doc = loader.load()

print("Document loaded successfully.")
print("Number of documents:", len(doc))

# Create text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

# Split the document into chunks
chunks = splitter.split_documents(doc)

# Display results
print("\nNumber of chunks:", len(chunks))

if chunks:
    print("\nFirst Chunk:")
    print(chunks[0].page_content)