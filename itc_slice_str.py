def itc_slice_str(string, start, end):
    sp = [char for char in string]
    res = ""
    c = 0
    for i in sp:
        c += 1
    if start > c:
        for i in sp:
            res += i
        return res
    elif end > c:
        for i in range(start-1, c):
            res += sp[i]
        return res
    elif start < end <= c:
        for i in range(start-1, end):
            res += sp[i]
        return res
