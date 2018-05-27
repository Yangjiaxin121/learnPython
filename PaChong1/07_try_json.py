import json
import requests


url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1525956586077"

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "https://m.douban.com/tv/american"}


response = requests.get(url,headers=headers)
#print(response.content.decode())
json_str = response.content.decode()

ret1 = json.loads(json_str)
# print(ret1)
# print(type(ret1))

with open("douban.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent = 2))
