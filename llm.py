
from pathlib import Path
import os

from dotenv import load_dotenv
from google import genai
import chromadb
from sentence_transformers import SentenceTransformer

# API key load karo
env_file = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_file)

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Vector database connect karo
db_client = chromadb.PersistentClient(path="vector_db")
collection = db_client.get_collection(
    name="video_transcripts"
)

# Embedding model load karo
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def ask_video(question):
    # Question ka embedding banao
    question_embedding = embedding_model.encode(
        [question]
    ).tolist()

    # Video se relevant context nikalo
    results = collection.query(
        query_embeddings=question_embedding,
        n_results=1
    )

    context = results["documents"][0][0]

    # Gemini ko context aur question do
    prompt = f"""
    Tum ek AI Video Assistant ho.

    Sirf video context ke aadhar par jawab do.
    Agar jawab context mein nahi hai, to batao
    ki video mein iski jankari nahi mili.

    Video context:
    {context}

    User question:
    {question}
    """

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text
