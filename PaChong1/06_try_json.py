import json

import requests

url = "http://fanyi.baidu.com/basetrans"

str=input("请输入要翻译的内容：")

data = {"query": str,
        "from": "zh",
        "to": "en"}

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "http://fanyi.baidu.com/translate"}


response = requests.post(url,data=data,headers = headers)
# print(response.text)
#
# print(response)
# print(response.content.decode())

html_str = response.content.decode()    #json字符串

dict_ret = json.loads(html_str)

# print(dict_ret)
# print(type(dict_ret))
ret = dict_ret["trans"][0]["dst"]
print("翻译结果为：",ret)

