from datetime import *

import pyttsx3

engine = pyttsx3.init('sapi5')  # speech api version 5


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.now().hour)
    if 0 <= hour < 12:
        print("Good morning NSN")
        speak("Good morning Sir")
    elif 12 <= hour < 18:
        print("Good afternoon N.S.N")
        speak("Good afternoon Sir")
    else:
        print("Good evening Sir")
        speak("Good evening Sir")
    # speak("I am jarvis Sir, What can run for you... ")


wishme()
speak(datetime.now().strftime("I am jarvis sir and,  the time is %H:%M:%S , Have a nice day sir..."))