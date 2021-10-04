import string


def is_pangram(sentence):
    sentence = sentence.lower()

    return set(sentence).issuperset(set(string.ascii_lowercase))
