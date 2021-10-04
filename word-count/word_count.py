import re


def count_words(sentence):
    words = re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower())
    result = []

    for word in words:
        result.append(words.count(word))
    countW = dict(zip(words, result))

    return countW
