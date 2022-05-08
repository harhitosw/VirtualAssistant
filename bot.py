from socket import timeout
from tokenize import Special
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes 
import os
import sys
import subprocess
import time
from urllib.request import urlopen
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
def speakfunction(audio):
    engine.say(audio)
    engine.runAndWait()
def greetfuntion():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12): 
        speakfunction('Good Morning')
    elif(hour>=12 and hour<=18):
        speakfunction('Good afternoon')
    else:
        speakfunction('Good evening')
    speakfunction('how may I help you Sir')
def takevoice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('hearing......')
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        print('recongnizing.......')
        query=r.recognize_google(audio)
        print(f"User said:{query}")
    except Exception as e:
        print('Say that Again please')
        return "None"
    return query
if __name__=='__main__':
    greetfuntion()
while(True):
    query=takevoice().lower()
    if 'wikipedia' in query:
        speakfunction('Searching Wikipedia')
        results=wikipedia.summary(query,sentences=2)
        speakfunction('According to wikipedia')
        speakfunction(results)
    if 'open youtube' in query:
        webbrowser.open('youtube.com')
    if 'joke' in query:
        My_joke = pyjokes.get_joke(language="en", category="all")
        speakfunction(My_joke)
        print(My_joke)
    if 'music' in query:
        music_dir='C:\\Users\\Harsh30\\Desktop\\Songs'
        songs=os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[1]))
        sys.exit()
    if 'time' in query:
        timenow=datetime.datetime.now().strftime("%H:%M:%S")
        speakfunction (f"The Time is{timenow}")
    if 'note' in query:
            speakfunction("What should i write, sir")
            note=None
            while note==None:
                speakfunction('Please  Say  that again  sir  did  not  get  you')
                note=takevoice()
            file = open('jarvis.txt', 'w')
            speakfunction("Sir, Should i include date and time")
            snfm = takevoice()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
    if "show note" in query:
            speakfunction("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speakfunction(file.read(6))   
    if "exit" in query :
            speakfunction("Thank You Sir") 
            speakfunction("GoodBye")    
            sys.exit()
    if "sleep" in query:
        speakfunction("Going to Sleep sir  please  see  that all applications  are   closed ")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
    


 