import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import pywhatkit
import os

print("Veronica")
MASTER = "Ma'ruf Iskandar"
# suara keluar
engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# suara [0] laki2 [1] perempuan
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# speak


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# menyapa MASTER


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Hello Good Morning " + MASTER)
        speak("Hello, Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        print("Hello Good Afternoon " + MASTER)
        speak("Hello, Good Afternoon" + MASTER)
    else:
        print("Hello Good Evening " + MASTER)
        speak("Hello, Good Evening" + MASTER)

# mic


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="id-ID")
        print(f"You said: {query}\n")

    except Exception as e:
        print("say that again please")
        query = takeCommand()

    return query

# takok


def takok():
    speak("Can I help You")
    query = takeCommand()

# menjalankan perintah
    if "wikipedia" in query.lower():
        speak("searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("time now is " + time)
    elif 'play' in query:
        song = query.replace("play", "")
        speak("playing" + song)
        pywhatkit.playonyt(song)

    elif "open google" in query.lower():
        print("processed...")
        wb.open("google.com")
        speak("opening google..")

    elif "open youtube" in query.lower():
        print("processed...")
        wb.open("youtube.com")
        speak("opening youtube..")

    elif "open facebook" in query.lower():
        print("processed...")
        wb.open("https://www.facebook.com/")
        speak("opening facebook..")

    elif "open my file" in query.lower():
        print("processed...")
        os.startfile("D:\Kuliah")
        speak("opening file..")

    elif "open office" in query.lower():
        print("processed...")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
        speak("opening microsoft word..")

    elif "open power" in query.lower():
        print("processed...")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
        speak("opening microsoft powerpoint..")
    elif "thank" in query:
        speak("you are wellcome ")
        exit()

    return takok()


# start
wishMe()
takok()
