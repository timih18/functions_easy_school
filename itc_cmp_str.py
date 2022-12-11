def itc_cmp_str(string1, string2, num):
    sp1 = [char for char in string1]
    sp2 = [char for char in string2]
    c1 = 0
    c2 = 0
    res = ""
    result = ""
    for i in string1:
        c1 += 1
    for i in string2:
        c2 += 1
    for i in range(num):
        res += sp1[i]
    for i in range(c2):
        res += sp2[i]
    for i in range(num, c1):
        res += sp1[i]
    for i in range(c1):
        result += res[i]
    return result
