def itc_max_char_on_end(str):
    len = 0
    max = 0
    for i in str:
        len += 1
    for i in range(len):
        cnt = 1
        for z in range(i, len-1):
            if str[i] == str[z]:
                cnt += 1
        if cnt > max:
            max = cnt
        return max
