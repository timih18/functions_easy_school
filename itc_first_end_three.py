def itc_first_end_three(str):
    len = 0
    for i in str:
        len += 1
    if len > 5:
        print(str[0], str[1], str[2], str[-3], str[-2], str[-1], sep='')
    else:
        print(str[0])
