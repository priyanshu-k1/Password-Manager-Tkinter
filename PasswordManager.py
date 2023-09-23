#LIBS
from tkinter import *
from os import *
from PIL import ImageTk,Image


#global variables
global loginbg



def splashScreen():
    splash=Tk()
    splash.title("P A S S W O R D  M A N A G E R")
    splash.geometry("800x600")
    splash.resizable(False,False)
    image = Image.open("mains/images/loginbg.jpg")
    loginbg= ImageTk.PhotoImage(image)
    bg=Label(splash,image=loginbg)
    bg.pack()
    loginFrame=Frame(splash,bg="white",height=30,width=35)
    loginFrame.place(x=100,y=100)
    
    
    
    splash.mainloop()


#creating main window
def mainWindow():
    root=Tk()
    root.title("P A S S W O R D  M A N A G E R")
    root.resizable(False,False)
    root.geometry("700x500")
    root.mainloop()





#main functions
splashScreen()
