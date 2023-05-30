//  let n='4e87183cfd3a45fe'
//  let r=undefined
//  let i=undefined
// let e=undefined
//  function t(t) {
//                             return "string" == typeof t
//                         }
// function enc(n, r, i) {
//     return t(r).encrypt(e, n, r, i)
//                                 }
//
//  console.log(enc(n,r,i))


const  a = require("crypto-js")

let n = "4e87183cfd3a45fe"

function s(t) {
            var e = {
                mode: a.mode.ECB,
                padding: a.pad.Pkcs7
            }
              , i = a.enc.Utf8.parse(n)
              , s = a.AES.encrypt(t, i, e)
              , r = s.toString().replace(/\//g, "_");
            return r = r.replace(/\+/g, "-"),
            r
        }

console.log(s("李恩熙是猪"))