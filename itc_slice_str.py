def itc_slice_str(str, start, end):
    cnt = -1
    for i in str:
        cnt += 1
    if start > end:
        return str
    elif end > cnt:
        return str[start:]
    else:
        return str[start:end]
