def itc_cmp_str(string1, string2, num):
    fstr = ''
    nstr = ''
    len1 = 0
    len2 = 0
    for i in string1:
        len1 += 1
    for i in string2:
        len2 += 1
    if len1 < num or num < 0:
        return string1
    for i in range(num):
        nstr += string1[i]
    for i in range(len2):
        nstr += string2[i]
    for i in range(num+len2, len1):
        nstr += string1[i]
    for i in range(len1):
        fstr += nstr[i]
    return fstr
