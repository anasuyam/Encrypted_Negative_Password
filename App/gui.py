from Tkinter import *
from PIL import ImageTk, Image
from aes import *
from modulegui import *
from reg import *
a=Tk()
a.geometry('1000x500')

path = 'blue-background.jpg'

img = ImageTk.PhotoImage(Image.open(path))
panel = Label(a, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

labelfont = ('times', 20, 'bold')
widget = Label(a, text='Register and Sign Up')
widget.config( fg='white',bg="black")  
widget.config(font=labelfont)           
widget.config(height=1, width=20) 
widget.place(x=300,y=10)

labelfont = ('times', 19, 'bold')
widget1 = Label(a, text='Log In')
widget1.config( fg='white',bg="black")  
widget1.config(font=labelfont)           
widget1.config(height=1, width=20) 
widget1.place(x=190,y=190)

labelfont1 = ('times', 13, 'bold')
b1=Button(a,text='>>>')
b1.config( fg='white',bg="black")  
b1.config(font=labelfont1)           
b1.config(height=1, width=5) 
b1.place(x=500,y=190)

labelfont = ('times', 19, 'bold')
widget1 = Label(a, text='Registration')
widget1.config( fg='white',bg="black")  
widget1.config(font=labelfont)           
widget1.config(height=1, width=20) 
widget1.place(x=190,y=390)

labelfont1 = ('times', 13, 'bold')
b1=Button(a,text='>>>',command=lambda:register())
b1.config( fg='white',bg="black")  
b1.config(font=labelfont1)           
b1.config(height=1, width=5) 
b1.place(x=500,y=390)

a.mainloop()
