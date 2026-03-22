## pip install sounddevice openai-whisper

import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os

# Configuration
FS = 16000
SECONDS = 2
FILENAME = "query.wav"

# Load Whisper Model (Local)
print("Loading Whisper model...")
model = whisper.load_model("base")

def record_query():
    """Captures audio from the microphone."""
    print(f"\nListening for {SECONDS} seconds... Speak now!")
    audio = sd.rec(int(SECONDS * FS), samplerate=FS, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    write(FILENAME, FS, (audio * 32767).astype(np.int16)) # Save as 16-bit WAV
    return FILENAME

def voice_to_rag():
    # 1. Capture Voice
    audio_path = record_query()
    
    # 2. Convert Voice to Text
    print("Transcribing...")
    result = model.transcribe(audio_path,fp16=False)
    user_query = result["text"].strip()
    print(f"User Query: {user_query}")
    
    if not user_query:
        print("No speech detected.")
        return

    # 3. Pass to your RAG system
    # Replace this with your actual RAG logic
    # response = query_rag_system(user_query) 
    print(f"Passing '{user_query}' to the LLM...")
    
    # Cleanup
    os.remove(audio_path)

# Run the pipeline
if __name__ == "__main__":
    voice_to_rag()