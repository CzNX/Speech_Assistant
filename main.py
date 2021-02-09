import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
from gtts import gTTS
import random


r = sr.Recognizer()

def record_audio(ask=False):
  with sr.Microphone() as source:
    if ask:
      speak(ask)
    audio = r.listen(source)
    voice_data = ''
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      speak('Sorry,I didnot get that')
    except sr.RequestError:
      speak('Sorry,my speech service is down!')   
    return voice_data  


def speak(audio_string):
  tts = gTTS(text=audio_string,lang='en')
  r = random.randint(1,10000000)
  audio_file = 'audio-' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound.playsound(audio_file)
  print(audio_string)
  os.remove(audio_file)

def respond(voice_data):
  if 'what is your name' in voice_data:
    speak('My name is CzN')

  if 'what time is it' in voice_data:
    speak(ctime())

  if 'search' in voice_data:
    search = record_audio('What do you want to search for')  
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    speak('herspeake is what I found')

  if 'find location' in voice_data:
    location = record_audio('What do you want to search for')  
    url = 'https://google.nl/maps/place/' + location + '/&amp'
    webbrowser.get().open(url)
    speak('here is what I found')  

  if 'exit' in voice_data:
    exit()  


time.sleep(1)
speak('How can I help you?')

while 1:
  voice_data = record_audio()
  respond(voice_data)