import speech_recognition as sr
import webbrowser
import time
import playsound
import random
import os
from gtts import gTTS
from time import ctime
from datetime import datetime
from datetime import date

r = sr.Recognizer()

def record_audio(ask = False):
  with sr.Microphone() as source:
      if ask:
        speak(ask)
      audio = r.listen(source)
      voice_data=''
      try:
        voice_data = r.recognize_google(audio)
        # print(voice_data)
      except sr.UnknownValueError:
        speak('Sorry, I did not get that')
      except sr.RequestError:
        speak('Sorry, my speech service is down')
      return voice_data

def speak(audio_string):
  tts = gTTS(text=audio_string, lang='en')
  r = random.randint(1,10000000)
  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Athena')

    if 'what\'s your name' in voice_data:
        speak('My name is Athena')

    if 'what time is it' in voice_data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)

    if 'what\'s the time' in voice_data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
    
    if 'what is the date today' in voice_data:
        today = date.today()
        d1 = today.strftime("%B %d %Y")
        speak(d1)
    
    if 'what\'s today\'s date' in voice_data:
        today = date.today()
        d1 = today.strftime("%B %d %Y")
        speak(d1)

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for: ' + search)

    if 'find place' in voice_data:
        location = record_audio('Where do you want to go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of ' + location)
    
    if 'thank you' in voice_data:
        speak('Your welcome')
    
    if 'thanks' in voice_data:
        speak('Your welcome')

    if 'goodbye' in voice_data:
        speak('Goodbye')
        exit()

time.sleep(1)
speak('Hello! How can I help you?')
while 1:
    voice_data=record_audio()
    respond(voice_data)