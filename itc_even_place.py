def itc_even_place(str):
    s = ''
    len = 0
    for i in str:
        len += 1
    for i in range(1, len+1):
        if i % 2 == 0:
            s = s + str[i-1]
    if s == '':
        return -1
    else:
        return s
