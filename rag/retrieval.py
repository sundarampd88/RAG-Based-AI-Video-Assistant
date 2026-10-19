
import chromadb
from sentence_transformers import SentenceTransformer

# Vector Database se connect karna
client = chromadb.PersistentClient(path="vector_db")

# Transcript collection open karna
collection = client.get_collection(
    name="video_transcripts"
)

# Embedding model load karna
model = SentenceTransformer("all-MiniLM-L6-v2")

# User ka question
question = "Maine apne baare me video me kya bataya?"

# Question ko vector me convert karna
question_embedding = model.encode([question]).tolist()

# Relevant transcript search karna
results = collection.query(
    query_embeddings=question_embedding,
    n_results=1
)

# Relevant chunk print karna
print("\nVideo se relevant information:")
print(results["documents"][0][0])
