def itc_first_end_three(str):
    len = 0
    for i in str:
        len += 1
    if len > 5:
        s = str[0] + str[1] + str[2] + str[-3] + str[-2] + str[-1]
        return s
    else:
        s = str[0]*len
        return s
