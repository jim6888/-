
var crypto_js = require("crypto-js")

// 返回解密
function decrypt_data(t) {
    var e = crypto_js.enc.Utf8.parse('EB444973714E4A40876CE66BE45D5930')
        , n = crypto_js.enc.Utf8.parse('B5A8904209931867')
        , a = crypto_js.AES.decrypt(t, e, {
        iv: n,
        mode: crypto_js.mode.CBC,
        padding: crypto_js.pad.Pkcs7
    });
    return a.toString(crypto_js.enc.Utf8)
}

// var data = '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'
//
// console.log(decrypt_data(data))
function l(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}

function u(t) {
    for (var e = Object.keys(t).sort(l), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function encrypt(parms) {
    var n = 'B3978D054A72A7002063637CCDF6B2E5' + u(parms)
    console.log(n)
    return crypto_js.MD5(n).toString()
}
