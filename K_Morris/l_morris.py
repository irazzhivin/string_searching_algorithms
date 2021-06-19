def form_pi(ps):
    output = [0]
    for i in range(1, len(st)):
        j = output[i - 1]
        while j > 0 and st[j] != st[i]:
            j = output[j - 1]
        if st[j] == st[i]:
            j = j + 1
        output.append(j)
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