def itc_max_char_on_end(string):
    cnt = 0
    len = 0
    cnt_max = 0
    for i in string:
        len += 1
    for i in range(len):
        if string[i] >= '0' and string[i] <= '9':
            cnt += 1
            if cnt > cnt_max:
                cnt_max = cnt
        else:
            cnt = 0
    return cnt_max
