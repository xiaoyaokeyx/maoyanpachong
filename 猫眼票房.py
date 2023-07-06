import hashlib
import math
import random
import time
import execjs
import requests

js1 = open('./test.js', 'r', encoding='utf-8').read()
ctx = execjs.compile(js1).call('params')


def getIndex():
    return math.floor(1000 * random.random() + 1)
index = getIndex()
timestemp = int(time.time() * 1000)
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Cookie': '_lxsdk_cuid=1891478d670c8-027adc931d3b7f-1b525634-1fa400-1891478d670c8; _lxsdk=1891478d670c8-027adc931d3b7f-1b525634-1fa400-1891478d670c8; uuid=1891478d670c8-027adc931d3b7f-1b525634-1fa400-1891478d670c8; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=1892b40f778-768-dfb-efd%7C%7C12',
    'Uid': '636634cdd97f51ae2563ee144069ff090bf13f20',
    'Referer': 'https://piaofang.maoyan.com/box-office?ver=normal&requestCode=010b28454fc07ad2d25b98fc2f593a3adxj3d'
}
d = 'method=GET&timeStamp=' + str(timestemp) + '&User-Agent=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLa' \
    'XQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2&index=' \
    + str(index) + '&channelId=40009&sVersion=2&key=A013F70DB97834C0A5492378BD76C53A'
print(d)

def getSignKey(d):
    md5 = hashlib.md5()
    md5.update(d.encode('utf-8'))
    ctx = md5.hexdigest()
    return ctx
ctx = getSignKey(d)
url = "https://piaofang.maoyan.com/i/api/getBoxList"
payloads = {
    'date': 1,
    'isSplit': 'true',
    'timeStamp': timestemp,
    'User-Agent': 'TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2',
    'index': index,
    'channelId': 40009,
    'sVersion': '2',
    'signKey': ctx,
}
resp = requests.get(url=url, headers=header, params=payloads)
print(resp.json())
for i in resp.json()['boxOffice']['data']['list']:
    print(i['movieInfo']['movieName'] + ':' '票房' + i['sumBoxDesc'])
