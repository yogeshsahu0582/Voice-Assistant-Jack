#----------------------Yogesh Sahu---------------------
import  tkinter as tk
from tkinter import *
from Replier import *
from Speaker import *
from Listener import *
from PIL import Image, ImageTk
#------Yogesh Sahu (pip install PIL or Pillow-PIL)

def GetText():

    Text = E.get("1.0", 'end-1c')
    Text=Text.lower()
    ChatBot(Text)
#--------------------------------------------------------
root = Tk()

root.geometry("750x600")
root.title("Jack")

root.configure(bg='aqua')

image = Image.open("download.jpeg")
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)
background_label.place(x=20, y=60, relwidth=1, relheight=1)


Head = Label(text ="Hi This is Jack")
Head.pack()

E = Text(width = 50, height=2, font=30)
E.pack()

label = tk.Label(root, text=" ",
                 wraplength=150)
label.pack()

Enter = Button(text = "Chat",pady=5, padx=5, command=GetText)
Enter.pack()

label = tk.Label(root, text=" ",
                 wraplength=150)
label.pack()

ListenBtn = Button(text = "Listen..",pady=5, padx=5, command=Listen)
ListenBtn.pack()

root.mainloop()