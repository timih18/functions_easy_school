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
    res = cnta/cntb*100
    return res
