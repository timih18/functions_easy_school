def itc_max_char_on_end(str):
    a = '1234567890'
    len = 0
    max = 0
    cnt = 0
    for i in str:
        len += 1
    for i in range(len):
        cnt = 0
        if str[i] in a:
            cnt = 1
            for z in range(i+1, len):
                if str[z] in a:
                    cnt += 1
                else:
                    break
        if cnt > max:
            max = cnt
    return max
