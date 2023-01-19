import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import pywhatkit
import os
import re


print("Siri")
MASTER = "Ma'ruf Iskandar"
# suara keluar
engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# suara [0] laki2 [1] perempuan
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# speak


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Ready.....")
        audio = r.listen(source)
    try:
        print("Processing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"You said: {query}\n")

    except Exception as e:
        speak("say that again please")
        query = takeCommand()

    return query


# menyapa

speak("Hello sir, Can I help you ?")

# takok


def takok():
    query = takeCommand()

# menjalankan perintah
    if "Siri" in query:
        speak("yes sir")
    elif "who are you" in query:
        speak("my name is Siri, I was created by Muhammad Ma'ruf Iskandar")
    elif "who am I" in query:
        wb.open("https://www.kuliahmusik.my.id/p/about.html")
        speak("your name is ma'ruf iskandar, you born in Sidoarjo, 13 January 1999, now you are studying at, UNU Blitar, university. your hobby is playing the piano and want to be a musician")
    elif "kidding" in query:
        speak("ha ha ha ha, I'm sorry sir")
    elif "time" in query:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("time now is " + time)
    elif "open" in query:
        re_eg = re.search("open (.+)", query)
        if re_eg:
            domain = re_eg.group(1)
            url = "https://www." + domain + ".com"
            wb.open(url)
            speak("opening " + domain)
        else:
            wb.open("google.com")
    elif "my website" in query:
        wb.open("https://www.kuliahmusik.my.id/")
    elif "open my file" in query:
        os.startfile("D:\Kuliah")
        speak("Opening file")
    elif 'play' in query:
        song = query.replace("play", "")
        speak("playing" + song)
        pywhatkit.playonyt(song)
    # Close program
    elif "thank" in query:
        speak("you are wellcome sir")
        exit()
    # else:
    #     query = query
    #     speak("Searching")
    #     try:
    #         results = wikipedia.summary(query, sentences=2)
    #         speak("I found !")
    #         speak("From wikipedia - ")
    #         speak(results)
    #     except:
    #         wb.open("google.com")

    return takok()


takok()
