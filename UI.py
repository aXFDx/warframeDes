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
global jsonText
global timeM, warnM
warnmsg = ""

#UI展示主界面
def showUI():
    global interval, dayOrNight
    win.title("迷你奥迪斯")
    win.geometry("300x400")
    win.resizable(width=False, height=True)
    #初始化信息
    initJSON()
    #设置平原时间界面
    global timeM
    timeT = Label(win, text="平原时间", font=("Arial", 12), width=10, height=2)
    timeT.pack(side=TOP)
    timeM = Label(win, text="初始化中...", font=("Arial", 12), width=20, height=2)
    timeM.pack(side=TOP)
    #设置警报界面
    global warnM
    warnT = Label(win, text="警报", font=("Arial", 12), width=10, height=2)
    warnT.pack(side=TOP)
    warnmsg = "初始化中..."
    warnM = Message(win, text=warnmsg)
    warnM.config(font=("Arial", 12))
    warnM.pack()
    # #初始化信息
    # initJSON()
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
            # intervalDate = datetime.datetime.fromtimestamp(interval)
            # m, s = divmod(interval, 60)
            # h, m = divmod(m, 60)
            # intervalDate = str(h)+":"+str(m)+":"+str(s)
            # # print(intervalDate)
            intervalDate = showHMS(interval)
        else:
            interval = 6000
            dayOrNight = "白天"
            # intervalDate = datetime.datetime.fromtimestamp(interval)
            # m, s = divmod(interval, 60)
            # h, m = divmod(m, 60)
            # intervalDate = str(h)+":"+str(m)+":"+str(s)
            # print(intervalDate)
            intervalDate = showHMS(interval)
    else:
        interval = interval-1
        # intervalDate = datetime.datetime.fromtimestamp(interval)
        # print(interval)
        # m, s = divmod(interval, 60)
        # h, m = divmod(m, 60)
        # intervalDate = str(h)+":"+str(m)+":"+str(s)
        # print(h, m, s)
        # print(intervalDate)
        intervalDate = showHMS(interval)
    # intervalDate = datetime.datetime.fromtimestamp(interval)

#刷新界面上时间显示
def refreshTime():
    global timeM
    global warnM
    global intervalDate
    global dayOrNight
    readTimeJSON()
    readWarnJSON()
    # timeM["text"] = intervalDate.strftime("%H:%M:%S")+dayOrNight
    # timeM["text"] = str(intervalDate)+dayOrNight
    timeM["text"] = intervalDate+dayOrNight
    warnM["text"] = warnmsg
    win.after(1000, refreshTime)

#解析JSON，初始化数据
def initJSON():
    global interval
    global dayOrNight
    global jsonText
    jsonText = getURL.getRestMsg()
    interval = int(jsonText['cetus']['cetusTime']) - int(jsonText['time'])
    print("时间差值为")
    print(interval)
    if jsonText['cetus']['day'] == "True":
        dayOrNight = "白天"
    else:
        dayOrNight = "夜晚"
    readWarnJSON()

# def showHMS():
#     global interval
#     global intervalDate
#     m, s = divmod(interval, 60)
#     h, m = divmod(m, 60)
#     intervalDate = str(h)+":"+str(m)+":"+str(s)


def showHMS(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    hms = str(h)+":"+str(m)+":"+str(s)
    return hms


#处理时间数据
def readWarnJSON():
    global jsonText
    global warnmsg
    warnmsg = "内容   剩余时间\n"
    for warnstr in jsonText['alerts']:
        if len(warnstr['rewards']) != 0:
            warnmsg = warnmsg + warnstr['rewards'][0]['item'] + "   " + str(warnstr['activation']) + "\n"
            warnstr['activation'] = warnstr['activation'] - 1000
        else :
            warnmsg = warnmsg + "只有钱" + "   " + str(warnstr['activation']) + "\n"
            warnstr['activation'] = warnstr['activation'] - 1000


