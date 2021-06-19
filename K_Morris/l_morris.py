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