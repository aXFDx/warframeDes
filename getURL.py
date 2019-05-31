#-*- conding:utf-8 -*-
import requests
import json


def getRestMsg():
    url = 'https://api.null00.com/world/ZHCN'
    #response = requests.get(url)
    #data = response.json()['alerts']
    #print(data)
    data = '{"time":1559271357,"cetus":{"oid":"5cf079fdcddc41bd996aec36Ostrons","activation":1559263741,"expiry":1559272733,"cetusTime":1559272733,"day":false}}'
    # data = '{"time":1559271357,"cetus":{"oid":"5cf079fdcddc41bd996aec36Ostrons", "activation":1559263741,"expiry":1559272733,"cetusTime":1559272733,"day":false},"alerts":[{"oid":"5cf0b14e7143d2fd18fdc5c3","activation":1559278158,"expiry":1559281284,"missionType":"歼灭","faction":"科普斯商会","location":"萨拉西亚(海王星)","minEnemyLevel":30,"maxEnemyLevel":35,"credits":12200,"rewards":[{"id":null,"oid":"5cf0b14e7143d2fd18fdc5c3","item":"150融合点数","itemCount":1,"imageUrl":"/MobileExport/Lotus/Interface/Icons/Store/EndoIconRenderLarge.png","count":false}]},{"oid":"5cf0b5851dd9de2ded8bccaa","activation":1559279253,"expiry":1559281580,"missionType":"生存","faction":"克隆尼帝国","location":"辛西亚(谷神星)","minEnemyLevel":16,"maxEnemyLevel":21,"credits":7100,"rewards":[]},{"oid":"5cf0b81a58b7230ff31779c9","activation":1559279930,"expiry":1559282876,"missionType":"破坏","faction":"科普斯商会","location":"林尼亚(金星)","minEnemyLevel":8,"maxEnemyLevel":10,"credits":4400,"rewards":[{"id":null,"oid":"5cf0b81a58b7230ff31779c9","item":"80融合点数","itemCount":1,"imageUrl":"/MobileExport/Lotus/Interface/Icons/Store/EndoIconRenderLarge.png","count":false}]},{"oid":"5cf0bc522506cc60b20135f5","activation":1559280986,"expiry":1559285419,"missionType":"防御","faction":"克隆尼帝国","location":"卡利班(天王星)","minEnemyLevel":28,"maxEnemyLevel":30,"credits":10700,"rewards":[{"id":null,"oid":"5cf0bc522506cc60b20135f5","item":"工程 系统 设计图","itemCount":1,"imageUrl":"/MobileExport/Lotus/Interface/Icons/Store/GenericWarframeSystem.png","count":false}]}]}'
    text = json.loads(data)
    return text
