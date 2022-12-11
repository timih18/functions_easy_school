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
def itc_three_str(str1, str2, str3):
    len1 = 0
    len2 = 0
    for i in str1:
        len1 += 1
    for i in str2:
        len2 += 1
    start = 0
    while itc_find_str(str1, str2) != -1:
        part1 = ''
        part2 = ''
        start = itc_find_str(str1, str2)
        for i in range(start):
            part1 += str1[i]
        for i in range(start+len2, len1):
            part2 += str1[i]
        str1 = part1 + str3 + part2
    return str1
