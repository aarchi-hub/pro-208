import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def musicwindow():

   
    print("\n\t\t\t\tMUSIC APP")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("400x300")

    global selectlabel
    global listbox
    global playButton
    global infolabel
    global Stop
    global Upload
    global Download

    selectlabel = Label(window, text= "Select song", font = ("Calibri",50))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton = Button(window,text ="play",width =10,bd = 1,bg ="SkyBlue",font = ("Calibri",10))
    playButton.place(x = 30,y = 200)

    Stop = Button(window,text="Stop",bd=1,width=10,bg = "SkyBlue", font = ("Calibri",10))
    Stop.place(x=200,y=200)

    Upload = Button(window,text = "Upload",width =10,bd = 1,bg ="SkyBlue",font =("Calibri,10"))
    Upload.place(x=30, y=250)

    Download = Button(window,text = "Download",width =10,bd = 1,bg ="SkyBlue",font =("Calibri,10"))
    Download.place(x=200, y=250)

    infolabel = Label(window, text= "", font = ("Calibri",10))
    infolabel.place(x=4, y=280)


    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicwindow ()

setup()