var crypto = require('crypto')
function h_(e, n, o) {
    var d = "";
    var n = Buffer.from(n, "utf8")
    var o = Buffer.from(o, "utf8");
    var c = crypto.createDecipheriv("aes-128-cbc", n, o);
    return d += c.update(e, "hex", "utf8"),
        d += c.final("utf8")
}

function v_(e, path, n, r) {
    var s = n.s
        , d = n.k
        , m = n.l
        , f = n.d
        , v = n.sort
        , l = n.num
        , k = function (content, t, e) {
            for (var a = Array.from(content), n = Array.from(t), r = a.length, o = n.length, d = String.fromCodePoint, i = 0; i < r; i++)
                a[i] = d(a[i].codePointAt(0) ^ n[(i + e) % o].codePointAt(0));
            return a.join("")
        }(function (s, t, path, e) {
            return [s, t, e, path].join("(&&)")
        }(function (t, e) {
            var n = t;
            if (true) {
                var r = [];
                for (var d in n)
                    Array.isArray(n[d]) && "get" === e && (n[d] = n[d].join("")),
                        "post" === e && (_()(n[d]) || o()(n[d])) && (n[d] = JSON.stringify(n[d])),
                        r.push(n[d]);
                return r.sort(),
                    r.join("")
            }
        }(e, r), parseInt((new Date).getTime() / 1e3) - 655876800 - f, path, v), h_(s, d, m), l);
    return Buffer.from(k).toString("base64")
}


function encrypt(r, s, k, l) {
    var path = '/v2/user/favorite'
    var n = {
        "proxy": "/app",
        "target": "",
        "sort": "dd",
        "num": 10,
        "s": s,
        "k": k,
        "l": l,
        "d": -139
    }
    o = v_(r, path, {
        s: n.s,
        k: n.k,
        l: n.l,
        d: n.d,
        sort: n.sort,
        num: n.num
    }, "get");
    return {
        "market_id": "",
        "sub_type": "1",
        "is_detail": "0",
        "is_go_sea": "0",
        "country_id": "",
        'k': o
    }

}

// console.log(encrypt({
//     "market_id": "",
//     "sub_type": "1",
//     "is_detail": "0",
//     "is_go_sea": "0",
//     "country_id": "",
// }))
