def itc_equal_reverse(str):
    cnt = 0
    res = 0
    for i in str:
        cnt += 1
    for i in range(cnt):
        if str[i] != str[-1-i]:
            res = 1
    if res == 1:
        return False
    else:
        return True
