import psutil 
import pyautogui
import os
import webbrowser as wb
import pyttsx3 # pop install
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is JARVIS ai assistant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is")
    speak(Time)

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:/Code/AI Asistance/ss.png")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)



def wishme():
    speak("Welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning Sir")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    elif hour >=18 and hour<24:
        speak("Good Evening")
    else:
        speak("Good Night Sir")
    speak("Jarvis at your service. Please tell me how can i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("")

        return "None"
    
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('akash.n.yanpure@gmail.com','MtheBest@94')
    server.sendmail('akash.n.yanpure@gmail.com',to,content)
    server.close()

def cpu(): 
    usage = str(psutil.cpu_percent())
    speak("cpu is at "+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    
        # wishme()

        while True:
            query = takeCommand().lower()
            if 'jarvis' in query:
                speak("How can I help you?")
                while True:
                    query = takeCommand().lower()
                    if 'time' in query:
                        time()
                    elif 'date' in query:
                        date()
                    elif 'offline' in query:
                        speak("Going Offline")
                        quit()
                    elif 'wikipedia' in query:
                        speak("Searching...")
                        query = query.replace("wikipedia","")
                        result = wikipedia.summary(query, sentences=2)
                        print(result)
                        speak(result)    
                    elif 'send email' in query:
                        try:
                            speak("what shold i send")
                            content = takeCommand()
                            to = 'akash.n.yanpure@gmail.com'
                            sendemail(to,content)
                            speak('Ok, Email has been sent!')
                        except Exception as e:
                            print(e)
                            speak("Unable to send email!")
                    elif 'chrome' in query:
                        speak("What you want to search")
                        chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'     
                        search = takeCommand().lower()
                        wb.get(chromepath).open_new_tab(search + '.com')
                    elif 'logout' in query:
                        os.system("shutdown -l")
                    elif 'play' in query:
                        dir = 'D:\\Movies'
                        media = os.listdir(dir)
                        print(media)
                        os.startfile(os.path.join(dir,media[0]))
                    elif 'remember that' in query:
                        speak("what should i remember?")
                        data = takeCommand()
                        speak("You said me to remember that"+data)
                        remember = open('data.txt','w')
                        remember.write(data)
                        remember.close()
                    elif 'do you know anything' in query:
                        remember= open('data.txt','r')
                        speak("You said me to remember that"+remember.read())
                    elif 'screenshot' in query:
                        screenshot()
                        speak('done')
                    elif 'cpu' in query:
                        cpu()
                    elif 'joke' in query:
                        jokes()
                    