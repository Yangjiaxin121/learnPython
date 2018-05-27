

import requests


url = "http://www.renren.com/327550029/profile"

headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

cookie ="anonymid=jh0g38g5jb779t; depovince=GW; jebecookies=b117d25a-c2a4-4987-bc1c-3c8f1d1b26e0|||||; _r01_=1; JSESSIONID=abcWK0rZ67kGThGeZYjnw; ick_login=f1ba6f68-73e5-482c-8ef1-d960e922d028; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=4090c4309a6b288ae2ea49c06092304c9; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20180415/1020/main_rHkm_0aac00000249195a.jpg; t=e62069a23c60999dc710dfb4132a909b9; societyguester=e62069a23c60999dc710dfb4132a909b9; id=327550029; xnsid=b63283da; loginfrom=syshome; ch_id=10016; jebe_key=8ae6b14d-07ca-4a29-9d0f-01925634f844%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1525951596319%7C1%7C1525951597537; wp_fold=0; _ga=GA1.2.1056336974.1525952114; _gid=GA1.2.1478191220.1525952114; _gat=1"


cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}
print(cookie_dict)

with open("renren1.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())
