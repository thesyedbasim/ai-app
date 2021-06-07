# import everything from tkinter module
from tkinter import *
import tkinter as tk
import tkinter
import tkinter.messagebox
import time

import tkinter as tk                    
from tkinter import ttk 
import tkinter as notebook
from colour import Color
matt_black = Color("#171717")
aqua_blue = Color("#00a8f3")

  
root = tk.Tk()
  
root.geometry("600x500")
root.title("Student Assistant")

tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl,width= 100,height=100)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")
  
ttk.Label(tab1, 
          text ="die") 
ttk.Label(tab2,
          text ="hey")



title = Label(root,text="heyy", bg=matt_black, font=("bold", 30))
title.pack()



c = Canvas(root, width=10000, height=10000, bg="white")
c.place(x=0, y=0)



a = Canvas(root,width=10000,height=1000,bg=matt_black)
a.place(x=0,y=0)

home = Canvas(root, width=1200, height=1000, bg="red")
home.place(x=0, y=0)

link = Canvas(root, width=1200, height=1000, bg="blue")
link.place(x=0, y=0)

q = Canvas(root, width=120, height=1000,bg=matt_black)
q.place(x=0, y=0)

menu = True

# the slide menu
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
homevar = True

def HOME():
    global homevar
    l=1000
    if homevar == True:
        while l>=40:
            
            home.config(width=l)
            l=l-1
            #time.sleep(0.01)
        homevar = False
    else:
        while l<=1150:
            
            home.config(width=l)
            l = l+1
            #time.sleep(0.01)
        homevar = True


linkvar = True

def Links():
    global linkvar
    b=1000
    if linkvar == True:
        while b>=40:
            
            link.config(width=b)
            b=b-1
            #time.sleep(0.01)
        linkvar = False
    else:
        while b<=1150:
            
            link.config(width=b)
            b = b+1
            #time.sleep(0.01)
        linkvar = True


slide = Label(q, text = "HIDE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 14)
slide1 = Label(q, text = "HOME",bd=2,bg=matt_black,fg="white").place(x = 45,y = 59)
slide2 = Label(q, text = "SCEDHULE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 109)
slide3 = Label(q, text = "LINKS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 159)
slide4 = Label(q, text = "TIMETABLE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 209)
slide5 = Label(q, text = "SAVE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 259)
slide6 = Label(q, text = "SETTINGS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 409)


#btn = Button(root, text='Welcome to Tkinter!', width=40,
             #height=5, bd='1', command=root.destroy)

def onClick():
    tkinter.messagebox.showinfo("Exit?",  "Exit this application?")
    root.destroy

yes= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\icon_menu.png')

img_label= Label(image=yes)

pic2= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\cil-home.png')

img_label2= Label(image=pic2)

pic3= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\cil-comment-square.png')

img_label3= Label(image=pic3)

pic4= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\cil-external-link.png')

img_label4= Label(image=pic4)

pic5= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\cil-view-module.png')

img_label5= Label(image=pic5)

pic6= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\cil-save.png')

img_label6= Label(image=pic6)

pic7= PhotoImage(file=r'C:\Users\richie\Downloads\timetable\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\images\icons\icon_settings.png')

img_label7= Label(image=pic7)


# Create a Button
#button = Button(root, text="Click Me", command=onClick, height=5, width=5)
#button.pack()
#utton.place(x=100,y=100)
#c = Canvas(root, width=1000000, height= 50, bg="grey")
#c.place(x=0, y=0)


buttonClicked = False
button1 = True



btn = Button(root,image=yes,background=matt_black,activebackground = aqua_blue ,relief="solid",border = 0,height=35,width=35,command=onPress)
btn.pack()
btn.place(x= 5, y= 5)

btn2 = Button(root,image=pic2,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=HOME)
btn2.pack()
btn2.place(x= 5, y= 50)



btn3 = Button(root,image=pic3,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=None)
btn3.pack()
btn3.place(x= 5, y= 100)

btn4 = Button(root,image=pic4,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=Links)
btn4.pack()
btn4.place(x= 5, y= 150)

btn5 = Button(root,image=pic5,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=None)
btn5.pack()
btn5.place(x= 5, y= 200)

btn6 = Button(root,image=pic6,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=None)
btn6.pack()
btn6.place(x= 5, y= 250)

btn7 = Button(q,image=pic7,background=matt_black,activebackground = "grey",relief="solid",border = 0,height=35,width=35,command=None)
btn7.pack()
btn7.place(x= 5, y= 400)





def on_enter(e):
    btn7['background'] = "grey"
def on_leave(e):
    btn7['background'] = matt_black


btn7.bind("<Enter>", on_enter)
btn7.bind("<Leave>", on_leave)



 
root.mainloop()
