def score(word):
    word = word.upper()
    resp = 0

    for char in word:
        if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'L' or char == 'N' or char == 'R' or char == 'S' or char == 'T':
            resp += (1)
        if char == 'D' or char == 'G':
            resp += (2)
        if char == 'B' or char == 'C' or char == 'M' or char == 'P':
            resp += (3)
        if char == 'F' or char == 'H' or char == 'V' or char == 'W' or char == 'Y':
            resp += (4)
        if char == 'K':
            resp += (5)
        if char == 'J' or char == 'X':
            resp += (8)
        if char == 'Q' or char == 'Z':
            resp += (10)
    return resp
