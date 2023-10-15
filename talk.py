from gtts import gTTS
import os

text = "Hello. It's nice to meet you. I'm Daisy, an advanced robotic dog. I've been designed to assist you as your receptionist and companion. Please bear with me for a moment as I initiate all my services. Once I'm up and running, we can connect seamlessly. Please wait."
language = 'en'


file_name = input("Enter the file name: ")
tts = gTTS(text=text, lang=language, tld='com.au')
tts.save(file_name+'.mp3')

os.system("ffmpeg -i " + file_name + ".mp3" +
          " -acodec pcm_s24le -ac 1 -ar 44100 " + file_name + ".wav")
os.system("rm " + file_name + ".mp3")


# SSH into the robot dog
# os.system("sshpass -p 123 scp -r " + file_name +
#          ".wav unitree@192.168.123.13:/home/unitree")
