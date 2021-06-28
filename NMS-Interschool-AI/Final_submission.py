#----------------------MODULES-------------------


from tkinter import *
import tkinter as tk
import tkinter
import tkinter.messagebox
import time        
import pyperclip    
import webbrowser

from threading import Timer   
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
discord = Color("#38393E")

#
import sys
import time
from time import sleep
from PIL import ImageTk, Image
import csvreadwritemultiple

# from timetable import *

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

c = Canvas(root, width=10000, height=10000, bg=matt_black,highlightbackground=matt_black)
c.place(x=0, y=0)



a = Canvas(root,width=10000,height=1000,bg=blacksy)
a.place(x=0,y=10)




sch = Canvas(root, width=1200, height=1000, bg="grey")
sch.place(x=0, y=0)

def fetchdata():
    urgent = csvreadwritemultiple.sortedTasks()["urgent"]
    middle = csvreadwritemultiple.sortedTasks()["middle"]
    low = csvreadwritemultiple.sortedTasks()["low"]

    

    schtab =Label(sch, text = urgent,height=10,width=50)
    schtab.place(x=200, y=40)
    urgenttext = ""

    for i in urgent:
        for j in i:
            urgenttext += j+"\t"
        urgenttext += "\n"


    schtab.config(text=urgenttext)
    urgentheading = Label(sch, text = "URGENT",bg = "red")
    urgentheading.place(x=300,y=10)





    midtab =Label(sch, text = urgent,height=10,width=50)
    midtab.place(x=200, y=240)
    midtext = ""


    for i in middle:
        for j in i:
            midtext += j+"\t"
        midtext += "\n"

    midtab.config(text=midtext)
    midheading = Label(sch, text = "Middle",bg = "yellow")
    midheading.place(x=300,y=200)


    lowtab =Label(sch, text = low,height=10,width=50)
    lowtab.place(x=200, y=430)
    lowtext = ""


    for i in low:
        for j in i:
            lowtext += j+"\t"
        lowtext += "\n"

    lowtab.config(text=lowtext)
    lowheading = Label(sch, text = "Low",bg = "green")
    lowheading.place(x=300,y=400)











home = Canvas(root, width=1200, height=1000, bg=discord,highlightbackground=matt_black)
home.place(x=0, y=0)

link = Canvas(root, width=1200, height=1000, bg=white,highlightbackground=matt_black)
link.place(x=0, y=0)

tt = Canvas(root,width=1200,height=1000,bg="white",highlightbackground=matt_black)
tt.place(x=0,y=0)
my_text6 = Text(tt, width = 200, height = 30,bg = "white",border=0,borderwidth=0,highlightbackground="white",background='white')
my_text6.pack(pady = 40,padx=40)
my_text6.place(x=52,y=80)

text_file = open("timetable.txt", 'r')
stuff = text_file.read()

my_text6.insert(END, stuff)
text_file.close()

def save_txt():
    text_file = open('C:\\Users\\richie\\Downloads\\timetable\\timetable.txt','w')
    text_file.write(my_text.get(1.0, END))

f = Button(tt, text = "Save", command = save_txt, relief ="ridge", bg = "WHITE", fg="black", font=('Century Gothic',16), width=15, height =1)
f.place(x=300,y=400)

subjects = {
    "phy": ["9508197762", "ZzVCM1dnem1zM0FnYVN1OEZmc0NFdz09"],
    "chem": ["5931742575", "TW1JYWxDRllhNEdIaytyeUpveDUzUT09"],
    "eng": ["4096292952", "N2p5RFAya1NVTndtM2ZBNXR5ZFBFZz09"],
    "maths": ["7599500314", "MmJGUUpLWHhHOEpTYlZWNC9kV1N0QT09"],
    "cs": ["7228857539", "bUVBcGpKS1hJVUxtYnhSNVZpWWMyQT09"]
}

def openZoom(subject):
    webbrowser.open_new_tab("https://asianschool-bh.zoom.us/j/" + subjects[subject][0] + "?pwd=" + subjects[subject][1])

seti = Canvas(root,width=1200,height=1000,bg=discord,highlightbackground=discord)
seti.place(x=0,y=0)

q = Canvas(root, width=40, height=1000,bg=matt_black,border=0,highlightbackground=matt_black)
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
    fetchdata()
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



#user_input = input()
#-----------------------TEXT ON MENU-----------------------
pic15= PhotoImage(file="27.png")
img_label15= Label(image=pic15)
pic16= PhotoImage(file="bot_input.png")
img_label16= Label(image=pic16)
slide = Label(q, text = "HIDE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 14)
slide1 = Label(q, text = "HOME      ",bd=2,bg=matt_black,fg="white").place(x = 45,y = 59)
slide2 = Label(q, text = "SCHEDULE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 109)
slide3 = Label(q, text = "LINKS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 159)
slide4 = Label(q, text = "TIMETABLE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 209)
slide5 = Label(q, text = "SAVE",bd=2,bg=matt_black,fg="white").place(x = 45,y = 259)
slide6 = Label(q, text = "SETTINGS",bd=2,bg=matt_black,fg="white").place(x = 45,y = 409)
assist = Label(home, text = "Type help and press enter if you require assistance",bd=2,bg=discord,fg="white",height=5,width=50).place(x = 400,y = 200)





# speech_botreplay = Canvas(home,width=350, height=175, bg=discord,highlightthickness=0)
# speech_botreplay.place(x=400, y=200)
# speech_botreplay.create_image(10, 10, image = pic16, anchor = NW)


# speechreplay = Canvas(home,width=350, height=175, bg=discord,highlightthickness=0)
# speechreplay.place(x=50, y=100)
# speechreplay.create_image(10, 10, image = pic15, anchor = NW)

# speech_bot = Canvas(home,width=350, height=175, bg=discord,highlightthickness=0)
# speech_bot.place(x=400, y=400)
# speech_bot.create_image(10, 10, image = pic16, anchor = NW)

# speech = Canvas(home,width=350, height=175, bg=discord,highlightthickness=0)
# speech.place(x=50, y=300)
# speech.create_image(10, 10, image = pic15, anchor = NW)





#btn = Button(root, text='Welcome to Tkinter!', width=40,
            #height=5, bd='1', command=root.destroy)


            
button_col = Color("#0E63C8")
button_col2 = Color("#B4B4B4")
greyish = Color("#cfcfcf")
stuff=""
my_text = Text(home, width = 70, height = 1,bg=greyish)
my_text.pack(pady = 40,padx=40)
my_text.place(x=125,y=450)
my_text.insert(END, stuff)
input2 = "entered text"

my_text4 = Text(home, width = 23, height = 2,bg = button_col,border=0,borderwidth=0,highlightbackground=button_col,background=discord)
my_text4.pack(pady = 40,padx=40)
my_text4.place(x=125,y=535)



my_text2 = Text(home, width = 60, height = 2,bg = button_col,border=0,borderwidth=0,highlightbackground=button_col,background='GREY')
my_text2.pack(pady = 40,padx=40)
my_text2.place(x=125,y=400)

botText = Text(home, width = 23, height = 4,bg = button_col2,border=0,borderwidth=0,highlightbackground=button_col2,background="grey")
botText.pack(pady = 40,padx=40)
botText.place(x=480,y=300)
slide7 = Label(home, text = "Enter Text",bd=2,bg=matt_black,fg="white").place(x = 67,y = 450)
slide8 = Label(home, text = "B.O.T---->",bd=2,bg=matt_black,fg="white").place(x = 418,y = 305)
my_text5 = Text(home, width = 40, height = 20,bg = discord,border=0,borderwidth=0,highlightbackground=discord,fg="white")
my_text5.pack(pady = 40,padx=40)
my_text5.place(x=100,y=75)

#my_text4.config(state=DISABLED)


        

allfunc = "Hi! I help in Daily Tasks for you school\n"

year= None
month= None
day= None
hour= None
minute = None
task = None
flag = None

formedFilled = False

yearClicked = False
monthClicked = False
dayClicked = False
hourClicked = False
minuteClicked = False
extraClicked = False
taskClicked = False
flagClicked = False

def resetValues():
    global year, month, day, hour, minute, task, flag, formedFilled

    global yearClicked, monthClicked, dayClicked, hourClicked, minuteClicked, extraClicked, taskClicked, flagClicked

    year= None
    month= None
    day= None
    hour= None
    minute = None
    task = None
    flag = None

    yearClicked = False
    monthClicked = False
    dayClicked = False
    hourClicked = False
    minuteClicked = False
    extraClicked = False
    taskClicked = False
    flagClicked = False

    formedFilled = False

def callWriteFn():
    global year, month, day, hour, minute, task, flag, formedFilled

    print('call write fn')

    csvreadwritemultiple.write(int(year), int(month), int(day), int(hour), int(minute), task, flag)

    formedFilled = True

def callcallEnter():
    my_text.delete('1.0', END)
    my_text.insert(END, 'done')
    callenter()

def askFlag(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Flag')

    my_text.unbind('<Return>')

    if not flag:
        my_text.bind('<Return>', handleFlag)

def handleFlag(x=None):
    global flag, flagClicked

    flagClicked = True

    flag = my_text.get('1.0', END)
    flag = flag.strip('\n')
    print('flag', flag)
    my_text.delete('1.0', END)

    ask()

def askTask(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Task')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleTask)

def handleTask(x=None):
    global task, taskClicked

    taskClicked = True

    task = my_text.get('1.0', END)
    task = task.strip('\n')
    print('task', task)
    my_text.delete('1.0', END)

    ask()

def askYear(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Year')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleYear)

def handleYear(x=None):
    global year, yearClicked

    yearClicked = True

    year = my_text.get('1.0', END)
    year = year.strip('\n')
    print('year', year)
    my_text.delete('1.0', END)

    ask()

def askMonth(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Month')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleMonth)

def handleMonth(x=None):
    global month, monthClicked

    monthClicked = True

    month = my_text.get('1.0', END)
    month = month.strip('\n')
    print('month', month)
    my_text.delete('1.0', END)
    
    ask()

def askDay(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Day')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleDay)

def handleDay(x=None):
    global day, dayClicked

    dayClicked = True

    day = my_text.get('1.0', END)
    day = day.strip('\n')
    print('day', day)
    my_text.delete('1.0', END)
    
    ask()

def askMinute(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Minute')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleMinute)

def handleMinute(x=None):
    global minute, minuteClicked

    minuteClicked = True

    minute = my_text.get('1.0', END)
    minute = minute.strip('\n')
    print('minute', minute)
    my_text.delete('1.0', END)

    ask()

def askHour(x=None):
    botText.delete("1.0",END)
    botText.insert(END, 'Enter Hour')

    my_text.unbind('<Return>')
    my_text.bind('<Return>', handleHour)

def handleHour(x=None):
    global hour, hourClicked

    hourClicked = True

    hour = my_text.get('1.0', END)
    hour = hour.strip('\n')
    print('hour', hour)
    my_text.delete('1.0', END)

    ask()

def handleExtra(x=None):
    global extra, extraClicked

    extraClicked = True
    print('extra function')

    botText.delete("1.0",END)
    askHour()
    
def ask(x=None):
    global hourClicked, minuteClicked, dayClicked, monthClicked, yearClicked, taskClicked, flagClicked

    global hour, minute, day, month, year, task, flag

    if not extraClicked:
        handleExtra()
    elif not hourClicked:
        askHour()
    elif not minuteClicked:
        askMinute()
    elif not dayClicked:
        askDay()
    elif not monthClicked:
        askMonth()
    elif not yearClicked:
        askYear()
    elif not taskClicked:
        askTask()
    elif not flagClicked:
        askFlag()

    if hour and minute and day and month and year and task and flag:
        callWriteFn()
        callcallEnter()

def handleJoin(entry):
    entry = entry[5:]
    print(entry)
    openZoom(entry)

extravar = False
def enter(x):
    global save1 
    global save2
    global formedFilled
    
    save2 = my_text.get("1.0",END)
    
    my_text2.insert(END, x)
    my_text4.insert(END,save1) 

    if entry == "hi bot":
        botText.insert(END,"yes human")
    elif entry == "set":
        my_text.delete("1.0",END)
        botText.insert(END, 'I will ask you a bunch of details. Press enter to continue...')
        my_text.bind('<Return>', ask)
    elif entry == "link":
        botText.delete("1.0",END) 
        botText.insert(END,"initialing link prot...") 
    elif 'join' in entry:
        handleJoin(entry)

    elif entry == "help":
        my_text5.insert(END,allfunc)
        my_text5.insert(END,"These are the things i can do:- \n")
        my_text5.insert(END,"Type these to access the sub functions:- \n")
        my_text5.insert(END,"join------>\ncs\neng\nphy\nchem\nmath\nset------>\nFollow instructions from bot")
    elif entry == "done" and formedFilled:
        botText.delete("1.0",END)
        botText.insert(END,"data saved.")

        resetValues()
    else:
        botText.insert(END,"I don't understand")

    
history = True
def callenter(a=None):
    
#    speechshift()
#    speechshift2()

   
    global save1
    global save2
    
    botText.delete("1.0",END) 
    my_text2.delete("1.0",END)
    my_text4.delete("1.0",END)
    global entry

    entry = my_text.get("1.0",END)
    entry = entry.strip("\n") # done
    
    if entry == "":
        return
    # print(entry)

    
    global history
    if history:
        save1 = ""
        history = False
    else:
        save1 =  save2   
         
    enter(entry)    
    my_text.delete("1.0",END)
    

my_text.bind("<Return>",callenter)
global entry

shift = False


#def speechshift():
    
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

pic6= PhotoImage(file='cancel.png')

img_label6= Label(image=pic6)

pic7= PhotoImage(file='info.png')

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
img_label12= Label(image=pic12)

pic13= PhotoImage(file="25.png")
img_label13= Label(image=pic13)

pic14= PhotoImage(file="26.png")
img_label14= Label(image=pic14)

picmain= PhotoImage(file="send.png")
img_labelmain= Label(image=picmain)

picinfo= PhotoImage(file="frame.png")
img_labelinfo= Label(image=picinfo)

send = Button(home,image=picmain ,background=discord,relief="solid",activebackground=discord,border = 0,height=40,width=40)
send.bind("<Button-1>",callenter)
# send.pack()
send.place(x= 695, y= 440)

#------------------------BUTTONS-----------------------------

root.resizable(width=False, height=False)
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
btn8 = Button(link,image=pic10,background=white,activebackground = white ,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('cs'))
btn8.pack()
btn8.place(x= 100, y= 100)

btn9 = Button(link,text="Home",image=pic11,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('phy'))
btn9.pack()
btn9.place(x= 300, y= 100)

btn10 = Button(link,image=pic12,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('chem'))
btn10.pack()
btn10.place(x= 100, y= 300)

btn11 = Button(link,image=pic13,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('eng'))
btn11.pack()
btn11.place(x= 300, y= 300)

btn12 = Button(link,image=pic14,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('math'))
btn12.pack()
btn12.place(x= 500, y= 100)

btn13 = Button(link,image=pic15,background=white,activebackground = white,relief="solid",border = 0,height=200,width=200,command=lambda: openZoom('eng'))
btn13.pack()
btn13.place(x= 500, y= 300)


mainslide = Label(seti,bg=discord,fg="white",image=picinfo).place(x = 0,y =30)
root.mainloop()