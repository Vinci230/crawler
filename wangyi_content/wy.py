import json

import execjs

import requests
from pprint import pprint

cookies = {
    'NMTID': '00O8fhiTHDrkdIJOU8KogP5Xvsb2o4AAAGHRIrmGQ',
    'MUSIC_U': '7cb34d114d36452c51e01d109ee58bc51469e28510b16db5e9af7de524f1ca51993166e004087dd39969ae1ab35f21cad4d620df9fa3cdbb7441af76c832aa4904ab2fa87b508160a0d2166338885bd7',
    'WM_TID': '%2Fqv2WLcdZ31AFAFFFEaAP3EQOl70eCna',
    '_ntes_nnid': 'd4995debe9d9d9c7c1b180fe921e53fa,1680529815325',
    '_ntes_nuid': 'd4995debe9d9d9c7c1b180fe921e53fa',
    'WEVNSM': '1.0.0',
    'WNMCID': 'fhdzto.1680529815480.01.0',
    'ntes_kaola_ad': '1',
    '__csrf': '154c4129b78f478464f1a79022ab11d5',
    'JSESSIONID-WYYY': 'ufuXmIM7VcFQ41G34th%5C6F0xblEFKEfFCOuYlk10ldY4r%2BN3CrDmSXy6pNGNJSNqBg4VW5%2F49yU7Zn9tRV6prpEjngnQZjFBnh96cPuAkRqjqp%2BtKTX01giO8%2F62jSl3pG9K7F28NXmaDPm63fY%2BtNYWfynIbBhpJc%5CN%2F%2BCoNuIAvuNF%3A1684392120709',
    '_iuqxldmzr_': '33',
    'WM_NI': '6bLL2GLxNjw69%2Bqgfkse70OaGqTS2mMAaWx7C5q4zFJyPeGl1Ylwkko%2BPJsjw96yUxbQD63C3GQIHg67Jfh8%2BjuvW2YUf93ZRM1kQEe7ALW4B45GMtzkZDXXIq0tEWT3TGw%3D',
    'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee95bc63e9948bb0dc4a8c9a8eb2c54b929b9eb0d56893b7b686b54988b3a2a8d22af0fea7c3b92af6be84adb14d90a8828bf63efbf5bf88e561b1bbf9d1ce6b85af9cb4b1678f9fafb8fb3d81ebbfd5f94e8aa7a086c668f387a498ea61adf5a0abf262b5e7fa9ad874a28f8cd7b249f1999faacb6df6e98687eb34e9b6bb97d63a9b8baadab2529293ff8cd44fa7e98fadd64082ecfba8d080bab596a5db548baf0095c85d98ed9ca8f637e2a3',
    'sDeviceId': 'YD-8a/OZ4a2eLpBQ0VAVUbEfDaAmroXiwiC',
    'ntes_utid': 'tid._.6f%252BeFFfSX5NEVhURUUeE0Bnzf%252FWGofqI._.0',
}

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'NMTID=00O8fhiTHDrkdIJOU8KogP5Xvsb2o4AAAGHRIrmGQ; MUSIC_U=7cb34d114d36452c51e01d109ee58bc51469e28510b16db5e9af7de524f1ca51993166e004087dd39969ae1ab35f21cad4d620df9fa3cdbb7441af76c832aa4904ab2fa87b508160a0d2166338885bd7; WM_TID=%2Fqv2WLcdZ31AFAFFFEaAP3EQOl70eCna; _ntes_nnid=d4995debe9d9d9c7c1b180fe921e53fa,1680529815325; _ntes_nuid=d4995debe9d9d9c7c1b180fe921e53fa; WEVNSM=1.0.0; WNMCID=fhdzto.1680529815480.01.0; ntes_kaola_ad=1; __csrf=154c4129b78f478464f1a79022ab11d5; JSESSIONID-WYYY=ufuXmIM7VcFQ41G34th%5C6F0xblEFKEfFCOuYlk10ldY4r%2BN3CrDmSXy6pNGNJSNqBg4VW5%2F49yU7Zn9tRV6prpEjngnQZjFBnh96cPuAkRqjqp%2BtKTX01giO8%2F62jSl3pG9K7F28NXmaDPm63fY%2BtNYWfynIbBhpJc%5CN%2F%2BCoNuIAvuNF%3A1684392120709; _iuqxldmzr_=33; WM_NI=6bLL2GLxNjw69%2Bqgfkse70OaGqTS2mMAaWx7C5q4zFJyPeGl1Ylwkko%2BPJsjw96yUxbQD63C3GQIHg67Jfh8%2BjuvW2YUf93ZRM1kQEe7ALW4B45GMtzkZDXXIq0tEWT3TGw%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee95bc63e9948bb0dc4a8c9a8eb2c54b929b9eb0d56893b7b686b54988b3a2a8d22af0fea7c3b92af6be84adb14d90a8828bf63efbf5bf88e561b1bbf9d1ce6b85af9cb4b1678f9fafb8fb3d81ebbfd5f94e8aa7a086c668f387a498ea61adf5a0abf262b5e7fa9ad874a28f8cd7b249f1999faacb6df6e98687eb34e9b6bb97d63a9b8baadab2529293ff8cd44fa7e98fadd64082ecfba8d080bab596a5db548baf0095c85d98ed9ca8f637e2a3; sDeviceId=YD-8a/OZ4a2eLpBQ0VAVUbEfDaAmroXiwiC; ntes_utid=tid._.6f%252BeFFfSX5NEVhURUUeE0Bnzf%252FWGofqI._.0',
    'nm-gcore-status': '1',
    'origin': 'https://music.163.com',
    'pragma': 'no-cache',
    'referer': 'https://music.163.com/song?id=1876909269',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '154c4129b78f478464f1a79022ab11d5',
}

i2x = {
    "rid": "R_SO_4_1876909269",
    "threadId": "R_SO_4_1876909269",
    "pageNo": "3",
    "pageSize": "20",
    "cursor": "1683020186913",
    "offset": "0",
    "orderType": "1",
    "csrf_token": "154c4129b78f478464f1a79022ab11d5"
}

data=execjs.compile(open("wy.js","r",encoding="utf-8").read()).call("main")

# data = 'params=%2Bp4QZ7UmhNrCL%2FW9uEnF%2FUa4ae%2F3w5l1ky1NkMhFfYOIBMbGs0dX%2BHLzdoq0NCdA5AMp%2Fz%2BzxFNi39IwFRrV5SCORH8sVWn9qXGX54bKXcoedvTcL%2FrhgTDVS%2F3LflDgaQ9IEALe32B6wmbFKefJBqKv2Mm2Sks3MSq9En8XvrSYVGfHMr%2B8p6loVle081mqsiltH6tSjqYK0287WXnUJwKjg6qUPP%2BX1toujKyCGM0cOQX6leoQwMg%2FwhfpVSm7%2BI7Q09mCcGK3kIvhUlLtCHIJuduLWy7sfm92n%2FJOyOeYHfYz9Bi1RxaEwSiBsPRMPtTnWqeUzn2kMtiHsuDhos%2B9Ki31kTtsZ8sJMEWjxWE%3D&encSecKey=a50b221d5e4f8be7460461fa3ed9732acf525dac37a593cfd0e65908fcc23bc6adab09d4781844a031968d94a8d0d9121d807d14d605acd3a8b1839f14b06f8bffd254933179f131188e09e194647d3f1873b849ab25a1d6c6b51a325e81c4bc74f23a7c211328771cadd7a5afecf97115512309677f4b0e056883ad1c17f4af'


response = requests.post(
    'https://music.163.com/weapi/comment/resource/comments/get',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

pprint(json.loads(response.text))
response.close()

