import requests
import execjs
import re
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://app.diandian.com",
    "Pragma": "no-cache",
    "Referer": "https://app.diandian.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "language": "zh",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
   #需要添加cookies
}
encrypt_url = 'https://app.diandian.com/'
url = "https://api.diandian.com/pc/app/v2/user/favorite"
params = {
    "market_id": "",
    "sub_type": "1",
    "is_detail": "0",
    "is_go_sea": "0",
    "country_id": "",
}
try:
    response = requests.get(encrypt_url, headers=headers, cookies=cookies).text
    data = re.findall('pageLoading:f,u:{s:"(.*?)",k:"(.*?)",l:"(.*?)",d:d',response)[0]
    print('获取加密参数s:',data[0])
    print('获取加密参数k:',data[1])
    print('获取加密参数l:',data[2])
except Exception as e:
    print('未找到加密参数,程序结束')
    exit()
exj = execjs.compile(open('./点点网.js', 'r', encoding= 'utf-8').read()).call('encrypt', params, data[0], data[1], data[2])
print('获取请求参数:',exj)
response = requests.get(url, headers=headers, cookies=cookies, params=exj)
print(response.text)



