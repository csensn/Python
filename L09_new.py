import webbrowser
from datetime import *

import pyttsx3  #python text to speech extened version 3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')      #speech api version 5
voices = engine.getProperty('voices')
print(voices[0].id)
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("What voice you like male / female ")
print("1. male and 2. female")

choice = int(input("Enter your choice : "))
if choice == 1:
    engine.setProperty('voice', voices[0].id)
else:
    engine.setProperty('voice', voices[1].id)
speak("Hello Sir, what can I do for you.")

print(datetime.now())
speak(datetime.now())

def wishme():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning NSN")
        print("Good morning NSN")
    elif hour>=12 and hour < 18:
        speak("Good afternoon N S N")
        print("Good afternoon N.S.N")
    else:
        speak("Good evening")
        print("Good evening")
    speak("I am jarvis Sir, What can run for you... " )
wishme()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said : {query}\n")
    return query

if __name__ == '__main__':
    while True:
        query = takecommand()
        query = query.lower()
        print(f"You said : {query}")
        speak(f"You said : {query}")
        if'wikipedia' in query:
            print("Your search wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'youtube' in query:
            print("Youtube is opening sir...")
            speak("You want to search somthing on youtube : Yes or No")
            pos = takecommand()
            if "yes" in pos.lower():
                if "search" in query:
                    ser = input("What you want to listen: ")
                    url = "https://www.youtube.com/results?search_query="
                    url = url + ser
                    webbrowser.open(url)
            else:
                webbrowser.open("youtube.com")
        elif "instagram" in query:
            webbrowser.open("www.instagram.com")
