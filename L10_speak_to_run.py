import webbrowser

import pyttsx3  #python text to speech extened version 3
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
            pos = pos.lower()
            if "yes" or "search" in pos:
                    ser = input("What you want to listen: ")
                    url = "https://www.youtube.com/results?search_query="
                    url = url + ser
                    webbrowser.open(url)
            else:
                webbrowser.open("youtube.com")
        elif "instagram" in query:
            webbrowser.open("www.instagram.com")