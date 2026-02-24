'''
-*- Coding: utf-8 -*-
Date: 2026-02-24 09:20:47
Author: Jim
LastEditTime: 2026-02-24 09:57:16
LastEditors: Do not edit
'''
import requests
import json
import execjs
cookies = {
    "webapp": "1",
    "siteCode": "sxzfcg",
    "siteGuid": "6883226032309207040",
    "regioncode": "140001000",
    "regionguid": "140001",
    "theme": "default",
    "regionpguid": "232",
    "rootregionguid": "232",
    "isOpenArea": "true",
    "regionname": "%E7%9C%81%E6%9C%AC%E7%BA%A7"
}
exj_obj = execjs.compile(open('./采购.js', 'r', encoding= 'utf-8').read())
url = "https://shanxisheng-zfcgdzmcgov.cn/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList"
for page in range(1, 6):
    exj = exj_obj.call('encrypt')
    print('获取参数', exj)
    headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "form-token": "fd04b8ea5de13014d95938c4252ba48d",
    "nsssjss": exj['nsssjss'],
    "origin": "https://shanxisheng-zfcgdzmcgov.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://shanxisheng-zfcgdzmcgov.cn/gpmall-main-web/basic/sxNotice",
    "regioncode": "140001000",
    "regionguid": "140001",
    "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sign": exj['sign'],
    "sitecode": "sxzfcg",
    "siteguid": "6883226032309207040",
    "time": str(exj['time']),
    "timestamp": str(exj['timestamp']),
    "url": "/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "webapp": "1"
    }
    data = {
        "regionGuid": "232",
        "regionCode": "140000000",
        "webApp": "1",
        "pageSize": 10,
        "pageNum": page,
        "noticeType": "0"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data, cookies=cookies).json()
    print(response)