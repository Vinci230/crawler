import requests
import execjs
ctx=execjs.compile(open("hhc.js",'r',encoding="utf-8").read())
cookies = {
    'UM_distinctid': '18855a477fc17-08bbf21c43129-26031a51-13c680-18855a477fd1337',
    'Hm_lvt_1521e0fb49013136e79181f2888214a7': '1685064023,1685277575',
    'Hm_lpvt_1521e0fb49013136e79181f2888214a7': '1685277575',
    'JSESSIONID': 'FCB0EB73CEEF8D533B8F455788F96E59',
    '_ACCOUNT_': 'OGE3ZWM3YjE0Yzc2NGMzOWI1YWFlYTk1MWFhYWFjYTMlNDAlNDBtb2JpbGU6MTY4NjQ4NzQyMzQ2MjplNzQ3OGY3OTYyMjQwMjczY2EyMTg5ZGE0M2FmMzdiNQ',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Auth-Plus': '',
    'Connection': 'keep-alive',
    # 'Cookie': 'UM_distinctid=18855a477fc17-08bbf21c43129-26031a51-13c680-18855a477fd1337; Hm_lvt_1521e0fb49013136e79181f2888214a7=1685064023,1685277575; Hm_lpvt_1521e0fb49013136e79181f2888214a7=1685277575; JSESSIONID=FCB0EB73CEEF8D533B8F455788F96E59; _ACCOUNT_=OGE3ZWM3YjE0Yzc2NGMzOWI1YWFlYTk1MWFhYWFjYTMlNDAlNDBtb2JpbGU6MTY4NjQ4NzQyMzQ2MjplNzQ3OGY3OTYyMjQwMjczY2EyMTg5ZGE0M2FmMzdiNQ',
    'Origin': 'https://www.hanghangcha.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'clientInfo': 'web',
    'clientVersion': '1.0.0',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'filter': '{"limit":3,"skip":0,"tagId":null}',
}

response = requests.get('https://api.hanghangcha.com/hhc/industry/getReportList', params=params, cookies=cookies, headers=headers)
print(response.text)
print(ctx.call("decrypt",response.json()["data"]))