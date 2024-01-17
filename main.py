

from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening! rohit sir")
    speak("I am your assistant sir, Plese tell me how can i help you")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Didnt get it! Say that again please ......")
        speak("Didnt get it! Say that again please ......")
        print("Ohh i got it! Are you Busy somewhere ealse? ......")
        speak("Ohh i got it! Are you Busy somewhere ealse? ......")
        return "None"
    return query


# def sendEmail(to, content):


if __name__ == "__main__":
    wishME()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")
        elif 'open porn' in query:
            webbrowser.open("playxporn.com")
        elif 'play music' in query:
            music_dir = 'c:\\songs'
            songs = os.listdir(music_dir)
            print('songs')
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\rohit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        # elif 'email to rohit' in query:
        #     try:
        #         speak("What should i say?")
        #         content = takeCommand()
        #         to = "rohyt99@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir ! Email has not send")
