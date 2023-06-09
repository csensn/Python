import pyttsx3
from datetime import *

"""VOICE"""

engine = pyttsx3.init() # object creation
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. o for male, 1 for female


pyttsx3.speak("Hello, Sir")
print(datetime.now().date())
pyttsx3.speak(datetime.now().date())
