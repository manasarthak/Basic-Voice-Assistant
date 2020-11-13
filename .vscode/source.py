import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#to take the command from user 
def command():
    r=sr.Recognizer()#creating an instance of the recognizer class
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en')
            print(query)
        except Exception as e:
            print(e)
            print("failed to understand.Can you say that gain sir")
            return "None"
        return query
    
#text to speech method 
def speech(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def date_and_time(day,date,time):
    now=datetime.datetime.now()
    if date == 1:
         print("Today is{}".format(now.strftime("%d")))
    if day == 1 :
         print("Today is{}".format(now.strftime("%A")))
    if time == 1:
         print("It is{}".format(now.strftime("%I:%M %p")))

def hello():
    speech("hello sir How may i help you")

def search_web(query):
    query=query.replace('search','')
    driver = webdriver.Chrome(executable_path=r'C:/Users/Sarthak/Documents/chromedriver.exe')
    driver.implicitly_wait(1)
    driver.maximize_window()
    driver.get('http://www.google.com/search?q='+query)

def query():
    hello()
    while(True):
        query=command().lower()
        if "tell me your name" in query:
            speak("I am Friday.Your desktop assistant.")
        elif "wikipedia" in query:
            query=query.replace("wikipedia","")
            result="according to wikipedia"+wikipedia.summary(query,sentences=4)
            speech(result)
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "time" in query:
            date_and_time(0,0,1)
        elif "date" in query:
            date_and_time(0,1,0)
        elif "day" in query:
            date_and_time(1,0,0)
        elif "bye" in query:
            speech("closing assistant")
            exit()
        elif "search" in query:
            search_web(query)
while(1):
    query()