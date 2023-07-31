import os
import subprocess
import webbrowser
from datetime import *
import pyttsx3  # python text to speech extend version 3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print(audio)
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        # print(f"user said : {query}\n")
    return query


if __name__ == '__main__':
    while True:
        query = takecommand()
        query = query.lower()
        print(f"You said : {query}")
        speak(f"You said : {query}")
        if 'wikipedia' in query:
            print("Your search wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'youtube' in query:
            print("Youtube is opening sir...")
            speak("You want to search somthing on youtube : Yes or No")
            pos = takecommand()
            pos = pos.lower()
            if "yes" or "search" in pos:
                ser = input("What you want to listen: ")
                url = "https://www.youtube.com/results?search_query="
                url = url + ser
                webbrowser.open(url)
            else:
                webbrowser.open("youtube.com")
        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")
        elif 'play music' in query:
            music_dir = 'D:\\Songs\\Shubh'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'word' in query:
            print("MS Word is opening......")
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        elif 'exel' in query:
            print("MS Exel is opening......")
            speak("MS Exel is opening sir......")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
        elif 'open chrome' in query:
            print("Google Chrome is opening......")
            speak("Google Chrome is opening sir......")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome")
        elif 'open edge' in query:
            print("MS Edge is opening......")
            speak("MS Edge is opening sir......")
            os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge")
        elif 'time' in query:
            print(datetime.now().strftime("%H:%M:%S , Have a nice day sir..."))
            speak(datetime.now().strftime("%H:%M:%S , Have a nice day sir..."))
        elif 'shutdown system' in query:
            speak("Are you sure sir to shutdown the system...")
            res = takecommand()
            if res == 'yes':
                speak("Okay, System is shutdown")
                os.system("shutdown /s /t 1")
        elif 'exit' in query:
            break
