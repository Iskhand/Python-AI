import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init("sapi5")
# kecepatan baca
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
# suara [0] laki2 [1] perempuan
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def ngongon():
    mendengar = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        suara = mendengar.listen(source, phrase_time_limit=5)
        try:
            print("Diterima...")
            dengar = mendengar.recognize_google(suara, language='id-ID')
            print(dengar)
        except:
            pass
        return dengar


def gasss():
    servis = ngongon()
    print(servis)
    engine.say()
    engine.runAndWait()


gasss()
