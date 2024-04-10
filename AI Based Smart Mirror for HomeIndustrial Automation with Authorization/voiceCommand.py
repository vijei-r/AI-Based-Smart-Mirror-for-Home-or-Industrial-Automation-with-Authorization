import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import firebase as fg
import webbrowser as wb
import smtplib as mail

heart = pyttsx3.init()
voice = heart.getProperty('voices')
heart.setProperty('voice',voice[1].id)
def speak(audio):
    heart.say(audio)
    heart.runAndWait()
#def mail():
    #mail.
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")

    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
def day():
    weekdays = ("hi", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
    weekday = (datetime.datetime.now().isoweekday())
    weak = weekdays[weekday]
    speak("today is")
    speak(weak)
def wiki():
    audios = command()
    print(audios)
    audios = audios.replace("wikipedia", "")
    result = wikipedia.summary(audios, sentences=2)
    speak(result)
def search():
    speak("what should i search for")
    name = command()
    name = name.lower()
    print(name)
    wb.open_new_tab(name + ".com")
def search1():
    speak("what should i search for")
    name = command()
    name = name.lower()
    print(name)
    wb.open_new_tab(name)

def wish():
    speak("welcome back ")
    hour = (datetime.datetime.now().hour)
    if hour >= 1 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")


def command():
    a = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            a.adjust_for_ambient_noise(source, duration=1)
            print("listening...")
            #speak("listening")
            take = a.listen(source)
            print("recognizing...")
            #speak("recognizing please wait a moment")
            audios = a.recognize_google(take)

    except:
        print("somthing went wrong")
        #speak("say it again")
        return "None"
    return audios.lower()

def main1(audios):

    print(audios)
    if "time" in audios:
        time()

    elif "date" in audios:
        date()
    elif "lights on" in audios:
        fg.ref.update({'float': 1})
        speak("turning lights on")
    elif "lights off" or "lights of" in audios:
        fg.ref.update({'float': 0})
        speak("turning lights off")
    elif "low" in audios:
        fg.ref.update({'int': 0})
        speak("adjusting brightness level to low")
    elif "medium" in audios:
        fg.ref.update({'int': 80})
        speak("adjusting brightness level to medium")
    elif "high" or "i" in audios:
        fg.ref.update({'int': 175})
        speak("adjusting brightness level to high")
voice_data = None
def main():
    wish()
    global c
    # speak("something")
    while True:
        # take input from Voice
        voice_data = command()
        print(voice_data)
        # process voice_data
        if 'corona' in voice_data:
            print("some")
            try:
                # Handle sys.exit()
                main1(voice_data)
            except SystemExit:
                speak("Exit Successfull")
                break
            except:
                # some other exception got raised
                print("EXCEPTION raised while closing.")
                break
        elif c==1:
            speak("going to offline")
            break


# main()