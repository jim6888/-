'''
-*- Coding: utf-8 -*-
Date: 2026-02-22 03:57:25
Author: Jim
LastEditTime: 2026-02-22 03:57:38
LastEditors: Do not edit
'''
import requests
import json
import time
import execjs
exj_obj = execjs.compile(open('./福建公共.js', 'r', encoding='utf8').read())
for page in range(1, 6):
    data = {
        "pageNo": page,
        "pageSize": 10,
        "total": 728,
        "type": "11",
        "timeType": "0",
        "ts": int(time.time() * 1000),
    }
    exj = exj_obj.call('encrypt', data)

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://ggzyfw.fj.gov.cn",
        "Pragma": "no-cache",
        "Referer": "https://ggzyfw.fj.gov.cn/index/newList/?type=11",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "portal-sign": exj,
        "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    url = "https://ggzyfw.fj.gov.cn/FwPortalApi/Article/PageList"
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, data=data).json()
    res = exj_obj.call('decrypt_data', response['Data'])
    print(res)