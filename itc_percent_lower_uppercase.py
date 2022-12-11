def itc_percent_lower_uppercase(string):
    up = 0
    low = 0
    len = 0
    for i in string:
        len += 1
    for i in range(len):
        if string[i] >= 'A' and string[i] <= 'Z':
            up += 1
        elif string[i] >= 'a' and string[i] <= 'z':
            low += 1
    return (up/low)*100
