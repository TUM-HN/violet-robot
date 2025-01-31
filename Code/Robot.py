import tkinter as tk
from tkinter import ttk
import pygame
from PIL import Image, ImageTk
import time
from time import sleep
import sys 
import signal
import threading 
from threading import Thread
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


try:
    from stypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

PAHT_CRED = './credentials.json'
URL_DB = 'https://atento-robot.firebaseio.com/'

root= tk.Tk()
root.geometry("600x400")
root.configure(background='blue')
root.resizable(False,False)
root.title("Robot")



a1 = 'Face/a1.png'
a2 = 'Face/a2.png'
a3 = 'Face/a3.png'
a4 = 'Face/a4.png'
a5 = 'Face/a5.png'
a6 = 'Face/a6.png'
a7 = 'Face/a7.png'
a8 = 'Face/a8.png'
a9 = 'Face/a9.png'
a10 = 'Face/a10.png'
a11 = 'Face/a11.png'
a12 = 'Face/a12.png'
a13 = 'Face/a13.png'
a14 = 'Face/a14.png'
a15 = 'Face/a15.png'
a16 = 'Face/a16.png'
a17 = 'Face/a17.png'
a18 = 'Face/a18.png'
a19 = 'Face/a19.png'
a20 = 'Face/a20.png'

i1 = 'Icons/1.png'
i2 = 'Icons/2.png'
i3 = 'Icons/3.png'
i4 = 'Icons/4.png'




#set window color








faceFeedback1 = [a20,a20,a1,a7,a1,a7,a20,a20,a1,a7,a1,a7,a1,a7,a20,a20,a1,a7,a1,a7,a1,a7,a20,a20]

refMenu= 'Child_Instructions'

refActivity= 'Child_Activity'

class GuiPart:
    def __init__(self, master, endCommand):
        global vB
        vB=0
       
        # Set up the GUI
        # console = Tkinter.Button(master, text='Done', command=endCommand)
        #console.pack()  #fill = BOTH, expand=1
        # Add more GUI stuff here depending on your specific needs
        load = Image.open('Face/a17.png') #Default image
        load2 = load.resize((600, 400))
        #load2= load.fill(BOTH, expand=1)
        #load2 = load.resize((200, 160), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load2)
        img = ttk.Label(root, image=render)
        img.image = render
        img.place(x=0, y=0)
        
        

for a in faceFeedback1:
    load = Image.open(a)
    #load2 = load.resize((200, 160), Image.ANTIALIAS)
    load2 = load.resize((600, 400))
    render = ImageTk.PhotoImage(load2)
    img = ttk.Label(root, image=render)
    img.image = render
    img.place(x=0, y=0)
    root.update()
    img.pack()
              

   



    

     
    
    
    

                
   

#root.attributes('-fullscreen',True) #'-fullscreen',True

#root.geometry("200x180+0+0")



root.mainloop(  )
        
 
    
        



