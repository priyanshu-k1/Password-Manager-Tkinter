#LIBS
from tkinter import *
import pickle



#Setting gui:
root=Tk()
root.geometry('800x500')
root.title("PASSWORD MANAGER")
root.resizable(False,False)

#Global Variables





#Side bar
sideBar=Frame(root,bg="grey",width=200,height=500)
sideBar.place(x=0,y=0)

#Side bar Buttons







#main body
mainBody=Frame(root,bg='red',width=600,height=465)
mainBody.place(y=0,x=200)

#Search box

searchBox=Entry(root,width=80,relief='flat',bg='blue')
searchBox.place(x=200,y=465,height=35)

#Main body buttons





#Main function call
root.mainloop()