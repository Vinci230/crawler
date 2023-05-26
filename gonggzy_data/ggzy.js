const crypto = require("crypto-js")
var MD5 = require('md5.js')


let t={ts: 1684844032188, type: '12', IS_IMPORT: 1, pageSize: 3}
function s(n) {
                        return new MD5(!0).update(n).digest("hex")
                    }


function u(t, e) {
            return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
        }
//console.log(s("3637CB36B2E54A72A7002978D0506CDFIS_IMPORT1pageSize3ts1684844032188type12"))
 function l(t) {
            for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
                if (void 0 !== t[e[a]])
                    if (t[e[a]] && t[e[a]]instanceof Object || t[e[a]]instanceof Array) {
                        var i = JSON.stringify(t[e[a]]);
                        n += e[a] + i
                    } else
                        n += e[a] + t[e[a]];
            return n
        }
function d(t) {
            for (var e in t)
                "" !== t[e] && void 0 !== t[e] || delete t[e];
            var n = '3637CB36B2E54A72A7002978D0506CDF' + l(t);
            return s(n).toLocaleLowerCase()
        }


function b(t) {
            var e = crypto.enc.Utf8.parse('BE45D593014E4A4EB4449737660876CE')
              , n = crypto.enc.Utf8.parse('A8909931867B0425')
              , a = crypto.AES.decrypt(t, e, {
                iv: n,
                mode: crypto.mode.CBC,
                padding: crypto.pad.Pkcs7
            });
            return a.toString(crypto.enc.Utf8)
        }

console.log(d({
    "ts": 1684845416020,
    "pageNo": 1,
    "pageSize": 20,
    "total": 0,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "1",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2022-11-23 00:00:00",
    "EndTime": "2023-05-23 23:59:59",
    "createTime": []
}))
