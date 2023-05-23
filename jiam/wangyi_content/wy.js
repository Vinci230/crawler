const CryptoJS = require("crypto-js")
const RSA=require("rsa-javascript")

function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")

            //console.log(d)

          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return RSA.setMaxDigits(131),
        d = new RSA.RSAKeyPair(b,"",c),
        e = RSA.encryptedString(d, a)
    }
function d(d, e, f, g) {
        var h = {}
            , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }


let i2x = {
    "rid": "R_SO_4_1876909269",
    "threadId": "R_SO_4_1876909269",
    "pageNo": "3",
    "pageSize": "20",
    "cursor": "1683020186913",
    "offset": "0",
    "orderType": "1",
    "csrf_token": "154c4129b78f478464f1a79022ab11d5"
}

let e='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
let g='0CoJUm6Qyw8W8jud'

function p(gG7z, UP8H, cKV9M) {
        if (!gG7z)
            return "";
        var bx5C = [];
        for (var x in gG7z) {
            bx5C.push(encodeURIComponent(x) + "=" + (!!cKV9M ? encodeURIComponent(gG7z[x]) : gG7z[x]))
        }
        return bx5C.join(UP8H || ",")
    }

    bMs6m = d(JSON.stringify(i2x),'010001',e,g)

function main(){
    return p({ params: bMs6m.encText,
                encSecKey: bMs6m.encSecKey},"&",!0)
}

//hhhjjjhhh
//找到加密参数的过程
//1.找到所需例如评论的所在网址
// 2.在该网址里找到加密参数所在位置的js
// 3.要保证该js的位置在本地下显示是是在该网址下
// 4.加密参数找到被加密位置后打断点开始调试，找到加密函数的原函数
// 5.找到原函数的参数，在控制台下打印输出参数固定值
// 6.可能需要进行导包，在npm进行搜索，如果为python的形式修改修改

