from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


# 1. Load the data
with open("data/docs.txt", "r") as f:
    text = f.read()

# 2. Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)
chunks = text_splitter.split_text(text)

# 3. Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# 4. Store embeddings in FAISS
vectorstore = FAISS.from_texts(chunks, embeddings)
vectorstore.save_local("faiss_index")

print("✅ Embeddings created successfully")
