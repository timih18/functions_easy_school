def itc_percent_lower_uppercase(str):
    a = 'qwertyuiopasdfghjklzxcvbnm'
    b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    cnta = 0
    cntb = 0
    for i in str:
        if i in a:
            cnta += 1
        elif i in b:
            cntb += 1
    res = cntb//cnta*100
    return res
