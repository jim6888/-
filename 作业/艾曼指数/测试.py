import requests
import execjs
exj_obj= execjs.compile(open('./艾曼指数.js', 'r', encoding='utf-8').read())
while True:
    print('请输入要查询的关键字,输入exit退出:')
    user = str(input())
    if user != 'exit':
        exj = exj_obj.call('encrypt', user)
        print('获取加密的值:', exj)
        headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Referer": "https://www.chinaindex.net/search",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "UUID": exj['uuid'],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "funcID": "2614",
        "incognitoMode": "0",
        "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://www.chinaindex.net/iIndexMobileServer/mobile/comm/getSearchResult"
        params = {
            "keyWord": exj['keyWord'],
            "sign": exj['sign'],
        }
        response = requests.get(url, headers=headers,  params=params).json()
        print('开始解密数据')
        res = execjs.compile(open('./艾曼指数.js', 'r', encoding='utf-8').read()).call('decrypt_data', response)
        print('解密后的数据:', res)
    else:
        break
