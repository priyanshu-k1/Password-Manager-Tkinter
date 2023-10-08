#LIBS
from tkinter import *
from os import *
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

ShowButton = Button(sideBar,text="Sign up",bg='light green',width=27,relief='flat')
ShowButton.place(x=0,y=140,height=50)

addButton = Button(sideBar,text="Sign up",bg='light green',width=27,relief='flat')
addButton.place(x=0,y=240,height=50)

editButton = Button(sideBar,text="Sign up",bg='light green',width=27,relief='flat')
editButton.place(x=0,y=340,height=50)

delButton = Button(sideBar,text="Sign up",bg='light green',width=27,relief='flat')
delButton.place(x=0,y=440,height=50)

loginButton = Button(sideBar,text="Sign up",bg='light green',width=27,relief='flat')
loginButton.place(x=0,y=440,height=50)
#main body
mainBody=Frame(root,bg='red',width=600,height=500)
mainBody.place(y=0,x=200)

#Search box

searchBox=Entry(mainBody,width=80,relief='flat',bg='blue',font='10')
searchBox.place(x=0,y=0,height=35)

#Main body buttons
searchButton=Button(mainBody,text='Search',width=16,state="disabled")
searchButton.place(x=484,y=0,height=35)




#Main function call
root.mainloop()