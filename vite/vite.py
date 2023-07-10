import requests
import execjs
# cookies = {
#     'isLogin': '4a6f577a34422f2b712b4d7458434e3453574e57333279336477716354334673717148306f327562725768416d7a4d4743434c45474878565763384e46367a352f756e7279586870343839767a4b533530785a4979773d3d',
# }

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    # 'Cookie': 'isLogin=4a6f577a34422f2b712b4d7458434e3453574e57333279336477716354334673717148306f327562725768416d7a4d4743434c45474878565763384e46367a352f756e7279586870343839767a4b533530785a4979773d3d',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://8.130.101.163:8000/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
username="thy"
password="12345"
user=execjs.compile(open("vite.js",'r',encoding='utf-8').read()).call("ka",username)
password=execjs.compile(open("vite.js",'r',encoding='utf-8').read()).call("ka",password)
params={
    'username':user,
    'password':password
}
response = requests.get('http://8.130.101.163:8000/api/login', headers=headers,params=params ,verify=False)
print(params)
print(response.text)
cookies=response.cookies
for cookie in cookies:
    print(cookie.name,cookie.value)