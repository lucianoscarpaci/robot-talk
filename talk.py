from gtts import gTTS
import os

text = input("Speak: ")
language = 'en'


file_name = input("Enter the file name: ")
tts = gTTS(text=text, lang=language, tld='com.au')
tts.save(file_name+'.mp3')

os.system("ffmpeg -i " + file_name + ".mp3" +
          " -acodec pcm_s24le -ac 1 -ar 44100 " + file_name + ".wav")
os.system("rm " + file_name + ".mp3")
