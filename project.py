from tkinter import *
from currency_converter import CurrencyConverter as p
from PIL import Image, ImageTk
import pyttsx3
import datetime
import speech_recognition as sr

import webbrowser
import os
import random



import wikipedia

import wolframalpha


#import time

import requests

import pywhatkit
import pyjokes




from PIL import Image

#pytesseract.pytesseract.tesseract_cmd = r"C:\Users\mridu\AppData\Local\Tesseract-OCR\tesseract.exe"
client = wolframalpha.Client('5H74PP-Y8T4YLUK9H')

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
a = {'Tribhuvan':'chawlatribhuvan@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir!") #Name - your Name
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir")
        window.update()
        speak("Good Evening Sir!")
    speak("I am Jarvis  sir  please tell me how may I help you?") #BotName - Give a name to your assistant

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 120
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query

def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishme()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg = '#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')


        elif 'doubt' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="5H74PP-Y8T4YLUK9H"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "convert dollar to rupee" in query:
            r = p.convert(1,"USD","INR")
            print(r)
            speak(r)


        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
			
        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

  

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" %strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" %strdate)
            window.update()
            speak("Sir today's date is %s" %strdate) 

        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")

        

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")

        

        

       
        
        if "youtube" in query:
            song = query.replace("youtube","")

            speak("playing"+song)
            pywhatkit.playonyt(song)

        elif "share" in query:
            text = query.replace("whatsapp","")
            speak("Sending"+text)
            pywhatkit.sendwhatmsg(f"+91{7340737262}","Hello World",18,55)

        # elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        #     speak("I was built by Sir Tribhuvan Chawla")
        #     print("I was built by Sir Tribhuvan Chawla")

        elif "weather" in query:
            api_key="bf818c7d471f4500226a49822097b9c8"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Jarvis')
            window.update()
            speak('Hello Everyone! My self Jarvis')

        

        elif 'open meet' in query:
            speak('okay')
            webbrowser.open('https://meet.google.com//landing?authuser=1//')

        # elif "notepad" in query:
        #     npath = "C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
        #     os.startfile(npath)

        # elif "spotify" in query:
        #     qpath = "C:\\Users\\DELL\\AppData\\Roaming\\Spotify\\Spotify.exe"
        #     os.startfile(qpath)

        # elif "document" in query:
        #     dpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
        #     os.startfile(dpath)

        # elif "spreadsheet" in query:
        #     spath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
        #     os.startfile(spath)

        # elif "presentation" in query:
        #     ppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
        #     os.startfile(ppath)

        # elif "settings" in query:
        #     gpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Settings"
        #     os.startfile(gpath)

        # elif "chrome" in query:
        #     cpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
        #     os.startfile(cpath)

        # elif "code" in query:
        #     vpath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
        #     os.startfile(vpath)

        # elif "message" in query:
        #     mpath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp"
        #     os.startfile(mpath)

        elif "crack a joke" in query:
            joke = pyjokes.get_joke()
            
            speak(joke)
  

        

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Jarvis version 5 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')
        

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
		
        

        
       

        

                

def update(ind):
    frame = frames[(ind)%20]
    ind += 1
    label.configure(image=frame)
    window.after(20, update, ind)

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
var1.set('Jarvis Said:')
label2.pack()

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='a.gif',format = 'gif -index %i' %(i)) for i in range(20)]
window.title('JARVIS')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text = 'WISH ME',width = 20, command = wishme, bg = '#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text = 'PLAY',width = 20,command = play, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text = 'EXIT',width = 20, command = window.destroy, bg = '#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()