"""
Author: Shivang
Created on: 7/3/20
Purpose: Assistant
"""

import pyttsx3  # for output voice
import datetime  # for time
import speech_recognition as sr  # for input voice
import wikipedia  # for search results
import webbrowser  # for search
import os  # for FileI/O

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # male voice


def speak(audio):
    """Assistant's voice"""
    engine.say(audio)
    engine.runAndWait()  # Runs an event loop until all commands queued up until this method call complete


def wishme():
    """Wish according to time"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good morning! ")
    elif 12 <= hour <= 18:
        speak("Good afternoon! ")

    else:
        speak("Good evening! ")
    speak("I am HIVANG, How may I help you!")


def takecommand():
    """for input of voice"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # waits for 1 second
        audio = r.listen(source)  # input audio
    try:
        print("Recognising ")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        print("Speak again, unable to recognise ")
        return "None"
    return query


# main
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # logic for tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia ")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            webbrowser.open("ganna.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}\n")  # print(songs)
        elif 'code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
            speak("Here you go programmer!")
            os.startfile(codePath)
    
        else:
            speak('Network error, This may take a while... ')
