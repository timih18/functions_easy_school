def itc_cmp_str(str1, str2, num):
    cnt2 = 0
    cnt1 = 0
    for i in str1:
        cnt1 += 1
    for i in str2:
        cnt2 += 1
    if str2 == '':
        return str1
    elif cnt2 > cnt1 - num:
        s = str1[:num] + str2[:cnt1-num]
        return s
    else:
        s = str1[:num] + str2 + str1[num+cnt2:]
        return s
