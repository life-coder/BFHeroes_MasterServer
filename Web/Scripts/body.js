(function(b) {
	var a = b.BFH = b.BFH || {},
		c = a.env = {};
	c.agt = b.navigator.userAgent.toLowerCase();
	c.browser = {
		firefox: !!c.agt.match(/firefox/i),
		chrome: !!b.chrome,
		ie: !!c.agt.match(/(?:\b(MS)?IE\s+|\bTrident\/7\.0;.*\s+rv:)(\d+)/i)
	};
	c.browser.version = (function() {
		var d;
		if (c.browser.firefox) {
			d = "firefox/"
		} else {
			if (c.browser.chrome) {
				d = "chrome/"
			} else {
				if (c.browser.ie) {
					d = !!c.agt.match(/msie/i) ? "msie" : "rv:"
				}
			}
		}
		return parseInt(c.agt.split(d)[1], 10)
	}())
}(this));
(function() {
	var A = this;
	var m = A._;
	var H = {};
	var G = Array.prototype,
		f = Object.prototype,
		u = Function.prototype;
	var K = G.push,
		r = G.slice,
		C = G.concat,
		d = f.toString,
		l = f.hasOwnProperty;
	var O = G.forEach,
		t = G.map,
		I = G.reduce,
		c = G.reduceRight,
		b = G.filter,
		F = G.every,
		s = G.some,
		q = G.indexOf,
		n = G.lastIndexOf,
		y = Array.isArray,
		e = Object.keys,
		J = u.bind;
	var P = function(Q) {
		if (Q instanceof P) {
			return Q
		}
		if (!(this instanceof P)) {
			return new P(Q)
		}
		this._wrapped = Q
	};
	if (typeof exports !== "undefined") {
		if (typeof module !== "undefined" && module.exports) {
			exports = module.exports = P
		}
		exports._ = P
	} else {
		A._ = P
	}
	P.VERSION = "1.4.4";
	var L = P.each = P.forEach = function(V, U, T) {
		if (V == null) {
			return
		}
		if (O && V.forEach === O) {
			V.forEach(U, T)
		} else {
			if (V.length === +V.length) {
				for (var S = 0, Q = V.length; S < Q; S++) {
					if (U.call(T, V[S], S, V) === H) {
						return
					}
				}
			} else {
				for (var R in V) {
					if (P.has(V, R)) {
						if (U.call(T, V[R], R, V) === H) {
							return
						}
					}
				}
			}
		}
	};
	P.map = P.collect = function(T, S, R) {
		var Q = [];
		if (T == null) {
			return Q
		}
		if (t && T.map === t) {
			return T.map(S, R)
		}
		L(T, function(W, U, V) {
			Q[Q.length] = S.call(R, W, U, V)
		});
		return Q
	};
	var g = "Reduce of empty array with no initial value";
	P.reduce = P.foldl = P.inject = function(U, T, Q, S) {
		var R = arguments.length > 2;
		if (U == null) {
			U = []
		}
		if (I && U.reduce === I) {
			if (S) {
				T = P.bind(T, S)
			}
			return R ? U.reduce(T, Q) : U.reduce(T)
		}
		L(U, function(X, V, W) {
			if (!R) {
				Q = X;
				R = true
			} else {
				Q = T.call(S, Q, X, V, W)
			}
		});
		if (!R) {
			throw new TypeError(g)
		}
		return Q
	};
	P.reduceRight = P.foldr = function(W, T, Q, S) {
		var R = arguments.length > 2;
		if (W == null) {
			W = []
		}
		if (c && W.reduceRight === c) {
			if (S) {
				T = P.bind(T, S)
			}
			return R ? W.reduceRight(T, Q) : W.reduceRight(T)
		}
		var V = W.length;
		if (V !== +V) {
			var U = P.keys(W);
			V = U.length
		}
		L(W, function(Z, X, Y) {
			X = U ? U[--V] : --V;
			if (!R) {
				Q = W[X];
				R = true
			} else {
				Q = T.call(S, Q, W[X], X, Y)
			}
		});
		if (!R) {
			throw new TypeError(g)
		}
		return Q
	};
	P.find = P.detect = function(T, S, R) {
		var Q;
		E(T, function(W, U, V) {
			if (S.call(R, W, U, V)) {
				Q = W;
				return true
			}
		});
		return Q
	};
	P.filter = P.select = function(T, S, R) {
		var Q = [];
		if (T == null) {
			return Q
		}
		if (b && T.filter === b) {
			return T.filter(S, R)
		}
		L(T, function(W, U, V) {
			if (S.call(R, W, U, V)) {
				Q[Q.length] = W
			}
		});
		return Q
	};
	P.reject = function(S, R, Q) {
		return P.filter(S, function(V, T, U) {
			return !R.call(Q, V, T, U)
		}, Q)
	};
	P.every = P.all = function(T, S, R) {
		S || (S = P.identity);
		var Q = true;
		if (T == null) {
			return Q
		}
		if (F && T.every === F) {
			return T.every(S, R)
		}
		L(T, function(W, U, V) {
			if (!(Q = Q && S.call(R, W, U, V))) {
				return H
			}
		});
		return !!Q
	};
	var E = P.some = P.any = function(T, S, R) {
		S || (S = P.identity);
		var Q = false;
		if (T == null) {
			return Q
		}
		if (s && T.some === s) {
			return T.some(S, R)
		}
		L(T, function(W, U, V) {
			if (Q || (Q = S.call(R, W, U, V))) {
				return H
			}
		});
		return !!Q
	};
	P.contains = P.include = function(R, Q) {
		if (R == null) {
			return false
		}
		if (q && R.indexOf === q) {
			return R.indexOf(Q) != -1
		}
		return E(R, function(S) {
			return S === Q
		})
	};
	P.invoke = function(S, T) {
		var Q = r.call(arguments, 2);
		var R = P.isFunction(T);
		return P.map(S, function(U) {
			return (R ? T : U[T])
				.apply(U, Q)
		})
	};
	P.pluck = function(R, Q) {
		return P.map(R, function(S) {
			return S[Q]
		})
	};
	P.where = function(R, Q, S) {
		if (P.isEmpty(Q)) {
			return S ? null : []
		}
		return P[S ? "find" : "filter"](R, function(U) {
			for (var T in Q) {
				if (Q[T] !== U[T]) {
					return false
				}
			}
			return true
		})
	};
	P.findWhere = function(R, Q) {
		return P.where(R, Q, true)
	};
	P.max = function(T, S, R) {
		if (!S && P.isArray(T) && T[0] === +T[0] && T.length < 65535) {
			return Math.max.apply(Math, T)
		}
		if (!S && P.isEmpty(T)) {
			return -Infinity
		}
		var Q = {
			computed: -Infinity,
			value: -Infinity
		};
		L(T, function(X, U, W) {
			var V = S ? S.call(R, X, U, W) : X;
			V >= Q.computed && (Q = {
				value: X,
				computed: V
			})
		});
		return Q.value
	};
	P.min = function(T, S, R) {
		if (!S && P.isArray(T) && T[0] === +T[0] && T.length < 65535) {
			return Math.min.apply(Math, T)
		}
		if (!S && P.isEmpty(T)) {
			return Infinity
		}
		var Q = {
			computed: Infinity,
			value: Infinity
		};
		L(T, function(X, U, W) {
			var V = S ? S.call(R, X, U, W) : X;
			V < Q.computed && (Q = {
				value: X,
				computed: V
			})
		});
		return Q.value
	};
	P.shuffle = function(T) {
		var S;
		var R = 0;
		var Q = [];
		L(T, function(U) {
			S = P.random(R++);
			Q[R - 1] = Q[S];
			Q[S] = U
		});
		return Q
	};
	var a = function(Q) {
		return P.isFunction(Q) ? Q : function(R) {
			return R[Q]
		}
	};
	P.sortBy = function(T, S, Q) {
		var R = a(S);
		return P.pluck(P.map(T, function(W, U, V) {
				return {
					value: W,
					index: U,
					criteria: R.call(Q, W, U, V)
				}
			})
			.sort(function(X, W) {
				var V = X.criteria;
				var U = W.criteria;
				if (V !== U) {
					if (V > U || V === void 0) {
						return 1
					}
					if (V < U || U === void 0) {
						return -1
					}
				}
				return X.index < W.index ? -1 : 1
			}), "value")
	};
	var x = function(V, U, R, T) {
		var Q = {};
		var S = a(U || P.identity);
		L(V, function(Y, W) {
			var X = S.call(R, Y, W, V);
			T(Q, X, Y)
		});
		return Q
	};
	P.groupBy = function(S, R, Q) {
		return x(S, R, Q, function(T, U, V) {
			(P.has(T, U) ? T[U] : (T[U] = []))
			.push(V)
		})
	};
	P.countBy = function(S, R, Q) {
		return x(S, R, Q, function(T, U) {
			if (!P.has(T, U)) {
				T[U] = 0
			}
			T[U]++
		})
	};
	P.sortedIndex = function(X, W, T, S) {
		T = T == null ? P.identity : a(T);
		var V = T.call(S, W);
		var Q = 0,
			U = X.length;
		while (Q < U) {
			var R = (Q + U) >>> 1;
			T.call(S, X[R]) < V ? Q = R + 1 : U = R
		}
		return Q
	};
	P.toArray = function(Q) {
		if (!Q) {
			return []
		}
		if (P.isArray(Q)) {
			return r.call(Q)
		}
		if (Q.length === +Q.length) {
			return P.map(Q, P.identity)
		}
		return P.values(Q)
	};
	P.size = function(Q) {
		if (Q == null) {
			return 0
		}
		return (Q.length === +Q.length) ? Q.length : P.keys(Q)
			.length
	};
	P.first = P.head = P.take = function(S, R, Q) {
		if (S == null) {
			return void 0
		}
		return (R != null) && !Q ? r.call(S, 0, R) : S[0]
	};
	P.initial = function(S, R, Q) {
		return r.call(S, 0, S.length - ((R == null) || Q ? 1 : R))
	};
	P.last = function(S, R, Q) {
		if (S == null) {
			return void 0
		}
		if ((R != null) && !Q) {
			return r.call(S, Math.max(S.length - R, 0))
		} else {
			return S[S.length - 1]
		}
	};
	P.rest = P.tail = P.drop = function(S, R, Q) {
		return r.call(S, (R == null) || Q ? 1 : R)
	};
	P.compact = function(Q) {
		return P.filter(Q, P.identity)
	};
	var B = function(R, S, Q) {
		L(R, function(T) {
			if (P.isArray(T)) {
				S ? K.apply(Q, T) : B(T, S, Q)
			} else {
				Q.push(T)
			}
		});
		return Q
	};
	P.flatten = function(R, Q) {
		return B(R, Q, [])
	};
	P.without = function(Q) {
		return P.difference(Q, r.call(arguments, 1))
	};
	P.uniq = P.unique = function(W, V, U, T) {
		if (P.isFunction(V)) {
			T = U;
			U = V;
			V = false
		}
		var R = U ? P.map(W, U, T) : W;
		var S = [];
		var Q = [];
		L(R, function(Y, X) {
			if (V ? (!X || Q[Q.length - 1] !== Y) : !P.contains(Q, Y)) {
				Q.push(Y);
				S.push(W[X])
			}
		});
		return S
	};
	P.union = function() {
		return P.uniq(C.apply(G, arguments))
	};
	P.intersection = function(R) {
		var Q = r.call(arguments, 1);
		return P.filter(P.uniq(R), function(S) {
			return P.every(Q, function(T) {
				return P.indexOf(T, S) >= 0
			})
		})
	};
	P.difference = function(R) {
		var Q = C.apply(G, r.call(arguments, 1));
		return P.filter(R, function(S) {
			return !P.contains(Q, S)
		})
	};
	P.zip = function() {
		var Q = r.call(arguments);
		var T = P.max(P.pluck(Q, "length"));
		var S = new Array(T);
		for (var R = 0; R < T; R++) {
			S[R] = P.pluck(Q, "" + R)
		}
		return S
	};
	P.object = function(U, S) {
		if (U == null) {
			return {}
		}
		var Q = {};
		for (var T = 0, R = U.length; T < R; T++) {
			if (S) {
				Q[U[T]] = S[T]
			} else {
				Q[U[T][0]] = U[T][1]
			}
		}
		return Q
	};
	P.indexOf = function(U, S, T) {
		if (U == null) {
			return -1
		}
		var R = 0,
			Q = U.length;
		if (T) {
			if (typeof T == "number") {
				R = (T < 0 ? Math.max(0, Q + T) : T)
			} else {
				R = P.sortedIndex(U, S);
				return U[R] === S ? R : -1
			}
		}
		if (q && U.indexOf === q) {
			return U.indexOf(S, T)
		}
		for (; R < Q; R++) {
			if (U[R] === S) {
				return R
			}
		}
		return -1
	};
	P.lastIndexOf = function(U, S, T) {
		if (U == null) {
			return -1
		}
		var Q = T != null;
		if (n && U.lastIndexOf === n) {
			return Q ? U.lastIndexOf(S, T) : U.lastIndexOf(S)
		}
		var R = (Q ? T : U.length);
		while (R--) {
			if (U[R] === S) {
				return R
			}
		}
		return -1
	};
	P.range = function(V, T, U) {
		if (arguments.length <= 1) {
			T = V || 0;
			V = 0
		}
		U = arguments[2] || 1;
		var R = Math.max(Math.ceil((T - V) / U), 0);
		var Q = 0;
		var S = new Array(R);
		while (Q < R) {
			S[Q++] = V;
			V += U
		}
		return S
	};
	P.bind = function(S, R) {
		if (S.bind === J && J) {
			return J.apply(S, r.call(arguments, 1))
		}
		var Q = r.call(arguments, 2);
		return function() {
			return S.apply(R, Q.concat(r.call(arguments)))
		}
	};
	P.partial = function(R) {
		var Q = r.call(arguments, 1);
		return function() {
			return R.apply(this, Q.concat(r.call(arguments)))
		}
	};
	P.bindAll = function(R) {
		var Q = r.call(arguments, 1);
		if (Q.length === 0) {
			Q = P.functions(R)
		}
		L(Q, function(S) {
			R[S] = P.bind(R[S], R)
		});
		return R
	};
	P.memoize = function(S, R) {
		var Q = {};
		R || (R = P.identity);
		return function() {
			var T = R.apply(this, arguments);
			return P.has(Q, T) ? Q[T] : (Q[T] = S.apply(this, arguments))
		}
	};
	P.delay = function(R, S) {
		var Q = r.call(arguments, 2);
		return setTimeout(function() {
			return R.apply(null, Q)
		}, S)
	};
	P.defer = function(Q) {
		return P.delay.apply(P, [Q, 1].concat(r.call(arguments, 1)))
	};
	P.throttle = function(V, X) {
		var T, S, W, Q;
		var U = 0;
		var R = function() {
			U = new Date;
			W = null;
			Q = V.apply(T, S)
		};
		return function() {
			var Y = new Date;
			var Z = X - (Y - U);
			T = this;
			S = arguments;
			if (Z <= 0) {
				clearTimeout(W);
				W = null;
				U = Y;
				Q = V.apply(T, S)
			} else {
				if (!W) {
					W = setTimeout(R, Z)
				}
			}
			return Q
		}
	};
	P.debounce = function(S, U, R) {
		var T, Q;
		return function() {
			var Y = this,
				X = arguments;
			var W = function() {
				T = null;
				if (!R) {
					Q = S.apply(Y, X)
				}
			};
			var V = R && !T;
			clearTimeout(T);
			T = setTimeout(W, U);
			if (V) {
				Q = S.apply(Y, X)
			}
			return Q
		}
	};
	P.once = function(S) {
		var Q = false,
			R;
		return function() {
			if (Q) {
				return R
			}
			Q = true;
			R = S.apply(this, arguments);
			S = null;
			return R
		}
	};
	P.wrap = function(Q, R) {
		return function() {
			var S = [Q];
			K.apply(S, arguments);
			return R.apply(this, S)
		}
	};
	P.compose = function() {
		var Q = arguments;
		return function() {
			var R = arguments;
			for (var S = Q.length - 1; S >= 0; S--) {
				R = [Q[S].apply(this, R)]
			}
			return R[0]
		}
	};
	P.after = function(R, Q) {
		if (R <= 0) {
			return Q()
		}
		return function() {
			if (--R < 1) {
				return Q.apply(this, arguments)
			}
		}
	};
	P.keys = e || function(S) {
		if (S !== Object(S)) {
			throw new TypeError("Invalid object")
		}
		var R = [];
		for (var Q in S) {
			if (P.has(S, Q)) {
				R[R.length] = Q
			}
		}
		return R
	};
	P.values = function(S) {
		var Q = [];
		for (var R in S) {
			if (P.has(S, R)) {
				Q.push(S[R])
			}
		}
		return Q
	};
	P.pairs = function(S) {
		var R = [];
		for (var Q in S) {
			if (P.has(S, Q)) {
				R.push([Q, S[Q]])
			}
		}
		return R
	};
	P.invert = function(S) {
		var Q = {};
		for (var R in S) {
			if (P.has(S, R)) {
				Q[S[R]] = R
			}
		}
		return Q
	};
	P.functions = P.methods = function(S) {
		var R = [];
		for (var Q in S) {
			if (P.isFunction(S[Q])) {
				R.push(Q)
			}
		}
		return R.sort()
	};
	P.extend = function(Q) {
		L(r.call(arguments, 1), function(R) {
			if (R) {
				for (var S in R) {
					Q[S] = R[S]
				}
			}
		});
		return Q
	};
	P.pick = function(R) {
		var S = {};
		var Q = C.apply(G, r.call(arguments, 1));
		L(Q, function(T) {
			if (T in R) {
				S[T] = R[T]
			}
		});
		return S
	};
	P.omit = function(S) {
		var T = {};
		var R = C.apply(G, r.call(arguments, 1));
		for (var Q in S) {
			if (!P.contains(R, Q)) {
				T[Q] = S[Q]
			}
		}
		return T
	};
	P.defaults = function(Q) {
		L(r.call(arguments, 1), function(R) {
			if (R) {
				for (var S in R) {
					if (Q[S] == null) {
						Q[S] = R[S]
					}
				}
			}
		});
		return Q
	};
	P.clone = function(Q) {
		if (!P.isObject(Q)) {
			return Q
		}
		return P.isArray(Q) ? Q.slice() : P.extend({}, Q)
	};
	P.tap = function(R, Q) {
		Q(R);
		return R
	};
	var M = function(X, W, R, S) {
		if (X === W) {
			return X !== 0 || 1 / X == 1 / W
		}
		if (X == null || W == null) {
			return X === W
		}
		if (X instanceof P) {
			X = X._wrapped
		}
		if (W instanceof P) {
			W = W._wrapped
		}
		var U = d.call(X);
		if (U != d.call(W)) {
			return false
		}
		switch (U) {
			case "[object String]":
				return X == String(W);
			case "[object Number]":
				return X != +X ? W != +W : (X == 0 ? 1 / X == 1 / W : X == +W);
			case "[object Date]":
			case "[object Boolean]":
				return +X == +W;
			case "[object RegExp]":
				return X.source == W.source && X.global == W.global && X.multiline == W.multiline && X.ignoreCase == W.ignoreCase
		}
		if (typeof X != "object" || typeof W != "object") {
			return false
		}
		var Q = R.length;
		while (Q--) {
			if (R[Q] == X) {
				return S[Q] == W
			}
		}
		R.push(X);
		S.push(W);
		var Z = 0,
			aa = true;
		if (U == "[object Array]") {
			Z = X.length;
			aa = Z == W.length;
			if (aa) {
				while (Z--) {
					if (!(aa = M(X[Z], W[Z], R, S))) {
						break
					}
				}
			}
		} else {
			var V = X.constructor,
				T = W.constructor;
			if (V !== T && !(P.isFunction(V) && (V instanceof V) && P.isFunction(T) && (T instanceof T))) {
				return false
			}
			for (var Y in X) {
				if (P.has(X, Y)) {
					Z++;
					if (!(aa = P.has(W, Y) && M(X[Y], W[Y], R, S))) {
						break
					}
				}
			}
			if (aa) {
				for (Y in W) {
					if (P.has(W, Y) && !(Z--)) {
						break
					}
				}
				aa = !Z
			}
		}
		R.pop();
		S.pop();
		return aa
	};
	P.isEqual = function(R, Q) {
		return M(R, Q, [], [])
	};
	P.isEmpty = function(R) {
		if (R == null) {
			return true
		}
		if (P.isArray(R) || P.isString(R)) {
			return R.length === 0
		}
		for (var Q in R) {
			if (P.has(R, Q)) {
				return false
			}
		}
		return true
	};
	P.isElement = function(Q) {
		return !!(Q && Q.nodeType === 1)
	};
	P.isArray = y || function(Q) {
		return d.call(Q) == "[object Array]"
	};
	P.isObject = function(Q) {
		return Q === Object(Q)
	};
	L(["Arguments", "Function", "String", "Number", "Date", "RegExp"], function(Q) {
		P["is" + Q] = function(R) {
			return d.call(R) == "[object " + Q + "]"
		}
	});
	if (!P.isArguments(arguments)) {
		P.isArguments = function(Q) {
			return !!(Q && P.has(Q, "callee"))
		}
	}
	if (typeof(/./) !== "function") {
		P.isFunction = function(Q) {
			return typeof Q === "function"
		}
	}
	P.isFinite = function(Q) {
		return isFinite(Q) && !isNaN(parseFloat(Q))
	};
	P.isNaN = function(Q) {
		return P.isNumber(Q) && Q != +Q
	};
	P.isBoolean = function(Q) {
		return Q === true || Q === false || d.call(Q) == "[object Boolean]"
	};
	P.isNull = function(Q) {
		return Q === null
	};
	P.isUndefined = function(Q) {
		return Q === void 0
	};
	P.has = function(R, Q) {
		return l.call(R, Q)
	};
	P.noConflict = function() {
		A._ = m;
		return this
	};
	P.identity = function(Q) {
		return Q
	};
	P.times = function(U, T, S) {
		var Q = Array(U);
		for (var R = 0; R < U; R++) {
			Q[R] = T.call(S, R)
		}
		return Q
	};
	P.random = function(R, Q) {
		if (Q == null) {
			Q = R;
			R = 0
		}
		return R + Math.floor(Math.random() * (Q - R + 1))
	};
	var p = {
		escape: {
			"&": "&amp;",
			"<": "&lt;",
			">": "&gt;",
			'"': "&quot;",
			"'": "&#x27;",
			"/": "&#x2F;"
		}
	};
	p.unescape = P.invert(p.escape);
	var N = {
		escape: new RegExp("[" + P.keys(p.escape)
			.join("") + "]", "g"),
		unescape: new RegExp("(" + P.keys(p.unescape)
			.join("|") + ")", "g")
	};
	P.each(["escape", "unescape"], function(Q) {
		P[Q] = function(R) {
			if (R == null) {
				return ""
			}
			return ("" + R)
				.replace(N[Q], function(S) {
					return p[Q][S]
				})
		}
	});
	P.result = function(Q, S) {
		if (Q == null) {
			return null
		}
		var R = Q[S];
		return P.isFunction(R) ? R.call(Q) : R
	};
	P.mixin = function(Q) {
		L(P.functions(Q), function(R) {
			var S = P[R] = Q[R];
			P.prototype[R] = function() {
				var T = [this._wrapped];
				K.apply(T, arguments);
				return v.call(this, S.apply(P, T))
			}
		})
	};
	var D = 0;
	P.uniqueId = function(Q) {
		var R = ++D + "";
		return Q ? Q + R : R
	};
	P.templateSettings = {
		evaluate: /<%([\s\S]+?)%>/g,
		interpolate: /<%=([\s\S]+?)%>/g,
		escape: /<%-([\s\S]+?)%>/g
	};
	var z = /(.)^/;
	var j = {
		"'": "'",
		"\\": "\\",
		"\r": "r",
		"\n": "n",
		"\t": "t",
		"\u2028": "u2028",
		"\u2029": "u2029"
	};
	var k = /\\|'|\r|\n|\t|\u2028|\u2029/g;
	P.template = function(Y, T, S) {
		var R;
		S = P.defaults({}, S, P.templateSettings);
		var U = new RegExp([(S.escape || z)
			.source, (S.interpolate || z)
			.source, (S.evaluate || z)
			.source].join("|") + "|$", "g");
		var V = 0;
		var Q = "__p+='";
		Y.replace(U, function(aa, ab, Z, ad, ac) {
			Q += Y.slice(V, ac)
				.replace(k, function(ae) {
					return "\\" + j[ae]
				});
			if (ab) {
				Q += "'+\n((__t=(" + ab + "))==null?'':_.escape(__t))+\n'"
			}
			if (Z) {
				Q += "'+\n((__t=(" + Z + "))==null?'':__t)+\n'"
			}
			if (ad) {
				Q += "';\n" + ad + "\n__p+='"
			}
			V = ac + aa.length;
			return aa
		});
		Q += "';\n";
		if (!S.variable) {
			Q = "with(obj||{}){\n" + Q + "}\n"
		}
		Q = "var __t,__p='',__j=Array.prototype.join,print=function(){__p+=__j.call(arguments,'');};\n" + Q + "return __p;\n";
		try {
			R = new Function(S.variable || "obj", "_", Q)
		} catch (W) {
			W.source = Q;
			throw W
		}
		if (T) {
			return R(T, P)
		}
		var X = function(Z) {
			return R.call(this, Z, P)
		};
		X.source = "function(" + (S.variable || "obj") + "){\n" + Q + "}";
		return X
	};
	P.chain = function(Q) {
		return P(Q)
			.chain()
	};
	var v = function(Q) {
		return this._chain ? P(Q)
			.chain() : Q
	};
	P.mixin(P);
	L(["pop", "push", "reverse", "shift", "sort", "splice", "unshift"], function(Q) {
		var R = G[Q];
		P.prototype[Q] = function() {
			var S = this._wrapped;
			R.apply(S, arguments);
			if ((Q == "shift" || Q == "splice") && S.length === 0) {
				delete S[0]
			}
			return v.call(this, S)
		}
	});
	L(["concat", "join", "slice"], function(Q) {
		var R = G[Q];
		P.prototype[Q] = function() {
			return v.call(this, R.apply(this._wrapped, arguments))
		}
	});
	P.extend(P.prototype, {
		chain: function() {
			this._chain = true;
			return this
		},
		value: function() {
			return this._wrapped
		}
	})
})
.call(this);
(function() {
	var y = this;
	var F = y.Backbone;
	var g = [];
	var H = g.push;
	var q = g.slice;
	var x = g.splice;
	var D;
	if (typeof exports !== "undefined") {
		D = exports
	} else {
		D = y.Backbone = {}
	}
	D.VERSION = "1.0.0";
	var P = y._;
	if (!P && (typeof require !== "undefined")) {
		P = require("underscore")
	}
	D.$ = y.jQuery || y.Zepto || y.ender || y.$;
	D.noConflict = function() {
		y.Backbone = F;
		return this
	};
	D.emulateHTTP = false;
	D.emulateJSON = false;
	var N = D.Events = {
		on: function(Q, T, S) {
			if (!B(this, "on", Q, [T, S]) || !T) {
				return this
			}
			this._events || (this._events = {});
			var R = this._events[Q] || (this._events[Q] = []);
			R.push({
				callback: T,
				context: S,
				ctx: S || this
			});
			return this
		},
		once: function(R, U, S) {
			if (!B(this, "once", R, [U, S]) || !U) {
				return this
			}
			var Q = this;
			var T = P.once(function() {
				Q.off(R, T);
				U.apply(this, arguments)
			});
			T._callback = U;
			return this.on(R, T, S)
		},
		off: function(Q, Z, R) {
			var X, Y, aa, W, V, S, U, T;
			if (!this._events || !B(this, "off", Q, [Z, R])) {
				return this
			}
			if (!Q && !Z && !R) {
				this._events = {};
				return this
			}
			W = Q ? [Q] : P.keys(this._events);
			for (V = 0, S = W.length; V < S; V++) {
				Q = W[V];
				if (aa = this._events[Q]) {
					this._events[Q] = X = [];
					if (Z || R) {
						for (U = 0, T = aa.length; U < T; U++) {
							Y = aa[U];
							if ((Z && Z !== Y.callback && Z !== Y.callback._callback) || (R && R !== Y.context)) {
								X.push(Y)
							}
						}
					}
					if (!X.length) {
						delete this._events[Q]
					}
				}
			}
			return this
		},
		trigger: function(S) {
			if (!this._events) {
				return this
			}
			var R = q.call(arguments, 1);
			if (!B(this, "trigger", S, R)) {
				return this
			}
			var T = this._events[S];
			var Q = this._events.all;
			if (T) {
				b(T, R)
			}
			if (Q) {
				b(Q, arguments)
			}
			return this
		},
		stopListening: function(T, Q, V) {
			var R = this._listeners;
			if (!R) {
				return this
			}
			var S = !Q && !V;
			if (typeof Q === "object") {
				V = this
			}
			if (T) {
				(R = {})[T._listenerId] = T
			}
			for (var U in R) {
				R[U].off(Q, V, this);
				if (S) {
					delete this._listeners[U]
				}
			}
			return this
		}
	};
	var A = /\s+/;
	var B = function(X, V, R, U) {
		if (!R) {
			return true
		}
		if (typeof R === "object") {
			for (var T in R) {
				X[V].apply(X, [T, R[T]].concat(U))
			}
			return false
		}
		if (A.test(R)) {
			var W = R.split(A);
			for (var S = 0, Q = W.length; S < Q; S++) {
				X[V].apply(X, [W[S]].concat(U))
			}
			return false
		}
		return true
	};
	var b = function(V, T) {
		var W, U = -1,
			S = V.length,
			R = T[0],
			Q = T[1],
			X = T[2];
		switch (T.length) {
			case 0:
				while (++U < S) {
					(W = V[U])
					.callback.call(W.ctx)
				}
				return;
			case 1:
				while (++U < S) {
					(W = V[U])
					.callback.call(W.ctx, R)
				}
				return;
			case 2:
				while (++U < S) {
					(W = V[U])
					.callback.call(W.ctx, R, Q)
				}
				return;
			case 3:
				while (++U < S) {
					(W = V[U])
					.callback.call(W.ctx, R, Q, X)
				}
				return;
			default:
				while (++U < S) {
					(W = V[U])
					.callback.apply(W.ctx, T)
				}
		}
	};
	var G = {
		listenTo: "on",
		listenToOnce: "once"
	};
	P.each(G, function(Q, R) {
		N[R] = function(U, S, W) {
			var T = this._listeners || (this._listeners = {});
			var V = U._listenerId || (U._listenerId = P.uniqueId("l"));
			T[V] = U;
			if (typeof S === "object") {
				W = this
			}
			U[Q](S, W, this);
			return this
		}
	});
	N.bind = N.on;
	N.unbind = N.off;
	P.extend(D, N);
	var I = D.Model = function(Q, S) {
		var T;
		var R = Q || {};
		S || (S = {});
		this.cid = P.uniqueId("c");
		this.attributes = {};
		P.extend(this, P.pick(S, J));
		if (S.parse) {
			R = this.parse(R, S) || {}
		}
		if (T = P.result(this, "defaults")) {
			R = P.defaults({}, R, T)
		}
		this.set(R, S);
		this.changed = {};
		this.initialize.apply(this, arguments)
	};
	var J = ["url", "urlRoot", "collection"];
	P.extend(I.prototype, N, {
		changed: null,
		validationError: null,
		idAttribute: "id",
		initialize: function() {},
		toJSON: function(Q) {
			return P.clone(this.attributes)
		},
		sync: function() {
			return D.sync.apply(this, arguments)
		},
		get: function(Q) {
			return this.attributes[Q]
		},
		escape: function(Q) {
			return P.escape(this.get(Q))
		},
		has: function(Q) {
			return this.get(Q) != null
		},
		set: function(Y, Q, ac) {
			var W, Z, aa, X, V, ab, S, U;
			if (Y == null) {
				return this
			}
			if (typeof Y === "object") {
				Z = Y;
				ac = Q
			} else {
				(Z = {})[Y] = Q
			}
			ac || (ac = {});
			if (!this._validate(Z, ac)) {
				return false
			}
			aa = ac.unset;
			V = ac.silent;
			X = [];
			ab = this._changing;
			this._changing = true;
			if (!ab) {
				this._previousAttributes = P.clone(this.attributes);
				this.changed = {}
			}
			U = this.attributes, S = this._previousAttributes;
			if (this.idAttribute in Z) {
				this.id = Z[this.idAttribute]
			}
			for (W in Z) {
				Q = Z[W];
				if (!P.isEqual(U[W], Q)) {
					X.push(W)
				}
				if (!P.isEqual(S[W], Q)) {
					this.changed[W] = Q
				} else {
					delete this.changed[W]
				}
				aa ? delete U[W] : U[W] = Q
			}
			if (!V) {
				if (X.length) {
					this._pending = true
				}
				for (var T = 0, R = X.length; T < R; T++) {
					this.trigger("change:" + X[T], this, U[X[T]], ac)
				}
			}
			if (ab) {
				return this
			}
			if (!V) {
				while (this._pending) {
					this._pending = false;
					this.trigger("change", this, ac)
				}
			}
			this._pending = false;
			this._changing = false;
			return this
		},
		unset: function(Q, R) {
			return this.set(Q, void 0, P.extend({}, R, {
				unset: true
			}))
		},
		clear: function(R) {
			var Q = {};
			for (var S in this.attributes) {
				Q[S] = void 0
			}
			return this.set(Q, P.extend({}, R, {
				unset: true
			}))
		},
		hasChanged: function(Q) {
			if (Q == null) {
				return !P.isEmpty(this.changed)
			}
			return P.has(this.changed, Q)
		},
		changedAttributes: function(S) {
			if (!S) {
				return this.hasChanged() ? P.clone(this.changed) : false
			}
			var U, T = false;
			var R = this._changing ? this._previousAttributes : this.attributes;
			for (var Q in S) {
				if (P.isEqual(R[Q], (U = S[Q]))) {
					continue
				}(T || (T = {}))[Q] = U
			}
			return T
		},
		previous: function(Q) {
			if (Q == null || !this._previousAttributes) {
				return null
			}
			return this._previousAttributes[Q]
		},
		previousAttributes: function() {
			return P.clone(this._previousAttributes)
		},
		fetch: function(R) {
			R = R ? P.clone(R) : {};
			if (R.parse === void 0) {
				R.parse = true
			}
			var Q = this;
			var S = R.success;
			R.success = function(T) {
				if (!Q.set(Q.parse(T, R), R)) {
					return false
				}
				if (S) {
					S(Q, T, R)
				}
				Q.trigger("sync", Q, T, R)
			};
			L(this, R);
			return this.sync("read", this, R)
		},
		save: function(U, R, Y) {
			var V, Q, X, S = this.attributes;
			if (U == null || typeof U === "object") {
				V = U;
				Y = R
			} else {
				(V = {})[U] = R
			}
			if (V && (!Y || !Y.wait) && !this.set(V, Y)) {
				return false
			}
			Y = P.extend({
				validate: true
			}, Y);
			if (!this._validate(V, Y)) {
				return false
			}
			if (V && Y.wait) {
				this.attributes = P.extend({}, S, V)
			}
			if (Y.parse === void 0) {
				Y.parse = true
			}
			var T = this;
			var W = Y.success;
			Y.success = function(aa) {
				T.attributes = S;
				var Z = T.parse(aa, Y);
				if (Y.wait) {
					Z = P.extend(V || {}, Z)
				}
				if (P.isObject(Z) && !T.set(Z, Y)) {
					return false
				}
				if (W) {
					W(T, aa, Y)
				}
				T.trigger("sync", T, aa, Y)
			};
			L(this, Y);
			Q = this.isNew() ? "create" : (Y.patch ? "patch" : "update");
			if (Q === "patch") {
				Y.attrs = V
			}
			X = this.sync(Q, this, Y);
			if (V && Y.wait) {
				this.attributes = S
			}
			return X
		},
		destroy: function(R) {
			R = R ? P.clone(R) : {};
			var Q = this;
			var U = R.success;
			var S = function() {
				Q.trigger("destroy", Q, Q.collection, R)
			};
			R.success = function(V) {
				if (R.wait || Q.isNew()) {
					S()
				}
				if (U) {
					U(Q, V, R)
				}
				if (!Q.isNew()) {
					Q.trigger("sync", Q, V, R)
				}
			};
			if (this.isNew()) {
				R.success();
				return false
			}
			L(this, R);
			var T = this.sync("delete", this, R);
			if (!R.wait) {
				S()
			}
			return T
		},
		url: function() {
			var Q = P.result(this, "urlRoot") || P.result(this.collection, "url") || u();
			if (this.isNew()) {
				return Q
			}
			return Q + (Q.charAt(Q.length - 1) === "/" ? "" : "/") + encodeURIComponent(this.id)
		},
		parse: function(R, Q) {
			return R
		},
		clone: function() {
			return new this.constructor(this.attributes)
		},
		isNew: function() {
			return this.id == null
		},
		isValid: function(Q) {
			return this._validate({}, P.extend(Q || {}, {
				validate: true
			}))
		},
		_validate: function(S, R) {
			if (!R.validate || !this.validate) {
				return true
			}
			S = P.extend({}, this.attributes, S);
			var Q = this.validationError = this.validate(S, R) || null;
			if (!Q) {
				return true
			}
			this.trigger("invalid", this, Q, P.extend(R || {}, {
				validationError: Q
			}));
			return false
		}
	});
	var a = ["keys", "values", "pairs", "invert", "pick", "omit"];
	P.each(a, function(Q) {
		I.prototype[Q] = function() {
			var R = q.call(arguments);
			R.unshift(this.attributes);
			return P[Q].apply(P, R)
		}
	});
	var c = D.Collection = function(R, Q) {
		Q || (Q = {});
		if (Q.url) {
			this.url = Q.url
		}
		if (Q.model) {
			this.model = Q.model
		}
		if (Q.comparator !== void 0) {
			this.comparator = Q.comparator
		}
		this._reset();
		this.initialize.apply(this, arguments);
		if (R) {
			this.reset(R, P.extend({
				silent: true
			}, Q))
		}
	};
	var r = {
		add: true,
		remove: true,
		merge: true
	};
	var O = {
		add: true,
		merge: false,
		remove: false
	};
	P.extend(c.prototype, N, {
		model: I,
		initialize: function() {},
		toJSON: function(Q) {
			return this.map(function(R) {
				return R.toJSON(Q)
			})
		},
		sync: function() {
			return D.sync.apply(this, arguments)
		},
		add: function(R, Q) {
			return this.set(R, P.defaults(Q || {}, O))
		},
		remove: function(V, T) {
			V = P.isArray(V) ? V.slice() : [V];
			T || (T = {});
			var U, Q, S, R;
			for (U = 0, Q = V.length; U < Q; U++) {
				R = this.get(V[U]);
				if (!R) {
					continue
				}
				delete this._byId[R.id];
				delete this._byId[R.cid];
				S = this.indexOf(R);
				this.models.splice(S, 1);
				this.length--;
				if (!T.silent) {
					T.index = S;
					R.trigger("remove", R, this, T)
				}
				this._removeReference(R)
			}
			return this
		},
		set: function(R, ad) {
			ad = P.defaults(ad || {}, r);
			if (ad.parse) {
				R = this.parse(R, ad)
			}
			if (!P.isArray(R)) {
				R = R ? [R] : []
			}
			var Y, U, aa, ab, S, Z;
			var T = ad.at;
			var X = this.comparator && (T == null) && ad.sort !== false;
			var V = P.isString(this.comparator) ? this.comparator : null;
			var ac = [],
				Q = [],
				W = {};
			for (Y = 0, U = R.length; Y < U; Y++) {
				if (!(aa = this._prepareModel(R[Y], ad))) {
					continue
				}
				if (S = this.get(aa)) {
					if (ad.remove) {
						W[S.cid] = true
					}
					if (ad.merge) {
						S.set(aa.attributes, ad);
						if (X && !Z && S.hasChanged(V)) {
							Z = true
						}
					}
				} else {
					if (ad.add) {
						ac.push(aa);
						aa.on("all", this._onModelEvent, this);
						this._byId[aa.cid] = aa;
						if (aa.id != null) {
							this._byId[aa.id] = aa
						}
					}
				}
			}
			if (ad.remove) {
				for (Y = 0, U = this.length; Y < U; ++Y) {
					if (!W[(aa = this.models[Y])
							.cid]) {
						Q.push(aa)
					}
				}
				if (Q.length) {
					this.remove(Q, ad)
				}
			}
			if (ac.length) {
				if (X) {
					Z = true
				}
				this.length += ac.length;
				if (T != null) {
					x.apply(this.models, [T, 0].concat(ac))
				} else {
					H.apply(this.models, ac)
				}
			}
			if (Z) {
				this.sort({
					silent: true
				})
			}
			if (ad.silent) {
				return this
			}
			for (Y = 0, U = ac.length; Y < U; Y++) {
				(aa = ac[Y])
				.trigger("add", aa, this, ad)
			}
			if (Z) {
				this.trigger("sort", this, ad)
			}
			return this
		},
		reset: function(T, R) {
			R || (R = {});
			for (var S = 0, Q = this.models.length; S < Q; S++) {
				this._removeReference(this.models[S])
			}
			R.previousModels = this.models;
			this._reset();
			this.add(T, P.extend({
				silent: true
			}, R));
			if (!R.silent) {
				this.trigger("reset", this, R)
			}
			return this
		},
		push: function(R, Q) {
			R = this._prepareModel(R, Q);
			this.add(R, P.extend({
				at: this.length
			}, Q));
			return R
		},
		pop: function(R) {
			var Q = this.at(this.length - 1);
			this.remove(Q, R);
			return Q
		},
		unshift: function(R, Q) {
			R = this._prepareModel(R, Q);
			this.add(R, P.extend({
				at: 0
			}, Q));
			return R
		},
		shift: function(R) {
			var Q = this.at(0);
			this.remove(Q, R);
			return Q
		},
		slice: function(R, Q) {
			return this.models.slice(R, Q)
		},
		get: function(Q) {
			if (Q == null) {
				return void 0
			}
			return this._byId[Q.id != null ? Q.id : Q.cid || Q]
		},
		at: function(Q) {
			return this.models[Q]
		},
		where: function(Q, R) {
			if (P.isEmpty(Q)) {
				return R ? void 0 : []
			}
			return this[R ? "find" : "filter"](function(S) {
				for (var T in Q) {
					if (Q[T] !== S.get(T)) {
						return false
					}
				}
				return true
			})
		},
		findWhere: function(Q) {
			return this.where(Q, true)
		},
		sort: function(Q) {
			if (!this.comparator) {
				throw new Error("Cannot sort a set without a comparator")
			}
			Q || (Q = {});
			if (P.isString(this.comparator) || this.comparator.length === 1) {
				this.models = this.sortBy(this.comparator, this)
			} else {
				this.models.sort(P.bind(this.comparator, this))
			}
			if (!Q.silent) {
				this.trigger("sort", this, Q)
			}
			return this
		},
		sortedIndex: function(Q, T, R) {
			T || (T = this.comparator);
			var S = P.isFunction(T) ? T : function(U) {
				return U.get(T)
			};
			return P.sortedIndex(this.models, Q, S, R)
		},
		pluck: function(Q) {
			return P.invoke(this.models, "get", Q)
		},
		fetch: function(Q) {
			Q = Q ? P.clone(Q) : {};
			if (Q.parse === void 0) {
				Q.parse = true
			}
			var S = Q.success;
			var R = this;
			Q.success = function(T) {
				var U = Q.reset ? "reset" : "set";
				R[U](T, Q);
				if (S) {
					S(R, T, Q)
				}
				R.trigger("sync", R, T, Q)
			};
			L(this, Q);
			return this.sync("read", this, Q)
		},
		create: function(R, Q) {
			Q = Q ? P.clone(Q) : {};
			if (!(R = this._prepareModel(R, Q))) {
				return false
			}
			if (!Q.wait) {
				this.add(R, Q)
			}
			var T = this;
			var S = Q.success;
			Q.success = function(U) {
				if (Q.wait) {
					T.add(R, Q)
				}
				if (S) {
					S(R, U, Q)
				}
			};
			R.save(null, Q);
			return R
		},
		parse: function(R, Q) {
			return R
		},
		clone: function() {
			return new this.constructor(this.models)
		},
		_reset: function() {
			this.length = 0;
			this.models = [];
			this._byId = {}
		},
		_prepareModel: function(S, R) {
			if (S instanceof I) {
				if (!S.collection) {
					S.collection = this
				}
				return S
			}
			R || (R = {});
			R.collection = this;
			var Q = new this.model(S, R);
			if (!Q._validate(S, R)) {
				this.trigger("invalid", this, S, R);
				return false
			}
			return Q
		},
		_removeReference: function(Q) {
			if (this === Q.collection) {
				delete Q.collection
			}
			Q.off("all", this._onModelEvent, this)
		},
		_onModelEvent: function(S, R, T, Q) {
			if ((S === "add" || S === "remove") && T !== this) {
				return
			}
			if (S === "destroy") {
				this.remove(R, Q)
			}
			if (R && S === "change:" + R.idAttribute) {
				delete this._byId[R.previous(R.idAttribute)];
				if (R.id != null) {
					this._byId[R.id] = R
				}
			}
			this.trigger.apply(this, arguments)
		}
	});
	var C = ["forEach", "each", "map", "collect", "reduce", "foldl", "inject", "reduceRight", "foldr", "find", "detect", "filter", "select", "reject", "every", "all", "some", "any", "include", "contains", "invoke", "max", "min", "toArray", "size", "first", "head", "take", "initial", "rest", "tail", "drop", "last", "without", "indexOf", "shuffle", "lastIndexOf", "isEmpty", "chain"];
	P.each(C, function(Q) {
		c.prototype[Q] = function() {
			var R = q.call(arguments);
			R.unshift(this.models);
			return P[Q].apply(P, R)
		}
	});
	var m = ["groupBy", "countBy", "sortBy"];
	P.each(m, function(Q) {
		c.prototype[Q] = function(T, R) {
			var S = P.isFunction(T) ? T : function(U) {
				return U.get(T)
			};
			return P[Q](this.models, S, R)
		}
	});
	var K = D.View = function(Q) {
		this.cid = P.uniqueId("view");
		this._configure(Q || {});
		this._ensureElement();
		this.initialize.apply(this, arguments);
		this.delegateEvents()
	};
	var z = /^(\S+)\s*(.*)$/;
	var e = ["model", "collection", "el", "id", "attributes", "className", "tagName", "events"];
	P.extend(K.prototype, N, {
		tagName: "div",
		$: function(Q) {
			return this.$el.find(Q)
		},
		initialize: function() {},
		render: function() {
			return this
		},
		remove: function() {
			this.$el.remove();
			this.stopListening();
			return this
		},
		setElement: function(Q, R) {
			if (this.$el) {
				this.undelegateEvents()
			}
			this.$el = Q instanceof D.$ ? Q : D.$(Q);
			this.el = this.$el[0];
			if (R !== false) {
				this.delegateEvents()
			}
			return this
		},
		delegateEvents: function(U) {
			if (!(U || (U = P.result(this, "events")))) {
				return this
			}
			this.undelegateEvents();
			for (var T in U) {
				var V = U[T];
				if (!P.isFunction(V)) {
					V = this[U[T]]
				}
				if (!V) {
					continue
				}
				var S = T.match(z);
				var R = S[1],
					Q = S[2];
				V = P.bind(V, this);
				R += ".delegateEvents" + this.cid;
				if (Q === "") {
					this.$el.on(R, V)
				} else {
					this.$el.on(R, Q, V)
				}
			}
			return this
		},
		undelegateEvents: function() {
			this.$el.off(".delegateEvents" + this.cid);
			return this
		},
		_configure: function(Q) {
			if (this.options) {
				Q = P.extend({}, P.result(this, "options"), Q)
			}
			P.extend(this, P.pick(Q, e));
			this.options = Q
		},
		_ensureElement: function() {
			if (!this.el) {
				var Q = P.extend({}, P.result(this, "attributes"));
				if (this.id) {
					Q.id = P.result(this, "id")
				}
				if (this.className) {
					Q["class"] = P.result(this, "className")
				}
				var R = D.$("<" + P.result(this, "tagName") + ">")
					.attr(Q);
				this.setElement(R, false)
			} else {
				this.setElement(P.result(this, "el"), false)
			}
		}
	});
	D.sync = function(W, R, Q) {
		var T = l[W];
		P.defaults(Q || (Q = {}), {
			emulateHTTP: D.emulateHTTP,
			emulateJSON: D.emulateJSON
		});
		var V = {
			type: T,
			dataType: "json"
		};
		if (!Q.url) {
			V.url = P.result(R, "url") || u()
		}
		if (Q.data == null && R && (W === "create" || W === "update" || W === "patch")) {
			V.contentType = "application/json";
			V.data = JSON.stringify(Q.attrs || R.toJSON(Q))
		}
		if (Q.emulateJSON) {
			V.contentType = "application/x-www-form-urlencoded";
			V.data = V.data ? {
				model: V.data
			} : {}
		}
		if (Q.emulateHTTP && (T === "PUT" || T === "DELETE" || T === "PATCH")) {
			V.type = "POST";
			if (Q.emulateJSON) {
				V.data._method = T
			}
			var S = Q.beforeSend;
			Q.beforeSend = function(X) {
				X.setRequestHeader("X-HTTP-Method-Override", T);
				if (S) {
					return S.apply(this, arguments)
				}
			}
		}
		if (V.type !== "GET" && !Q.emulateJSON) {
			V.processData = false
		}
		if (V.type === "PATCH" && window.ActiveXObject && !(window.external && window.external.msActiveXFilteringEnabled)) {
			V.xhr = function() {
				return new ActiveXObject("Microsoft.XMLHTTP")
			}
		}
		var U = Q.xhr = D.ajax(P.extend(V, Q));
		R.trigger("request", R, U, Q);
		return U
	};
	var l = {
		create: "POST",
		update: "PUT",
		patch: "PATCH",
		"delete": "DELETE",
		read: "GET"
	};
	D.ajax = function() {
		return D.$.ajax.apply(D.$, arguments)
	};
	var s = D.Router = function(Q) {
		Q || (Q = {});
		if (Q.routes) {
			this.routes = Q.routes
		}
		this._bindRoutes();
		this.initialize.apply(this, arguments)
	};
	var t = /\((.*?)\)/g;
	var v = /(\(\?)?:\w+/g;
	var d = /\*\w+/g;
	var j = /[\-{}\[\]+?.,\\\^$|#\s]/g;
	P.extend(s.prototype, N, {
		initialize: function() {},
		route: function(R, S, T) {
			if (!P.isRegExp(R)) {
				R = this._routeToRegExp(R)
			}
			if (P.isFunction(S)) {
				T = S;
				S = ""
			}
			if (!T) {
				T = this[S]
			}
			var Q = this;
			D.history.route(R, function(V) {
				var U = Q._extractParameters(R, V);
				T && T.apply(Q, U);
				Q.trigger.apply(Q, ["route:" + S].concat(U));
				Q.trigger("route", S, U);
				D.history.trigger("route", Q, S, U)
			});
			return this
		},
		navigate: function(R, Q) {
			D.history.navigate(R, Q);
			return this
		},
		_bindRoutes: function() {
			if (!this.routes) {
				return
			}
			this.routes = P.result(this, "routes");
			var R, Q = P.keys(this.routes);
			while ((R = Q.pop()) != null) {
				this.route(R, this.routes[R])
			}
		},
		_routeToRegExp: function(Q) {
			Q = Q.replace(j, "\\$&")
				.replace(t, "(?:$1)?")
				.replace(v, function(S, R) {
					return R ? S : "([^/]+)"
				})
				.replace(d, "(.*?)");
			return new RegExp("^" + Q + "$")
		},
		_extractParameters: function(Q, R) {
			var S = Q.exec(R)
				.slice(1);
			return P.map(S, function(T) {
				return T ? decodeURIComponent(T) : null
			})
		}
	});
	var k = D.History = function() {
		this.handlers = [];
		P.bindAll(this, "checkUrl");
		if (typeof window !== "undefined") {
			this.location = window.location;
			this.history = window.history
		}
	};
	var E = /^[#\/]|\s+$/g;
	var f = /^\/+|\/+$/g;
	var M = /msie [\w.]+/;
	var p = /\/$/;
	k.started = false;
	P.extend(k.prototype, N, {
		interval: 50,
		getHash: function(R) {
			var Q = (R || this)
				.location.href.match(/#(.*)$/);
			return Q ? Q[1] : ""
		},
		getFragment: function(S, R) {
			if (S == null) {
				if (this._hasPushState || !this._wantsHashChange || R) {
					S = this.location.pathname;
					var Q = this.root.replace(p, "");
					if (!S.indexOf(Q)) {
						S = S.substr(Q.length)
					}
				} else {
					S = this.getHash()
				}
			}
			return S.replace(E, "")
		},
		start: function(S) {
			if (k.started) {
				throw new Error("Backbone.history has already been started")
			}
			k.started = true;
			this.options = P.extend({}, {
				root: "/"
			}, this.options, S);
			this.root = this.options.root;
			this._wantsHashChange = this.options.hashChange !== false;
			this._wantsPushState = !!this.options.pushState;
			this._hasPushState = !!(this.options.pushState && this.history && this.history.pushState);
			var R = this.getFragment();
			var Q = document.documentMode;
			var U = (M.exec(navigator.userAgent.toLowerCase()) && (!Q || Q <= 7));
			this.root = ("/" + this.root + "/")
				.replace(f, "/");
			if (U && this._wantsHashChange) {
				this.iframe = D.$('<iframe src="javascript:0" tabindex="-1" />')
					.hide()
					.appendTo("body")[0].contentWindow;
				this.navigate(R)
			}
			if (this._hasPushState) {
				D.$(window)
					.on("popstate", this.checkUrl)
			} else {
				if (this._wantsHashChange && ("onhashchange" in window) && !U) {
					D.$(window)
						.on("hashchange", this.checkUrl)
				} else {
					if (this._wantsHashChange) {
						this._checkUrlInterval = setInterval(this.checkUrl, this.interval)
					}
				}
			}
			this.fragment = R;
			var V = this.location;
			var T = V.pathname.replace(/[^\/]$/, "$&/") === this.root;
			if (this._wantsHashChange && this._wantsPushState && !this._hasPushState && !T) {
				this.fragment = this.getFragment(null, true);
				this.location.replace(this.root + this.location.search + "#" + this.fragment);
				return true
			} else {
				if (this._wantsPushState && this._hasPushState && T && V.hash) {
					this.fragment = this.getHash()
						.replace(E, "");
					this.history.replaceState({}, document.title, this.root + this.fragment + V.search)
				}
			}
			if (!this.options.silent) {
				return this.loadUrl()
			}
		},
		stop: function() {
			D.$(window)
				.off("popstate", this.checkUrl)
				.off("hashchange", this.checkUrl);
			clearInterval(this._checkUrlInterval);
			k.started = false
		},
		route: function(Q, R) {
			this.handlers.unshift({
				route: Q,
				callback: R
			})
		},
		checkUrl: function(R) {
			var Q = this.getFragment();
			if (Q === this.fragment && this.iframe) {
				Q = this.getFragment(this.getHash(this.iframe))
			}
			if (Q === this.fragment) {
				return false
			}
			if (this.iframe) {
				this.navigate(Q)
			}
			this.loadUrl() || this.loadUrl(this.getHash())
		},
		loadUrl: function(S) {
			var R = this.fragment = this.getFragment(S);
			var Q = P.any(this.handlers, function(T) {
				if (T.route.test(R)) {
					T.callback(R);
					return true
				}
			});
			return Q
		},
		navigate: function(S, R) {
			if (!k.started) {
				return false
			}
			if (!R || R === true) {
				R = {
					trigger: R
				}
			}
			S = this.getFragment(S || "");
			if (this.fragment === S) {
				return
			}
			this.fragment = S;
			var Q = this.root + S;
			if (this._hasPushState) {
				this.history[R.replace ? "replaceState" : "pushState"]({}, document.title, Q)
			} else {
				if (this._wantsHashChange) {
					this._updateHash(this.location, S, R.replace);
					if (this.iframe && (S !== this.getFragment(this.getHash(this.iframe)))) {
						if (!R.replace) {
							this.iframe.document.open()
								.close()
						}
						this._updateHash(this.iframe.location, S, R.replace)
					}
				} else {
					return this.location.assign(Q)
				}
			}
			if (R.trigger) {
				this.loadUrl(S)
			}
		},
		_updateHash: function(Q, S, T) {
			if (T) {
				var R = Q.href.replace(/(javascript:|#).*$/, "");
				Q.replace(R + "#" + S)
			} else {
				Q.hash = "#" + S
			}
		}
	});
	D.history = new k;
	var n = function(Q, S) {
		var R = this;
		var U;
		if (Q && P.has(Q, "constructor")) {
			U = Q.constructor
		} else {
			U = function() {
				return R.apply(this, arguments)
			}
		}
		P.extend(U, R, S);
		var T = function() {
			this.constructor = U
		};
		T.prototype = R.prototype;
		U.prototype = new T;
		if (Q) {
			P.extend(U.prototype, Q)
		}
		U.__super__ = R.prototype;
		return U
	};
	I.extend = c.extend = s.extend = K.extend = k.extend = n;
	var u = function() {
		throw new Error('A "url" property or function must be specified')
	};
	var L = function(S, R) {
		var Q = R.error;
		R.error = function(T) {
			if (Q) {
				Q(S, T, R)
			}
			S.trigger("error", S, T, R)
		}
	}
})
.call(this);