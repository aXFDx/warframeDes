import requests

def getads():
    url = 'https://api.null00.com/world/ZHCN'
    response = requests.get(url)
    data = response.json()['alerts']
    print(data)


getads()