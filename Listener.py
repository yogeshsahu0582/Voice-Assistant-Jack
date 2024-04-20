import speech_recognition as sr
#----------Yogesh Sahu ( pip install SpeechRecognition )----
from Replier import *

from tkinter import *
r=sr.Recognizer()

def Listen():

        global Mytext
        MyText = ""
        R = Label(text="Listening.....", width=50, height=2, font=30)

        try:

            a="Listenning............"
            print(a)
            print("------------")

            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)

                MyText = r.recognize_google(audio)
                MyText = MyText.lower()

                b="Did You Say : "
                print(b+MyText)
                ChatBot(MyText)

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")


        R.config(text=MyText)
        R.pack()

