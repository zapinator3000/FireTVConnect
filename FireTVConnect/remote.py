from tkinter import *
import FireTVConnect as firetv
tv=firetv.Connector("192.168.1.73")
tv.Reset()
tv.Connect()
def test():
    print("test")
def up():
    tv.KeyEvent("Up")
def down():
    tv.KeyEvent("Down")
def select():
    tv.KeyEvent("Enter")
def right():
    tv.KeyEvent("Right")
def left():
    tv.KeyEvent("Left")
def home():
    tv.KeyEvent("Home")
def back():
    tv.KeyEvent("back")
def forward():
    tv.KeyEvent("forward")
root = Tk() 
frame = Frame(root) 
frame.pack() 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Up', fg ='green',command=up) 
redbutton.pack( side = TOP) 
greenbutton = Button(frame, text = 'Left', fg ='red',command=left) 
greenbutton.pack( side = LEFT) 
brownbutton = Button(frame, text = 'Select', fg='brown',command=select) 
brownbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Right', fg ='blue',command=right) 
bluebutton.pack( side = LEFT )
fwbut = Button(bottomframe, text ='FFW', fg ='black',command=forward) 
fwbut.pack( side = RIGHT)
playbut = Button(bottomframe, text ='Play/Pause', fg ='red',command=back) 
playbut.pack( side = BOTTOM) 
revbut = Button(bottomframe, text ='REV', fg ='black',command=back) 
revbut.pack( side = LEFT)
homebutt = Button(bottomframe, text ='Home', fg ='blue',command=home) 
homebutt.pack( side = BOTTOM)
blackbutton = Button(bottomframe, text ='Down', fg ='black',command=down) 
blackbutton.pack( side = BOTTOM)




root.mainloop() 
