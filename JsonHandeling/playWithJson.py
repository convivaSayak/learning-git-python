import json

json_string='''{"t":"CwsSessionHb","cid":"96c68c5242c705150b56c7162f122ebdd8cfd756","clid":"3307534992.1680532383.739284817.4172364447","sid":1960184409,"seq":14,"pver":"2.1","iid":0,"sf":1,"st":1800001,"sst":302135679,"vid":"metadatadrop","caps":4,"pm":{"sch":"silverlight.3","bp":"MacIntel","rv":"5.0.61118.0"},"ptv":"1.8","tags":{"kind":"SmoothStreaming","tagAction":"echo","throttle":"true","goResponse":"true"},"an":"http://trona.sql1.corp.conviva.com/Bunny/BigBuckBunny.ism/manifest","evs":[{"t":"CwsCustomEvent","name":"AdFinished","st":2300,"seq":11,"bl":5000,"pht":10000,"attr":{"adId":"expensiveAd.123","adDurationSec":"35.0"}}],"fw":"OSMF","fwv":"1.8","pn":"abc","ct":"abc","cc":{"abc":"123"},"strmetadata":{"pn":"new player name","vid":"newviewerId"},"rs":"abc","url":"http://a.b.com/v4/USUV71102122.ism/manifest","csi":"1.1.1.1","ssid":"wifiname","le":"WEP","ati":"Apple IDFA","ss":"80","w":2,"h":2,"cdn":"abc"}'''

data=json.loads(json_string)
print(type(data))

for value in data["evs"]:
    print(value['attr']['adId'])