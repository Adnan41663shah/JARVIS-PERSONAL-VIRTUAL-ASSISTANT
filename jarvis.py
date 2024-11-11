import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import comtypes
import pywhatkit  # import pywhatkit for WhatsApp functionality
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I help you today?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """
    it takes microphone input from the user and return string output.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Running...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def set_volume(level):
    """
    Sets the system volume to the specified level (0 to 100).
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(level / 100, None)
    speak(f"Volume set to {level} percent.")

def send_whatsapp_message(name, message):
    """
    Sends a WhatsApp message to the specified contact name.
    """
    try:
        # Get current time and add a minute for message scheduling
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1  # Sends the message in the next minute

        # Use pywhatkit to schedule the message
        speak(f"Sending WhatsApp message to {name}.")
        pywhatkit.sendwhatmsg(f"{name}", message, hour, minute)
        speak("Message scheduled to be sent shortly.")
    except Exception as e:
        print(e)
        speak("I was unable to send the message. Please check the contact name.")
        
if __name__ == '__main__':
    wishme()
    
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query.
        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chat gpt' in query:
            webbrowser.open("chatgpt.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%Y:%m:%d")
            speak(f"The date is {strDate}")

        elif 'open code' in query:
            code_path = "C:\\Users\\adnan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'play music' in query:
            music_dir = 'M:\\music'
            songs = os.listdir(music_dir)
            song = random.choice(songs)
            print(song)
            os.startfile(os.path.join(music_dir, song))

        elif 'play any movie' in query:
            movie_dir = 'M:\\movies_and_webseries'
            movies = os.listdir(movie_dir)
            movie = random.choice(movies)
            print(movie)
            os.startfile(os.path.join(movie_dir, movie))

        elif 'set volume to' in query:
            try:
                level = int(query.split("set volume to ")[-1].replace(" percent", ""))
                if 0 <= level <= 100:
                    set_volume(level)
                else:
                    speak("Please specify a volume level between 0 and 100.")
            except ValueError:
                speak("I couldn't understand the volume level.")
        
        elif 'send whatsapp message to' in query:
            try:
                name = query.split("send whatsapp message to ")[-1]
                speak(f"What message would you like to send to {name}?")
                message = takeCommand()
                if message != "None":
                    send_whatsapp_message(name, message)
            except Exception as e:
                speak("I couldn't understand the contact name or the message.")
