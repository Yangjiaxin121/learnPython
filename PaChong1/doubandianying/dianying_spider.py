

import requests
import json
from doubandianying.dianying_parse import parse_url
# from parse import parse_url

class DianyingSpider(object):

    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_score_hot/items?os=ios&for_mobile=1&start={}&count=18&loc_id=108288&_=1526058303974"

    def get_content_list(self,html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list,total

    def save_content_list(self,content_list):
        with open("dianying.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent = 2))
                f.write("\n")


    def run(self):
        num = 0
        total = 100
        while num < total + 18:
            #1.start_url
            start_url = self.temp_url.format(num)

            #2.发送请求获取响应
            # html_str = parse_url(start_url)
            html_str = parse_url(start_url)
            print(html_str)

            #3.提取数据
            content_list,total = self.get_content_list(html_str)


            #4.保存
            self.save_content_list(content_list)


            #5.循环2到5
            num+=18


if __name__ == '__main__':
    dianying = DianyingSpider()
    dianying.run()


