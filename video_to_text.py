import whisper

# Whisper model load karna
model = whisper.load_model("base")

# Video ko text me convert karna
result = model.transcribe(
    "videos/my_vedio.mp4",
    fp16=False
)

# Transcript ko text file me save karna
with open("transcripts/my_vedio.txt", "w", encoding="utf-8") as file:
    file.write(result["text"])

print("Video successfully text me convert ho gayi!")
print("Transcript save ho gaya: transcripts/my_vedio.txt")