def naive(st, text):
    ls = len(st)
    lps = len(text)
    n = 0
    for i in range(ls - lps + 1):
        n += 1
        if st[i] == text[0]:
            for j in range(1, lps):
                n += 1
                if st[i + j] != text[j]:
                    break
                if j == lps - 1:
                    print(n, ' сравнений')
                    return i
    print(n, ' сравнений')
    return None