

from lxml import etree


import requests


url = "https://movie.douban.com/chart"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36unit"}

response = requests.get(url,headers = headers)
html_str = response.content.decode()


# print(html_str)

#使用entree处理数据

html = etree.HTML(html_str)
# print(html)

#1.获取所有的电影的URL地址

url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")

# print(url_list)

#2.所有图片的地址
img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")

# print(img_list)

#3.需要把每部电影组成一个字典，字典中是电影的数据，比如标题、url，评分、图片地址、评论数、评分
#思路
    #1.分组
    #2.每一组提取数据
ret1 = html.xpath("//div[@class='indent']/div/table")

# print(ret1)
for table in ret1:
    item = {}
    item["title"] = table.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    item["href"] = table.xpath(".//a[@class='nbg']/@href")
    item["img"] = table.xpath(".//a[@class='nbg']/img/@src")
    item["comment_num"] = table.xpath(".//span[@class='pl']/text()")
    item["rating_num"] = table.xpath(".//span[@class='rating_nums']/text()")

    print(item)