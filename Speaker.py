import  os
import pyttsx3
#----------------Yogesh Sahu (pip install pyttsx3)-------
engine = pyttsx3.init()
# ---------------Text To Speech------------------------
def Speak(T):
    engine.say(T)
    engine.runAndWait()