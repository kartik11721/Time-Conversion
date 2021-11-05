# Time Conversion -by Kartik Kumar

def timeConversion(s):
    if s[-2] == 'P':
        if int(s[0]) == 1 and int(s[1]) == 2:
            s = s.replace(s[:2],'12')
        else:
            hh = str(12 +int(n := s[0:2]))
            s = s.replace(n,hh)
        s = s[:8]
    else:
        if int(s[0]) == 1 and int(s[1]) == 2:
            s = s.replace(s[:2],'00')
        s = s[:8]
    return s


# Put the time in here :-

print(timeConversion('04:59:59PM'))