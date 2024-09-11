from gtts import gTTS
from pydub import AudioSegment
import os

# Nolasām tekstu no faila
with open('text.txt', 'r', encoding='utf-8') as text_file:
    text_text = text_file.read()

# Izveidojam TTS objektu latviešu valodai
tts = gTTS(text=text_text, lang='lv')

# Saglabājam uz mp3 failu
mp3_filename = "output.mp3"
tts.save(mp3_filename)

# Konvertējam mp3 uz wav, izmantojot pydub
mp3_audio = AudioSegment.from_mp3(mp3_filename)
wav_filename = "output.wav"
mp3_audio.export(wav_filename, format="wav")

# Atskaņojam .wav failu
os.system(f"start {wav_filename}")  # Windows

print(f"Teksts veiksmīgi saglabāts kā {wav_filename}")
