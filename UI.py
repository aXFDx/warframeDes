#-*- conding:utf-8 -*-
from tkinter import *
import getURL
import time, datetime

win = Tk()
num = 0
global timeM, warnM
def showUI():
    data = getURL.getRestMsg()
    print("展示UI")
    win.title("迷你奥迪斯")
    win.geometry("250x600")
    win.resizable(width=False, height=True)
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

# def readTimeJSON():
#     global num
#     num = num + 10


def refreshTime():
    global timeM
    # readTimeJSON()
    text = getURL.getRestMsg()
    interval = int(text['cetus']['cetusTime']) - int(text['time'])
    intervalDate = datetime.datetime.fromtimestamp(interval)
    # timeM["text"] = num
    timeM["text"] = intervalDate.strftime("%Y-%m-%d %H:%M:%S")
    win.after(1000, refreshTime)
