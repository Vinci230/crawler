const node_rsa=require("node-rsa")
const PublicKey  = "-----BEGIN PUBLIC KEY-----\nMFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAMz4u0O0AI4TfvilTlJxQedoZgA8NuEC\nM/N16k3Pb2mObSpPGDIYdkqm1w3mjUGqK+Sld0Za2JEGAHrN1w+VvVECAwEAAQ==\n-----END PUBLIC KEY-----\n"

const key = new node_rsa()
key.importKey(PublicKey,'pkcs8-public-pem')
let h2e =  new TextEncoder
user="thy"
pass="123"
function ka(e) {
   key.getKeySize();
        const t = key.encrypt(e,"base64")
          ,  n = h2e.encode(t);
        return Array.from(new Uint8Array(n)).map(o=>o.toString(16).padStart(2, "0")).join("")
    }

console.log(ka(user))
console.log(ka(pass))