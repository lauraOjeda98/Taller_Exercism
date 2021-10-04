def is_isogram(string):
    result = False
    string = string.replace("-", "").replace(" ", "").lower()
    if len(string) == len(set(string)):
        result = True

    return result
