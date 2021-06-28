import csv
import math
from tkinter import *
import tkinter as tk
import datetime

def bubbleSortByDate(arr):
    arrLen = len(arr)
  
    for i in range(arrLen-1):
        for j in range(0, arrLen-i-1):
              if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def getDateString(dateString):
    datetimeFormat = datetime.datetime.strptime(dateString, r'%Y/%m/%d %H:%M:%S')

    difference = datetimeFormat - datetime.datetime.now()
    diffInSeconds = difference.total_seconds

    days = math.floor(divmod(diffInSeconds, 86400)[0])
    months = 0
    minutes = math.floor(divmod(diffInSeconds, 60)[0])
    hours = 0

    if days > 30:
        months = days // 30
        days -= months * 30
    if minutes > 60:
        hours = minutes // 60
        minutes -= hours * 60

    formattedString = ""

    if not months == 0:
        formattedString += str(months) + " months. "
    if not days == 0:
        formattedString += str(days) + " days. "

    if days == 0 and months == 0:
        if not hours == 0:
            formattedString += str(hours) + " hours. "
        if not minutes == 0:
            formattedString += str(minutes) + " minutes. "

    if not formattedString == "":
        formattedString += "remaining."

    return formattedString    

def sortedTasks():
    f=open("studentdetails.csv","r")
    s_reader = csv.reader(f)

    urgent = []
    middle = []
    low = []

    rowPointer = 0
    for item in s_reader:
        if rowPointer == 0:
            rowPointer += 1
            continue
        print(item)
        if item == []:
            continue

        if item[2] == '3':
            urgent.append(item)
        elif item[2] == '2':
            middle.append(item)
        elif item[2] == '1':
            low.append(item)
        
    urgentSorted = bubbleSortByDate(urgent)
    middleSorted = bubbleSortByDate(middle)
    lowSorted = bubbleSortByDate(low)

    f.close()

    return { 'urgent': urgentSorted, 'middle': middleSorted, 'low': lowSorted }

# sortedTasks()

def write(year, month, day, hour, minute,task,flag):
#def write():
        f=open("studentdetails.csv","a",newline='\n' )
        s_writer=csv.writer(f)

        date = datetime.datetime(year, month, day, hour, minute)

        eachrow=[date, task, flag]
        s_writer.writerow(eachrow)
        f.close()

# root = Tk()
# root.geometry("700x600")
# my_text = Text(root, width = 90, height = 20)
# my_text.pack(pady = 15)


# for row in list1:
#     for item in row:
#         print(item)

# root.mainloop()
