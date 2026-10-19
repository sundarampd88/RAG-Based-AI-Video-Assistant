# Embeddings ko Vector Database me store karna

import chromadb
from sentence_transformers import SentenceTransformer

# ChromaDB database banana
client = chromadb.PersistentClient(path="vector_db")

# Collection banana
collection = client.get_or_create_collection(
    name="video_transcripts"
)

# Embedding model load karna
model = SentenceTransformer("all-MiniLM-L6-v2")

# Transcript read karna
with open("transcripts/my_vedio.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Transcript ko words me todna
words = text.split()

# 100-100 words ke chunks banana
chunk_size = 100
chunks = []

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

# Chunks ke embeddings banana
embeddings = model.encode(chunks).tolist()

# Vector Database me data store karna
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)

print("Chunks Vector Database me successfully store ho gaye!")
print("Total chunks:", len(chunks))