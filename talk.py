from gtts import gTTS

text = "Hello, its nice to meet you! My name is Daisy. I am a robot. I am here to help you."
language = 'en'

tts = gTTS(text=text, lang=language, tld='com.au')
tts.save('hello_daisy.wav')