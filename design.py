#----------------------MODULES-------------------

from os import terminal_size
from tkinter import *
import tkinter as tk
import tkinter
import tkinter.messagebox
import time               
from tkinter import ttk 
import tkinter as notebook
from colour import Color
matt_black = Color("#171717")
aqua_blue = Color("#00916E")
emerald = Color("#1982C4")
cyber_yellow = Color("#FFCF00")
purple = Color("#FA003F")
orange = Color("#EE6123")
hot_pink = Color("#FF69B4")
blacksy=Color("#171717")
white = Color("#e5e5e5")
#
import sys
import time
from time import sleep
from PIL import ImageTk, Image








#---------------------LOADING CODE-----------------

# for i in range(101):
#     sys.stdout.write('\r')
#     sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
#     sys.stdout.flush()
#     sleep(0.02)


#-------------------TKINTER-------------------------


root = tk.Tk()

root.geometry("750x600")
root.title("Student Assistant")



#-------------------CANVAS----------------

c = Canvas(root, width=10000, height=10000, bg=matt_black)
c.place(x=0, y=0)



a = Canvas(root,width=10000,height=1000,bg=blacksy)
a.place(x=0,y=0)

sch = Canvas(root, width=1200, height=1000, bg="white")
sch.place(x=0, y=0)

home = Canvas(root, width=1200, height=1000, bg="white")
home.place(x=0, y=0)

link = Canvas(root, width=1200, height=1000, bg=white)
link.place(x=0, y=0)

tt = Canvas(root,width=1200,height=1000,bg="white")
tt.place(x=0,y=0)

seti = Canvas(root,width=1200,height=1000,bg="white")
seti.place(x=0,y=0)

q = Canvas(root, width=40, height=1000,bg=matt_black,border=0)
q.place(x=0, y=0)



#------------------------FUNCTIONS-------------------------


def onClick2():
    response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()
    else:
        return None

#root.protocol('WM_DELETE_WINDOW',on_close)
#----------------------Slide-Menu---------------------
home.config(width=2000)
link.config(width=40)
sch.config(width=40)
tt.config(width=40)
seti.config(width=40)

menu = False
def onPress():
    global menu
    i=100
    if menu == True:
        while i>=40:
            
            q.config(width=i)
            i=i-1
            #time.sleep(0.01)
        menu = False
    else:
        while i<=115:
            
            q.config(width=i)
            i = i+1
            #time.sleep(0.01)
        menu = True
homevar = False

#-----------------------------HOME TAB---------------------------

def HomeOn():
    global homevar 
    home.config(width=2000)
    btn2.config(bg = matt_black)
    btn4.config(bg = matt_black)
    btn3.config(bg = matt_black)
    btn5.config(bg=matt_black)
    btn7.config(bg = matt_black)
#    slide1 = Label(q, text = "HOME      ",bd=10,bg=aqua_blue,fg="white").place(x = 40,y = 50)
    homevar = True


def HomeOff():
    global homevar       
    home.config(width=40)
#   slide1 = Label(q, text = "HOME      ",bd=10,bg=matt_black,fg="white").place(x = 40,y = 50)
    homevar = False
#--------------------LINKS-TAB-------------------------
linkvar = False


def LinksOn():
    global linkvar   
    link.config(width=2000)
    btn4.config(bg = matt_black)
    btn2.config(bg = matt_black)
    btn3.config(bg = matt_black)
    btn5.config(bg = matt_black)
    btn7.config(bg = matt_black)
    linkvar = True

def LinksOff():
    global linkvar
    link.config(width=40)
    linkvar = False

#----------------------Schedule-tab----------------------------
schvar = False

def SchOn():
    global schvar   
    sch.config(width=2000)
    btn4.config(bg = matt_black)
    btn2.config(bg = matt_black)
    btn3.config(bg = matt_black)
    btn5.config(bg = matt_black)
    btn7.config(bg = matt_black)
    schvar = True

def SchOff():
    global schvar
    sch.config(width=40)
    schvar = False


#-----------------timetable-tab-------------------

ttvar = False

def TTOn():
    global ttvar   
    tt.config(width=2000)
    btn4.config(bg = matt_black)
    btn2.config(bg = matt_black)
    btn3.config(bg = matt_black)
    btn5.config(bg = matt_black)
    btn7.config(bg = matt_black)
    
    ttvar = True

def TTOff():
    global ttvar
    tt.config(width=40)
    ttvar = False



#-------------settings-tab-------------------
setvar = False

def setOn():
    global setvar   
    seti.config(width=2000)
    btn4.config(bg = matt_black)
    btn2.config(bg = matt_black)
    btn3.config(bg = matt_black)
    btn5.config(bg = matt_black)
    btn7.config(bg = matt_black)
    
    setvar = True

def setOff():
    global setvar
    seti.config(width=40)
    setvar = False


#-----------------------TAB-MECHANICS--------------------------


def HomePhy():
    if homevar == False:
        HomeOn()
        LinksOff()
        SchOff()
        TTOff()
        setOff()
        

def LinksPhy():
    if linkvar == False:
        LinksOn()
        HomeOff()
        SchOff()
        TTOff()
        setOff()

def SchPhy():
    if schvar == False:
        SchOn()
        HomeOff()
        LinksOff()
        TTOff()
        setOff()
        
def TTphy():
    if ttvar == False:
        TTOn()
        SchOff()
        HomeOff()
        LinksOff()
        setOff()

def Setphy():
    if setvar == False:
        TTOff()
        SchOff()
        HomeOff()
        LinksOff()
        setOn()


def newWindow():
    response=tkinter.messagebox.askyesno('Exit','Are you sure you want to exit?')
    if response:
        root.destroy()
    else:
        return None



#-----------------------TEXT ON MENU-----------------------

slide = Label(q, text = "HIDE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 14)
slide1 = Label(q, text = "HOME      ",bd=2,bg=matt_black,fg="white").place(x = 45,y = 59)
slide2 = Label(q, text = "SCHEDULE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 109)
slide3 = Label(q, text = "LINKS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 159)
slide4 = Label(q, text = "TIMETABLE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 209)
slide5 = Label(q, text = "SAVE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 259)
slide6 = Label(q, text = "SETTINGS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 409)

#btn = Button(root, text='Welcome to Tkinter!', width=40,
            #height=5, bd='1', command=root.destroy)



#------------------------IMAGES--------------------

yes= PhotoImage(file='menu.png')

img_label= Label(image=yes)

pic2= PhotoImage(file='3.png')
img_label2= Label(image=pic2)

pic3= PhotoImage(file='17.png')

img_label3= Label(image=pic3)

pic4= PhotoImage(file='12.png')

img_label4= Label(image=pic4)

pic5= PhotoImage(file="13.png")

img_label5= Label(image=pic5)

pic6= PhotoImage(file='20.png')

img_label6= Label(image=pic6)

pic7= PhotoImage(file='14.png')

img_label7= Label(image=pic7)
pic8= PhotoImage(file="fullscreen.png")
img_label8= Label(image=pic8)


pic9= PhotoImage(file="1.png")
img_label9= Label(image=pic9)

pic10= PhotoImage(file="22.png")
img_label10= Label(image=pic10)

pic11= PhotoImage(file="23.png")
img_label11= Label(image=pic11)

pic12= PhotoImage(file="24.png")
img_label12= Label(image=pic9)

pic13= PhotoImage(file="25.png")
img_label13= Label(image=pic9)

pic14= PhotoImage(file="26.png")
img_label14= Label(image=pic9)

pic15= PhotoImage(file="27.png")
img_label15= Label(image=pic9)
#------------------------BUTTONS-----------------------------


buttonClicked = False
button1 = True
btn = Button(root,image=yes,background=matt_black,activebackground = matt_black ,relief="solid",border = 0,height=35,width=35,command=onPress)
btn.pack()
btn.place(x= 5, y= 5)

btn2 = Button(root,text="Home",image=pic2,background=blacksy,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=HomePhy)
btn2.pack(padx=50,pady=50)
btn2.place(x= 5, y= 50)

btn3 = Button(q,image=pic3,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=SchPhy)
btn3.pack()
btn3.place(x= 5, y= 100)

btn4 = Button(q,image=pic4,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=LinksPhy)
btn4.pack()
btn4.place(x= 5, y= 150)

btn5 = Button(q,image=pic5,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=TTphy)
btn5.pack()
btn5.place(x= 5, y= 200)

btn6 = Button(q,image=pic6,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=onClick2)
btn6.pack()
btn6.place(x= 5, y= 250)

btn7 = Button(q,image=pic7,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=Setphy)
btn7.pack()
btn7.place(x= 5, y= 400)



#--------------------HOVER HIGHLIGHT-------------------

# def on_enter(e):
#     btn7['background'] = "grey"
# def on_leave(e):
#     btn7['background'] = matt_black
# btn7.bind("<Enter>", on_enter)
# btn7.bind("<Leave>", on_leave)

#--------------------Buttons for Home-------------------
#home_start = Label(home, text = "Welcome",bd=2,bg=matt_black,fg="white").place(x = 100,y = 100)
btn8 = Button(link,image=pic10,background=white,activebackground = white ,relief="solid",border = 0,height=200,width=200,command=None)
btn8.pack()
btn8.place(x= 100, y= 100)

btn9 = Button(link,text="Home",image=pic11,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=None)
btn9.pack()
btn9.place(x= 300, y= 100)

btn10 = Button(link,image=pic12,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=None)
btn10.pack()
btn10.place(x= 100, y= 300)

btn11 = Button(link,image=pic13,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=None)
btn11.pack()
btn11.place(x= 300, y= 300)

btn12 = Button(link,image=pic14,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=None)
btn12.pack()
btn12.place(x= 500, y= 100)

btn13 = Button(link,image=pic15,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=newWindow)
btn13.pack()
btn13.place(x= 500, y= 300)

# btn14 = Button(link,image=pic7,background=matt_black,activebackground = matt_black,relief="solid",border = 0,height=35,width=35,command=Setphy)
# btn14.pack()
# btn14.place(x= 5, y= 400)
#-------------------------------
#label=Label(tt, text='Timetable', font=('Fixedsys',32))
#tt.pack(pady=5)
# my_text = Text(tt, width = 90, height = 20)
# my_text.pack(pady = 70,padx= 50)

# text_file = open(r"timetable.txt", 'r')
# stuff = text_file.read()

# my_text.insert(END, stuff)
# text_file.close()

#Button(tt, text = "Save", command = None, relief ="ridge", bg = "WHITE", fg="black", font=('Century Gothic',16), width=15, height =1).pack(pady=15)
# def end():
#     a.destroy
#     a.config(width=0,height=0)
#     None
# a = Canvas(root,width=10000,height=1000,bg="grey")
# a.place(x=0,y=0)
# loading = Label(a, image=pic8,border=0,bg="grey",fg="white",height=355,width=350).place(x = 350,y = 300,anchor=CENTER)
# a.after(5000,end)

# entry1 = tk.Entry (link) 
# input = link.create_window(200, 140, window=entry1)
# rint(link)
# stuff="hello"
# my_text = Text(link, width = 20, height = 20)
# my_text.config()
# my_text.pack(pady = 15)
# my_text.insert(END, stuff)
#-----------------------------------
root.mainloop()
