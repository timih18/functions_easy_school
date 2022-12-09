def itc_three_str(str1, str2, str3):
    len1 = 0
    len2 = 0
    a = []
    for i in str1:
        len1 += 1
        a.append(i)
    for i in str2:
        len2 += 1
    for i in range(len1):
        if ''.join(a[i:len2+i]) == str2:
            a[i:len2+i] = str3
    return ''.join(a)
