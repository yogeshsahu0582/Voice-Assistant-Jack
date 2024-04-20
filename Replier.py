import os
#-------Yogesh Sahu (pip install os)---------------
from Speaker import Speak
import random
import webbrowser
#-------Yogesh Sahu ( pip install webbroweser )----
import wikipedia
#----------Yogesh Sahu (pip install wikipedia)-----

def ChatBot(Text):

    if "hi" in Text:
        print("Hello")
        Speak("Hello Yogesh Boss")

    elif "Hello jack what is your age" in Text:
        print("i am a robo not human.")
        Speak("i am a robo not human.")

    elif "good morning" in Text:
        print("good morning")
        Speak("good morning Yogesh Boss")

    elif "good afternoon" in Text:
        print("good afternoon")
        Speak("good afternoon Yogesh Boss")

    elif "good evening" in Text:
        print("good evening")
        Speak("good evening Yogesh Boss")

    elif "good night" in Text:
        print("good night")
        Speak("good night Yogesh Boss")

    elif "how are you" in Text:
        print("I am good")
        Speak("i am fantastic good Yogesh Boss")

    elif "tell me about yourself" in Text:
        print("my name is jack and my author is yogesh sahu.so, yogesh sahu is my Boss")
        Speak("my name is jack and My author is yogesh sahu.So, yogesh sahu is my Boss")

    elif "what is greatest achievment" in Text:
        print("I am a jack assistant ")
        Speak("i am a jack assistant")

    elif "what are your weakness" in Text:
        print("no weakness but come content display")
        Speak("no weakness but come content display")

    elif "sgsits" in Text:
        print("Sgsits is a best Institute.")
        Speak("Shri Govindram Seksaria Institute of technology and Science is a toppest institute in madhya pradesh")

    elif "full form sgsits" in Text:
        print("Shri Govindram Seksaria Institute of technology and Science")
        Speak("Shri Govindram Seksaria Institute of technology and Science")

    elif "Sports" in Text:
        print("cricket, kabaddi, hockey, badminton, chess, football, basketball etc.")
        Speak("cricket, kabaddi, hockey, badminton, chess, football, basketball etc.")

    elif "Festivals" in Text:
        print("Diwali, Holi, rakshabandhan, navratri, ganesha chaturthi etc.")
        Speak("Diwali, Holi, rakshabandhan, navratri, ganesha chaturthi etc.")

    elif "Current Prime Minister" in Text:
        print("Shri Damodar Rao Narendra Modi ji")
        Speak("Shri Damodar Rao Narendra Modi ji")

    elif "Current Chief Minister in Madhya Pradesh" in Text:
        print("Manniya Shri Shivraj Singh Chouhan")
        Speak("Manniya Shri Shivraj Singh Chouhan")

    elif "good afternoon" in Text:
        print("good afternoon")
        Speak("good afternoon Yogesh Boss")

    elif "National Song" in Text:
        print("Vande Matram")
        Speak("Vande Matram")


    elif "national anthem" in Text:
        print("Jana Gana Mana")
        Speak("Jana Gana Mana "
              "Adhinaayak Jaya Hey,"
              " Bhaarat Bhaagya Vidhaataa "
              "Panjaab Sindhu Gujarat Maraatha, "
              "Draavid Utkal Banga "
              "Vindhya Himaachal Yamuna Ganga, "
              "Uchchhal Jaladhi Taranga "
              "Tav Shubh Naamey Jaagey, "
              "Tav Shubh Aashish Maange "
              "Gaahey Tav Jayagaathaa "
              "Jana Gana Mangal Daayak, "
              "Jaya Hey Bhaarat Bhaagya Vidhaataa "
              "Jaya Hey, Jaya Hey, Jaya Hey, "
              "Jaya Jaya Jaya, Jaya Hey")

    elif "national sport" in Text:
        print("hocky")
        Speak("hocky")

    elif "national animal" in Text:
        print("tiger")
        Speak("Tiger")

    elif "national tree" in Text:
        print("Banyan Tree")
        Speak("Banyan Tree")

    elif "programming languages" in Text:
        print("c, c++, java python, javascirpt etc.")
        Speak("c, c++, java python, javascript, ruby, perl etc.")

    elif "how are you" in Text:
        print("I am good")
        Speak("i am fantastic good Yogesh Boss")

    elif "search" in Text:
        Text = Text[7:]
        webbrowser.open("https://www.google.com/search?q="+Text)

    elif "open sgsits" in Text:
        Speak("Ok Yogesh Boss")
        os.startfile("https://www.sgsits.ac.in/")

    elif "open chatgpt" in Text:
        Speak("Ok Yogesh Boss")
        os.startfile("https://chat.openai.com/")


    elif "open gmail" in Text:
        Speak("Ok Yogesh Boss")
        os.startfile("https://mail.google.com/mail")


    elif "open youtube" in Text:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in Text:
        webbrowser.open("https://www.google.com")

    elif "open LinkedIn" in Text:
        webbrowser.open("https://www.linkedin.com")

    elif "open instagram" in Text:
        webbrowser.open("https://www.instagram.com")

    elif "open facebook" in Text:
        webbrowser.open("https://www.facebook.com")

    elif "open github" in Text:
        webbrowser.open("https://www.github.com")

    elif "open weather" in Text:
        webbrowser.open("https://www.weather.com")


    elif "search" in Text:
        Text = Text[7:]
        webbrowser.open("https://www.google.com/search?q="+Text)


    elif "bye" in Text:
        Speak("Bye Yogesh Boss")
        print("Byeee")
        return

    else:
        Speak("Sorry Say It Again")
        print("Dekh kar message daal")