from gtts import gTTS
import os

text = "Hello, its nice to meet you! My name is Daisy. I am a robot. I am here to help you."
language = 'en'

tts = gTTS(text=text, lang=language, tld='com.au')
tts.save('hello_daisy.mp3')

os.system("ffmpeg -i hello_daisy.mp3 -acodec pcm_s24le -ac 1 -ar 44100 daisy_signed.wav")