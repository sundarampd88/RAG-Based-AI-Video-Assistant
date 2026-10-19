# Text ko numerical vectors (embeddings) me convert karna

from sentence_transformers import SentenceTransformer

# Embedding model load karna
model = SentenceTransformer("all-MiniLM-L6-v2")

# Transcript ke chunks read karna
with open("transcripts/my_vedio.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Text ko words me todna
words = text.split()

# 100-100 words ke chunks banana
chunk_size = 100
chunks = []

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

# Chunks ko embeddings/vectors me convert karna
embeddings = model.encode(chunks)

# Result check karna
print("Total chunks:", len(chunks))
print("Embedding ka type:", type(embeddings))
print("Vector ka size:", embeddings.shape)

print("\nFirst chunk ka vector:")
print(embeddings[0])
