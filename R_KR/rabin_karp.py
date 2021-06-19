def calc_hash(h, wp, wn, lps, p, x):
    h = ((h - ord(wp)*(x**(lps - 1)))*x + ord(wn)) % p
    return h


def str_check(s1, s2):
    n = 0
    for i in range(len(s1)):
        n += 1
        if s1[i] != s2[i]:
            return (0, n)
    return (1, n)


def rabin(s, ps, p):
    n = 0
    x = random.randint(0, p - 1)
    ls = len(s)
    lps = len(ps)
    h = sum(ord(s[i - 1])*(x**(lps - i)) for i in range(1, lps)) % p
    hps = sum(ord(ps[i - 1])*(x**(lps - i)) for i in range(1, lps)) % p
    n += 1
    if h == hps:
        ch = str_check(s[0:lps], ps)
        n += ch[1]
        if ch[0]:
            print(n, ' сравнений')
            return 0
    for i in range(1, ls - lps + 1):
        h = sum(ord(s[i + j - 1])*(x**(lps - j)) for j in range(1, lps)) % p
        n += 1
        if h == hps:
            ch = str_check(s[i:i + lps], ps)
            n += ch[1]
            if ch[0]:
                print(n, ' сравнений')
                return i
    print(n, ' сравнений')
    return None