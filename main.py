import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
from gtts import gTTS
from playsound import playsound

root = Tk()
root.title("Text to Speech converter")
root.geometry("1000x580+200+80")
root.resizable(False,False)
root.configure(bg="#F7AC40")
#root.mainloop()

logo_image = PhotoImage(file = "C:/Users/download.png" )
root.iconphoto(False, logo_image)
#root.mainloop()

upper_frame = Frame(root, bg="#14A7DD" , width=1200, height=130)
upper_frame.place(x=0,y=0)
picture = PhotoImage(file = "C:/Users/download.png")
Label(upper_frame, image= picture , bg="#14A7DD").place(x=100, y=20)
#root.mainloop()

Label(upper_frame,text="Text to Speech convertor", font="TimesNewroman 40 bold",bg="#14A7DD",fg='white').place(x=250,y=35)
#root.mainloop()

text_box= Text(root, font="calibri 20",bg="white",relief= GROOVE,wrap=WORD,bd=0)
text_box.place(x=30,y=150,width=940,height=180)
#root.mainloop()

gender_box = Combobox(root, values=['Male','Female'],font = "Roboto 12" , state='r' , width=12)
gender_box.place(x=340,y=400)
gender_box.set('Male')
#root.mainloop()

speed_box = Combobox(root, values=['Fast','Medium','Slow'],font = "Roboto 12" , state='r' , width=12)
speed_box.place(x=540,y=400)
speed_box.set('Medium')
#root.mainloop()

Label(root, text="Select Voice", font="TimesNewRoman 15 bold" , bg="#F7AC40", fg="White").place(x=340,y=370)
Label(root, text="Select Speed", font="TimesNewRoman 15 bold" , bg="#F7AC40", fg="White").place(x=540,y=370)
#root.mainloop()

tts=pyttsx3.init()
def speaknow():
    text = text_box.get(1.0, END)
    gender =gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            tts.setProperty('voice',voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else :
            tts.setProperty('voice',voices[1].id)
            tts.say(text)
            tts.runAndWait()
    if(text):
        if(speed=='Fast'):
            tts.setProperty('rate',250)
            setvoice()
        elif(speed=='Medium'):
            tts.setProperty('rate',150)
            setvoice()
        else:
            tts.setProperty('rate',60)
            setvoice()


play_button=PhotoImage(file = "C:/Users/play1.png" )
play_btn =  Button(root, text="Play" , compound= LEFT , image=play_button, bg='White',width=130,font="arial 14 bold" ,borderwidth= '0.1c',command=speaknow)
play_btn.place(x=450,y=450)
root.mainloop()