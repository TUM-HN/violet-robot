
import time

from tkinter import *

root = Tk()

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

imagelist = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19]

#imagelist = ["dog001.gif","dog002.gif","dog003.gif",
            # "dog004.gif","dog005.gif","dog006.gif","dog007.gif"]

# extract width and height info
photo = PhotoImage(file=imagelist[5])
width = photo.width()
height = photo.height()
canvas = Canvas(width=800, height=500)
canvas.pack()

# create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

counterPhoto=0

# loop through the gif image objects for a while
for k in range(0, 1):
    for gif in giflist:
        counterPhoto=counterPhoto+1
        canvas.delete(ALL)
        canvas.create_image(400, 250, image=gif)
        canvas.update()
        time.sleep(0.1)
        if counterPhoto==len(giflist):
            photo = PhotoImage(file=imagelist[1])
            canvas.delete(ALL)
            canvas.create_image(400, 250, image=photo)
            
            #giflist.append(photo)
            canvas.update()
            print ("Listo")

root.mainloop()
