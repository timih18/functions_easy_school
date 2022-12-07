def itc_count_char_in_str(symbol, str):
    cnt = 0
    for i in str:
        if i == symbol:
            cnt += 1
    return cnt
