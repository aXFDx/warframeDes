#-*- conding:utf-8 -*-
import requests
import json


def getRestMsg():
    url = 'https://api.null00.com/world/ZHCN'
    #response = requests.get(url)
    #data = response.json()['alerts']
    #print(data)
    data = '{"time":1559271357,"cetus":{"oid":"5cf079fdcddc41bd996aec36Ostrons","activation":1559263741,"expiry":1559272733,"cetusTime":1559272733,"day":false}}'
    text = json.loads(data)
    return text
