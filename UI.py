#-*- conding:utf-8 -*-
from tkinter import *
import getURL
import time, datetime

win = Tk()
num = 0
#下一个变化时间减去服务器时间的差值  
interval = 0
#字符串形式的差值
intervalDate = ""
#白天还是夜晚
dayOrNight = ""
#JSON数据
global data
global timeM, warnM


#UI展示主界面
def showUI():
    global interval, dayOrNight
    win.title("迷你奥迪斯")
    win.geometry("250x600")
    win.resizable(width=False, height=True)
    #设置平原时间界面
    global timeM
    timeT = Label(win, text="平原时间", font=("Arial", 12), width=10, height=2)
    timeT.pack(side=TOP)
    timeM = Label(win, text="初始化中...", font=("Arial", 12), width=20, height=2)
    timeM.pack(side=TOP)
    #设置警报界面
    warnT = Label(win, text="警报", font=("Arial", 12), width=10, height=2)
    warnT.pack(side=TOP)
    warnmsg = "内容   剩余时间\n反应堆   10：00\n催化剂  5：00\n无态晶   99：00"
    warnM = Message(win, text=warnmsg)
    warnM.config(font=("Arial", 12))
    warnM.pack()
    #初始化信息
    initJSON()
    #刷新时间
    refreshTime()
    win.mainloop()

#处理时间数据
def readTimeJSON():
    global interval
    global intervalDate
    global dayOrNight
    if interval <= 0:
        if dayOrNight == "白天":
            interval = 3000
            dayOrNight = "夜晚"
            intervalDate = datetime.datetime.fromtimestamp(interval)
        else:
            interval = 6000
            dayOrNight = "白天"
            intervalDate = datetime.datetime.fromtimestamp(interval)
    else:
        interval = interval-1
        intervalDate = datetime.datetime.fromtimestamp(interval)
    # intervalDate = datetime.datetime.fromtimestamp(interval)

#刷新界面上时间显示
def refreshTime():
    global timeM
    global intervalDate
    readTimeJSON()
    timeM["text"] = intervalDate.strftime("%H:%M:%S")+dayOrNight
    win.after(1000, refreshTime)

#解析JSON，初始化数据
def initJSON():
    text = getURL.getRestMsg()
    interval = int(text['cetus']['cetusTime']) - int(text['time'])
    print("时间差值为")
    print(interval)
    if text['cetus']['day'] == "True":
        dayOrNight = "白天"
    else:
        dayOrNight = "夜晚"