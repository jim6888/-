crypto_js = require('crypto-js');
const crypto = require('crypto');
//加密数据
function encrypt(user) {
    var t = [
        "keyWord",
        user,
        "iIndex"
    ]
    var s = t.join("_")
    const uuid = crypto.randomUUID();
    var sign = crypto_js.MD5(s).toString()
    return {
        sign: sign,
        uuid: uuid,
        keyWord: user
    };
}
var w = {
    stringify: function (v) {
        for (var m = v.words, C = v.sigBytes, R = [], S = 0; S < C; S++) {
            var x = m[S >>> 2] >>> 24 - S % 4 * 8 & 255;
            R.push(String.fromCharCode(x))
        }
        return R.join("")
    },
    parse: function (v) {
        for (var m = v.length, C = [], R = 0; R < m; R++)
            C[R >>> 2] |= (v.charCodeAt(R) & 255) << 24 - R % 4 * 8;
        return new g.init(C, m)
    }
}
var g = ({
    init: function (v, m) {
        var i = undefined;
        v = this.words = v || [],
            m != i ? this.sigBytes = m : this.sigBytes = v.length * 4
    },
    toString: function (v) {
        return (v || b).stringify(this)
    },
    concat: function (v) {
        var m = this.words
            , C = v.words
            , R = this.sigBytes
            , S = v.sigBytes;
        if (this.clamp(),
            R % 4)
            for (var x = 0; x < S; x++) {
                var L = C[x >>> 2] >>> 24 - x % 4 * 8 & 255;
                m[R + x >>> 2] |= L << 24 - (R + x) % 4 * 8
            }
        else
            for (var N = 0; N < S; N += 4)
                m[R + N >>> 2] = C[N >>> 2];
        return this.sigBytes += S,
            this
    },
    clamp: function () {
        var v = this.words
            , m = this.sigBytes;
        v[m >>> 2] &= 4294967295 << 32 - m % 4 * 8,
            v.length = r.ceil(m / 4)
    },
    clone: function () {
        var v = f.clone.call(this);
        return v.words = this.words.slice(0),
            v
    },
    random: function (v) {
        for (var m = [], C = 0; C < v; C += 4)
            m.push(s());
        return new g.init(m, v)
    }
})
var _m = {
    stringify: function (v) {
        try {
            return decodeURIComponent(escape(w.stringify(v)))
        } catch {
            throw new Error("Malformed UTF-8 data")
        }
    },
    parse: function (v) {
        return w.parse(unescape(encodeURIComponent(v)))
    }
}
// 数据解密
function decrypt_data(e) {
    var n = e
        , r = n.data;
    var i = _m.parse(n.lastFetchTime + "000")
        , a = _m.parse(n.lastFetchTime + "000")
    var s = crypto_js.AES.decrypt(r.toString(), i, {
        iv: a
    });
    var c = s.toString(_m)
    return JSON.parse(c)
}




