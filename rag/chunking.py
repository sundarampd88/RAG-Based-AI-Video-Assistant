# Transcript ko read karke 100-100 words ke chunks me divide karna

# Transcript file read karna
with open("transcripts/my_vedio.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Text ko words me todna
words = text.split()

# Har chunk me 100 words
chunk_size = 100

chunks = []

for i in range(0, len(words), chunk_size):
    chunk = " ".join(words[i:i + chunk_size])
    chunks.append(chunk)

# Chunks check karna
for number, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {number} ---")
    print(chunk)