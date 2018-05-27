import requests
from retrying import retry

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Referer": "https://m.douban.com/movie/doubantop"}



@retry(stop_max_attempt_number = 3)
def _parse_url(url):
    print("*"*100)
    response = requests.get(url,headers = headers,timeout = 5)
    return response.content.decode()

def parse_url(url):
    try:
        html_url = _parse_url(url)
    except:
        html_url = None

    return html_url




