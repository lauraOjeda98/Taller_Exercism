num = (
       ("M", 1000),
       ("CM", 900),
       ("D", 500),
       ("CD", 400),
       ("C", 100),
       ("XC", 90),
       ("L", 50),
       ("XL", 40),
       ("X", 10),
       ("IX", 9),
       ("V", 5),
       ("IV", 4),
       ("I", 1)
       )


def roman(number):
    roman = []
    for i in range(len(num)):
        count = int(number/num[i][1])
        roman.append(num[i][0]*count)
        number -= num[i][1]*count
    resp = "".join(roman)
    return resp
