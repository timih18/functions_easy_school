def itc_find_str(str1, str2):
    len2 = 0
    len1 = 0
    for i in str1:
        len1 += 1
    for i in str2:
        len2 += 1
    if str2 in str1:
        for i in range(len1):
            if str1[i] == str2[0] and str2 == str1[i:len2+i]:
                return i
    else:
        return -1
