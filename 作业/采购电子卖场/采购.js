require('./webpack脚本.js')
var o = '77,73,71,102,77,65,48,71,67,83,113,71,83,73,98,51,68,81,69,66,65,81,85,65,65,52,71,78,65,68,67,66,105,81,75,66,103,81,67,83,50,84,90,68,115,53,43,111,114,76,89,67,76,53,83,115,74,53,52,43,98,80,67,86,115,49,90,81,81,119,80,50,82,111,80,107,70,81,70,50,106,99,84,48,72,110,78,78,84,56,90,111,81,103,74,84,114,71,119,78,105,53,81,78,84,66,68,111,72,67,52,111,74,101,115,65,86,89,101,54,68,111,120,88,83,57,78,108,115,56,87,98,71,69,56,90,78,103,79,67,53,116,86,118,49,87,86,106,121,66,119,55,107,50,120,55,50,67,47,113,106,80,111,121,111,47,107,79,55,84,89,108,54,81,110,117,52,106,113,87,47,73,109,76,111,117,112,47,110,115,74,112,112,85,122,110,70,48,89,103,98,121,85,47,100,70,70,78,66,81,73,68,65,81,65,66'
var i = window.loader("9816")
function p() {
    for (var e = "", t = (arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "").split(","), n = 0; n < t.length; n++)
        e += String.fromCharCode(Number(t[n]));
    return e
}
function w_(e) {
    var t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : p(o)
        , n = new i.a;
    return n.setPublicKey(t),
        n.encrypt(e)
}
function _() {
    return [
        "DgLTzq",
        "mJaYndHWtLPUswC",
        "ntqWmJi4yNnywgD0",
        "mJeXmde0r3LduKnK",
        "z2v0vgLTzq",
        "zgvJB2rL",
        "nti5otCXvwDWwhLn",
        "mtvUt1vKt3a",
        "mZqZnZvLy2DhA0G",
        "mty2oeXWBerwsG",
        "x2jVC3nZB2z0xW",
        "mti2D3rrCLPl",
        "C2LNBG",
        "Dg9Rzw5ZAwDU",
        "mZCYuNn5yxLN",
        "mJuYmdLSt2n4rvu",
        "DxjS",
        "otbUwKfnCvm",
        "nJjgEKXtvKi",
        "C3bSAxq",
        "CgXHDgzVCM1Fma",
        "otuYodu"
    ]
}
function w(e, t) {
    const n = _();
    return w = function (t, i) {
        let r = n[t -= 161];
        void 0 === w.hEWvPs && (w.LvEbrJ = function (e) {
            let t = ""
                , n = "";
            for (let i, r, o = 0, a = 0; r = e.charAt(a++); ~r && (i = o % 4 ? 64 * i + r : r,
                o++ % 4) ? t += String.fromCharCode(255 & i >> (-2 * o & 6)) : 0)
                r = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(r);
            for (let i = 0, r = t.length; i < r; i++)
                n += "%" + ("00" + t.charCodeAt(i).toString(16)).slice(-2);
            return decodeURIComponent(n)
        }
            ,
            e = arguments,
            w.hEWvPs = !0);
        const o = t + n[0]
            , a = e[o];
        return a ? r = a : (r = w.LvEbrJ(r),
            e[o] = r),
            r
    }
        ,
        w(e, t)
}
var b = w
var m = window.loader("6821")
var v = window.loader.n(m)
var g = window.loader("f1dd")
var y = window.loader.n(g);
var x = e => v()(y.a[b(166)](e));
function s_(e, t) {
    const n = w
        , i = (new Date)[n(165)]()
        , r = x(p(i + "_" + String(e)[n(180)]("?")[0] + (n(171) + n(181) + n(182))))
        , o = {};
    if (o[n(161)] = i,
        o[n(177)] = String(e)[n(180)]("?")[0],
        o[n(173)] = r,
        null != t && "" !== t) {
        const r = x(p("" + t + String(e)[n(180)]("?")[0] + i));
        o[n(174)] = r
    }
    return o
}

function encrypt() {
    var url = '/gateway/gpmall-bpoc/notice/v1/ignore/getNoticeList'
    var b = (new Date).getTime()
    var nsssjss = w_("".concat(url, "$$").concat(b))
    var sign = s_(url, "")
    console.log(sign)
    return {
        "nsssjss": nsssjss,
        'timestamp': b,
        'sign': sign.sign,
        'time': sign.time
    }
}

console.log(encrypt())