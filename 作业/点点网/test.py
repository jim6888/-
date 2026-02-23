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
    "deviceid": "435b2270bc9ec351f5dc89faa1d8156",
    "_ga": "GA1.1.825946130.1771030158",
    "token": "a96a4cefad9f74ed7c7afef662c59b04edbd733b95792a5ade6da456f2312510fdb3f467d7c5fef179514d9a4a96c006f5ccb8a70b2fb347f3cb7fee1e7ba36a2ba7fe35d6674b53522e9c198e668fa7",
    "Hm_lvt_4b46d92b8c2be1622e347873de8ada00": "1771780340",
    "Hm_lvt_c420cc498e4250baa6114afe2947045e": "1771780340",
    "Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f": "1771780340",
    "Qs_lvt_404253": "1771030154%2C1771254688%2C1771779254%2C1771832782%2C1771861765",
    "Qs_pv_404253": "3061402436045860400%2C3901205203587188000%2C2715232987739528000%2C3915605962635997700%2C2198456116981729300",
    "_ga_GVCWL6PNZ2": "GS2.1.s1771886495$o12$g1$t1771886512$j43$l0$h0",
    "_uetsid": "1f7e8b80100f11f192d5f7e109203af7|7qnh6w|2|g3t|0|2244",
    "_uetvid": "fe4ef130093e11f1b39b276a5e13532b|1cm4d1l|1771886427044|1|1|bat.bing.com/p/conversions/c/b"
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



