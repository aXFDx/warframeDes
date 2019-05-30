#-*- conding:utf-8 -*-
import requests

def getRestMsg():
    url = 'https://api.null00.com/world/ZHCN'
    #response = requests.get(url)
    #data = response.json()['alerts']
    #print(data)
    data = '{"cetus":{"oid":"5cef60f99aa9ed1999db8378Ostrons","activation":1559191801,"expiry":1559200742,"cetusTime":1559197742,"day":true}}'
    print(data)
    return data

