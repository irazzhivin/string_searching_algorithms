def boyer_moore_horspool(st, subst):
    indices = []  # index massive
    compares = 0
    unique = set()  # substr unic symbols 
    offsets = {}  # offsets alphabet
    # offsets alphabet initilization
    # move all symbols, but not move last
    for i in range(len(subst) - 2, -1, -1):  # before lasr
        if subst[i] not in unique:  # condition if symb no add into alphabet
            unique.add(subst[i])
            offsets[subst[i]] = len(subst) - i - 1  # m=6
    # move last symb
    if subst[len(subst) - 1] not in unique:
        offsets[subst[len(subst) - 1]] = len(subst)
    # move for others
    offsets['*'] = len(subst)
    # search substr in str
    k = len(subst) - 1
    while k < len(st):
        compares += 1
        j = len(subst) - 1  # count for checked symb in substr
        i = k  # count for checked symb in main str
        while j >= 0 and st[i] == subst[j]:
            compares += 2
            j -= 1
            i -= 1
        compares += 1
        if j == len(subst) - 1:  # last symb not same
            if offsets.get(st[i]) is None:
                off = offsets['*']
            else:
                off = offsets[st[i]]
        else:  # symb not same except last
            off = offsets[subst[j]]
        compares += 1
        if j == -1:  # FIND successfully!!!
            indices.append(i + 1)

        k += off

    return indices, compares
