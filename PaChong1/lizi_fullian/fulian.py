from lxml import etree
import requests
import json



class FuLian:

    def __init__(self):
        self.url = "https://www.zhihu.com/question/29556265"
        #self.url = "https://www.zhihu.com/question/50333203"
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36unit"}

    def parse_url(self,url1):
        response = requests.get(url1,headers = self.headers)
        html_str = response.content.decode()
        print(html_str)
        return html_str


    def get_content(self,html_str):
        html = etree.HTML(html_str)
        #1.分组
        div_list = html.xpath("//div[@class='List-item']")
        print(div_list)

        content_list = []
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//meta[@itemprop='name']/@content")
            item["img"] = div.xpath(".//meta[@itemprop='image']/@content")
            item["content"] = div.xpath(".//div[@class='RichContent-inner']/span[@class='RichText CopyrightRichText-richText']/p/text()")
            item["content"] = [i.strip() for i in item["content"]]
            item["title"] = div.xpath(".//div[@class='ContentItem AnswerItem']/@data-zop")
            content_list.append(item)
        return content_list


    def save_content_list(self,content_list):
        with open("zhihu.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
            print("保存成功")

    def run(self):  #实现主要逻辑

        #1.构造url地址
        url1 = self.url

        #2.发送请求，获取响应
        html_str = self.parse_url(url1)

        #3.提取数据
        content_list = self.get_content(html_str)

        #4.保存
        self.save_content_list(content_list)


if __name__ == '__main__':
    z = FuLian();
    z.run()