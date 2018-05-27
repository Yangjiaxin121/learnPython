import json
from urllib import request

def fetch_data(url):
    f = request.urlopen(url)
    data = f.read()
    return json.loads(data.decode('utf-8'))

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)