from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio
import cv2
import random
from requests import get, options
import wikipedia
import webbrowser
import smtplib
import pywhatkit as kit
import sys
import requests
import pyautogui
import pyjokes
import time
import PyPDF2
import instaloader
import DateTime
import operator
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, QDateTime ,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




#towish
def wish():
    hour = int(datetime.datetime.now().hour)

    tt=time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good morning maam, its {tt}")
    elif hour>12 and hour<18:
        speak(f"Good afternoon maam, its {tt}")
    else:
        speak(f"Good evening maam, its {tt}")
    speak("I Am you helping partner maam ,please telll me how can I help you")


def sendEmail(to,content):
    #587 is server which anyone can use
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    #email id real and password real
    server.login('eccentricxx54@gmail.com','jarvis5000')
    server.sendmail('eccentricxx54@@gmail.com',to,content)
    server.close()

def news():
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=11cc72644afc475fbf85f1d1ff521e3d'

    main_page = requests.get(main_url).json()
    #print(mainpage)
    articles = main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: , {head[i]}")


def add(a,b):
    "Same as a + b."
    return a+b

def sub(a,b):
    "Same as a - b."
    return a-b

def mul(a,b):
    "Same as a * b."
    return a*b

def mod(a,b):
    "Same as a % b."
    return a % b

def floordiv(a,b):
    "Same as a // b."
    return a//b




def pdf_reader():
    book=open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
   
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
      self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=7,phrase_time_limit=11)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said: {self.query}")

        except Exception as e:
            speak("Maam sorry i was not attentive kindly Say that again please...")
            return "none"
        self.query = self.query.lower()
        return self.query


    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            #logic Building for taska

            if "open notepad" in self.query:
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "temperature" in self.query:
                search = "temperature in ghaziabad"
                url = f"https://www.google.com/search?q=temperature+in+ghaziabad&oq=temperature+in+ghaziabad&aqs=chrome..69i57.8813j0j7&sourceid=chrome&ie=UTF-8={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp} ")

            elif "oh shitt" in self.query:
                speak("what happend maam kindly don't abuse")

            elif 'how are you' in self.query:
                speak("I am fine, Thank you")
                speak("How are you, maam")
 
            elif "fine" in self.query or "good" in self.query:
                speak("It's good to know that your fine")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'open powerpoint presentation' in self.query:
                speak("opening Power Point presentation")
                power = r"C:\\Users\\smrit\\OneDrive\\Desktop\\pchelper\\presentation\\report\\PCHELPf.pptx"
                os.startfile(power)

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("Searching wikipedia...")
                self.query = self.query.replace("wikipedia","")
                results = wikipedia.summary(self.query, sentences=8)
                speak("according to wikipedia")
                speak(results)
                #print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("maam, what should I search on google for you ")
                cm = self.takecommand()
                webbrowser.open(f"{cm}")

            elif "send whatsapp message" in self.query:
                # kit.sendwhatmsg("+918447650706","hello",19,53)
                speak("maam, what number you need to send")
                cp = self.takecommand()
                speak("maam,what is the message")
                co = self.takecommand()
                kit.sendwhatmsg(f"+91{cp}", f"{co}", 19, 56)

            elif "play song on youtube" in self.query:
                speak("which song you want to play")
                tc = self.takecommand()
                kit.playonyt(f"{tc}")

            elif "play interesting song" in self.query:
                webbrowser.open("https://www.youtube.com/watch?v=WZLNJcTuu70")
            
            elif "play romantic song" in self.query :
                webbrowser.open("https://www.youtube.com/watch?v=fD6SzYIRr4c")
            
            elif "play motivational song" in self.query :
                webbrowser.open("https://www.youtube.com/watch?v=u3h1DvwH6yM")

            elif "who made you"  in self.query :
                speak("maam currently i am prototype model and i am made by contribution of two friends Smriti and Pratigya")
        

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shutdown the system " in self.query:
                speak("okay maam bye bye ")
                os.system("shutdown /s /t 5")

            elif "restart the system " in self.query:
                speak("will see you soon again maam ")
                os.system("shutdown /r /t 5")

            elif "sleep the system " in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "email to my friend" in self.query:
                speak("mam,what should I say")
                self.query= self.takecommand()
                if "send a file" in self.query:
                    email='eccentricxx54@gmail.com'
                    password='jarvis5000'
                    send_to_email='eccentricxx54@gmail.com'
                    speak("okay mam,what is the subject for this email")
                    self.query= self.takecommand()
                    subject=self.query
                    speak("and mam, what is the message for this email")
                    self.query2= self.takecommand()
                    message=self.query2
                    speak("mam please enter the correct path of the file into the shell")
                    file_location=input("please enter the path here:")

                    speak("please wait, i am sending the email now")

                    msg= MIMEMultipart()
                    msg['From']=email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message,'plain'))

                    #setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('content-Disposition',"attachment;filename=%s" % filename)

                    #Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    server.sendmail(email,send_to_email,text)
                    server.quit()
                    speak("email has been sent to your friend")

                else:
                    email = 'eccentricxx54@gmail.com'
                    password = 'jarvis5000'
                    send_to_email = 'eccentricxx54@gmail.com'
                    message=self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to your friend")


            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait mam,fetching the latest news")
                news()

            elif "where i am" in self.query :
                speak("wait maam, i am finding the location let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/vl/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    print(geo_data)
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"maam i am not so sure , but i think we are in {city} present in country {country}")
                except Exception as e:
                    speak("Sorry maam ,Due to network issues i am unable to get the location")
                    pass

            elif "take screenshot" in self.query :
                speak("mam, please tell me the name for this screenshot file")
                name= self.takecommand()
                speak("please hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done mam,the screenshot is saved in our main folder,now i am ready for next work")
                
                
            elif "tell me pages in book" in self.query :
                pdf_reader()
                speak("That is a very big book maam do you want to read it now maam")
                tk = self.takecommand()

            elif "no i will read it later " in self.query:
                speak("that is hell a lot of pages to read maam, if you want i can read for you later")

            elif "no not required" in self.query :
                speak("ok as you wish maam i will do as you say")

            elif "alarm" in self.query:
                speak("maam please tell me the time to set alarm for eg set alarm to 5:30 am")
                tt = self.takecommand()
                tt = tt.replace("set alarm to ", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                import MyAlarm

                MyAlarm.alarm(tt)

            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("maam please enter the name correctly")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                time.sleep(5)
                speak("maam would you like to download the profile picture")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader()  # pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done maam,profile picture is saved in main folder")
                else:
                    pass


            elif "do some calculation" in self.query or "calculate" in self.query:

                r=sr.Recogniser()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate,example: 3 plus 3")
                    print("listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognise_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+': operator.add, #plus
                        '-': operator.sub,
                        'x': operator.mul,
                        'divided' : operator.__truediv__,
                    }[op]
                def eval_binary_expr(op1,oper,op2):
                    op1,op2=int(op1),int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))


            elif "no thanks" in self.query:
                speak("thanks for using me mam , Have a good day")
                sys.exit()

            speak("Do you need any more help maam")


startExecution = MainThread()




class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    
        
    def startTask(self):
       self.ui.movie = QtGui.QMovie("D:/wallpap/arrakis-f-dr.gif")  
       self.ui.label.setMovie(self.ui.movie)
       self.ui.movie.start() 
       self.ui.movie = QtGui.QMovie("D:/wallpap/initalize.gif")  
       self.ui.label_2.setMovie(self.ui.movie)
       self.ui.movie.start() 
       self.ui.movie = QtGui.QMovie("D:/wallpap/earth.gif")  
       self.ui.label_4.setMovie(self.ui.movie)
       self.ui.movie.start() 
       self.ui.movie = QtGui.QMovie("D:/wallpap/arrakis-f-dr.gif")  
       self.ui.label.setMovie(self.ui.movie)
       self.ui.movie.start() 
       timer =QTimer(self)
       timer.timeout.connect(self.showTime)
       timer.start(1000)
       startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

   
app =QApplication(sys.argv)
pchelperfy = Main()
jarvisfy.show()
exit(app.exec_())

