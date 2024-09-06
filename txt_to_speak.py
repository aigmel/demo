from gtts import gTTS
import os

# Nolasām tekstu no faila
with open('text.txt', 'r', encoding='utf-8') as text_file:
    text_text = text_file.read()

# Izveidojam TTS objektu latviešu valodai
tts = gTTS(text=text_text, lang='lv')

# Saglabājam uz failu
tts.save("output.mp3")

# Atskaņojam failu
os.system("start output.mp3")  # Windows
