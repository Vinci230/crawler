
import execjs
import re
import requests
#url='https://fanyi.baidu.com/v2transapi?from=zh&to=en'
cookies = {
    'BAIDUID': '4A4DBC0DE98640E6542D838E2BA01749:FG=1',
    'BAIDUID_BFESS': '4A4DBC0DE98640E6542D838E2BA01749:FG=1',
    'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1686141249',
    'REALTIME_TRANS_SWITCH': '1',
    'FANYI_WORD_SWITCH': '1',
    'HISTORY_SWITCH': '1',
    'SOUND_SPD_SWITCH': '1',
    'SOUND_PREFER_SWITCH': '1',
    'ab_sr': '1.0.1_MGM1OWYyNjkxMmZmOWUzZTI1M2U0ZGY4OTc1YjAxYTE0ZTY0MTM4ZDU2NDJlOTU1MmU0Y2Q5OTFiNjUwMmRkMTUyNTg2MjlhYWNlM2E5NGEzOGI2ODY3MjNjYTE2N2Q3ZWI1M2E5ZDgxZjIyYjBlYWNmNjVmM2Q4YmZlZTJhODFkMTRlMzM2YTRiM2NiZDI2NWZjNDExYmVmOTE5OWJjZQ==',
    'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1686223879',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Acs-Token': '1686223877644_1686223879966_c2qreB5AEYGT/9sGnI9L5zL7cMCcNP2N/rgAtZ+LBSdFAunSJ+B3t2cOKOlB/jTWJ9Udczj1akxNFv22E8EqZh2BuVJGBzalUyXdfaQgaGeEHpiOydQGKH0wOKzf+zeMvaIu+3Lu25tCfI2fzu5PXLV1Ar9nU4Qxd6tkY07mZLYfDZDfZrQkE1JlR2WLTE73bTApgIkOrNZkqIhUUfg2n/r5EA6wTHp7Sukh6ZJtnxiV0KGxf3FluoGmkFEradM/RyoQ8YLd8sGmtoyX35Yf82RwW+UzoEq6IxwttC709u7iGXJLrPRPd/hKDxogq3/m+mYHnE44qmM8+WJ8H72ToOKXRdhNd0T47O4WqSCxX4+zhxkDG2VDVqf4vUMVxpZ8cZiAgB1CEXAJM+cSDzzpXR3HnKdwXe0hGLazwvvH+zwS++G8ko19Hy7mUNOg4Sae4DXFHDhrogdwkort57/hA7rGEmwGjfRQhyI//sA17Jic2q512Ayu44ufpiNXCrKQ',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'BAIDUID=4A4DBC0DE98640E6542D838E2BA01749:FG=1; BAIDUID_BFESS=4A4DBC0DE98640E6542D838E2BA01749:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1686141249; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_MGM1OWYyNjkxMmZmOWUzZTI1M2U0ZGY4OTc1YjAxYTE0ZTY0MTM4ZDU2NDJlOTU1MmU0Y2Q5OTFiNjUwMmRkMTUyNTg2MjlhYWNlM2E5NGEzOGI2ODY3MjNjYTE2N2Q3ZWI1M2E5ZDgxZjIyYjBlYWNmNjVmM2Q4YmZlZTJhODFkMTRlMzM2YTRiM2NiZDI2NWZjNDExYmVmOTE5OWJjZQ==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1686223879',
    'Origin': 'https://fanyi.baidu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://fanyi.baidu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'from': 'zh',
    'to': 'en',
}
query=input('请输入需要翻译文字：')
sign=execjs.compile(open("bdfy.js",'r',encoding='utf-8').read()).call("w",query)
resp = requests.post('https://fanyi.baidu.com/langdetect', cookies=cookies, headers=headers, data={'query':query})
lang=resp.json()["lan"]
data = {
    'from': lang,
    'to': 'en',
    'query': query,
    'simple_means_flag': '3',
    'sign': sign,
    'token': '133d097bb18348cc59078e2253c9fc59',
    'domain': 'common',
    'ts': '1686223879951',
}

# resp=requests.get(url=url, headers=headers).text
# print(resp)
#token=re.findall(r"token: ", resp)[0]
#print(token)

response = requests.post('https://fanyi.baidu.com/v2transapi', params=params, cookies=cookies, headers=headers, data=data)
print(response.json()['trans_result']['data'][0]['dst'])







