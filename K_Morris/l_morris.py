def form_pi(ps):
    pi = [0 for _ in range(len(ps))]
    i, j = 0, 1
    while j < len(ps):
        if ps[i] == ps[j]:
            pi[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                pi[j] = 0
                j += 1
            else:
                i = pi[i - 1]
    return pi


def kmp(s, ps):
    pi = form_pi(ps)
    ls = len(s)
    lps = len(ps)
    i, j = 0, 0
    n = 0
    while i < ls:
        n += 1
        if s[i] == ps[j]:
            i += 1
            j += 1
            if j == lps:
                print(n, ' сравнений')
                return i - lps
        else:
            if j == 0:
                i += 1
            else:
                j = pi[j - 1]
    print(n, ' сравнений')
    return None