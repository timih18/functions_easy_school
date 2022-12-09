def itc_max_char_on_end(string):
    a = '1234567890'
    length = 0
    m = 0
    for i in string:
        length += 1
    for i in range(length):
        cnt = 0
        if string[i] in a:
            cnt = 1
            for z in range(i+1, length):
                if string[z] in a:
                    cnt += 1
                else:
                    break
        if cnt > m:
            m = cnt
    return m
