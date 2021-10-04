def is_armstrong_number(number):
    result = 0
    n = str(number)

    for i in n:
        result += int(i)**(len(n))
    return number == result
