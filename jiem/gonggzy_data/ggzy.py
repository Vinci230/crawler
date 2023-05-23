import time

import execjs

import requests

ctx = execjs.compile(open("ggzy.js", "r").read())

date = round(time.time() * 1000)

json_data = {
    'pageNo': 1,
    'pageSize': 20,
    'total': 0,
    'AREACODE': '',
    'M_PROJECT_TYPE': '',
    'KIND': 'GCJS',
    'GGTYPE': '1',
    'PROTYPE': '',
    'timeType': '6',
    'BeginTime': '2022-11-23 00:00:00',
    'EndTime': '2023-05-23 23:59:59',
    'createTime': [],
    'ts': date,
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ggzyfw.fujian.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://ggzyfw.fujian.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'portal-sign': ctx.call("d",json_data),
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



response = requests.post('https://ggzyfw.fujian.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, json=json_data)
print(headers['portal-sign'])

print(response.text)


print(ctx.call("b",response.json()["Data"]))


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"pageNo":1,"pageSize":20,"total":0,"AREACODE":"","M_PROJECT_TYPE":"","KIND":"GCJS","GGTYPE":"1","PROTYPE":"","timeType":"6","BeginTime":"2022-11-21 00:00:00","EndTime":"2023-05-21 23:59:59","createTime":[],"ts":1684674757813}'
#response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', headers=headers, data=data)