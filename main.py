import whisper

model = whisper.load_model("base")
result = model.transcribe("reagan_america.wav")
print(result["text"])
