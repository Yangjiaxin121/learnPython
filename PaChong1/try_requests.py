import requests

url = "http://www.baidu.com/"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}



response = requests.get(url,headers =headers)


# response.encoding = "utf-8"
#
# print(response.text)

# print(response.content.decode())
print(response.url)
print(response.request.url)
print(response.headers)
print(response.request.headers)
