import requests

url = "http://fanyi.baidu.com/basetrans"

data = {"query": "你好，世界","from": "zh","to": "en"}

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
           "Referer": "http://fanyi.baidu.com/translate"}


response = requests.post(url,data=data,headers = headers)
# print(response.text)

print(response)
print(response.content.decode())