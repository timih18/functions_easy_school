def itc_percent_lower_uppercase(string):
    a = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё'
    b = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
    cnta = 0
    cntb = 0
    for i in string:
        if i in a:
            cnta += 1
        elif i in b:
            cntb += 1
    if cnta + cntb == 0:
        res = 0
    else:
        res = cnta * 100 / (cnta + cntb)
    return res
