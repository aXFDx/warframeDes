#-*- conding:utf-8 -*-
from tkinter import *
import getURL
import time, datetime

win = Tk()
num = 0
interval = 0
intervalDate = ""
dayOrNight = ""
global timeM, warnM


def showUI():
    global interval, dayOrNight
    data = getURL.getRestMsg()
    print("展示UI")
    win.title("迷你奥迪斯")
    win.geometry("250x600")
    win.resizable(width=False, height=True)
    text = getURL.getRestMsg()
    interval = int(text['cetus']['cetusTime']) - int(text['time'])
    if text['cetus']['day'] == "True":
        dayOrNight = "白天"
    else:
        dayOrNight = "黑夜"
    pyTime()
    warn()
    win.after(1000,refreshTime())
    win.mainloop()


def pyTime():
    global timeM
    timeT = Label(win, text="平原时间", font=("Arial", 12), width=10, height=2)
    timeT.pack(side=TOP)
    #timeM = Label(win, text="10：0：0", font=("Arial", 12), width=10, height=2)
    timeM = Label(win, text="", font=("Arial", 12), width=20, height=2)
    timeM.pack(side=TOP)


def warn():
    warnT = Label(win, text="警报", font=("Arial", 12), width=10, height=2)
    warnT.pack(side=TOP)
    warnmsg = "内容   剩余时间\n反应堆   10：00\n催化剂  5：00\n无态晶   99：00"
    warnM = Message(win, text=warnmsg)
    warnM.config(font=("Arial", 12))
    warnM.pack()


def readTimeJSON():
    # global num
    # num = num + 10
    global interval
    global intervalDate
    global dayOrNight
    # text = getURL.getRestMsg()
    # interval = int(text['cetus']['cetusTime']) - int(text['time'])
    # if text['cetus']['day'] == "True":
    #     dayOrNight = "白天"
    # else:
    #     dayOrNight = "黑夜"

    if interval == 0:
        if dayOrNight == "白天":
            interval = 3600
            dayOrNight = "黑夜"
            intervalDate = datetime.datetime.fromtimestamp(interval)
        else:
            interval = 3600*2
            dayOrNight = "白天"
            intervalDate = datetime.datetime.fromtimestamp(interval)
    else:
        interval = interval-1
        intervalDate = datetime.datetime.fromtimestamp(interval)
    # intervalDate = datetime.datetime.fromtimestamp(interval)


def refreshTime():
    global timeM
    global intervalDate
    readTimeJSON()
    # timeM["text"] = num
    timeM["text"] = intervalDate.strftime("%H:%M:%S")+dayOrNight
    win.after(1000, refreshTime)
