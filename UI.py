#-*- conding:utf-8 -*-
from tkinter import *
import getURL

win = Tk()
num = 0
def showUI():
    data = getURL.getRestMsg()
    print("展示UI")
    win.title("迷你奥迪斯")
    win.geometry("250x600")
    win.resizable(width=False, height=True)
    pyTime()
    warn()
    win.mainloop()

def pyTime():
    global num
    timeT = Label(win, text="平原时间", font=("Arial", 12), width=10, height=2)
    timeT.pack(side=TOP)
    timeM = Label(win, text="10：0：0", font=("Arial", 12), width=10, height=2)
    num = num + 10
    timeM = Label(win, text=num, font=("Arial", 12), width=10, height=2)
    timeM.pack(side=TOP)
    win.after(1000,pyTime)

def warn():
    warnT = Label(win, text="警报", font=("Arial", 12), width=10, height=2)
    warnT.pack(side=TOP)
    li = ['C','python','php','html','SQL','java']
    warnmsg = "内容   剩余时间\n反应堆   10：00\n催化剂  5：00\n无态晶   99：00"
    warnM = Message(win, text = warnmsg)
    warnM.config(font=("Arial", 12))
    warnM.pack()