def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ").replace("/", " ").replace("  ", " ").replace("#", " ")
    div_words = words.split()
    acronym = ""

    for div in div_words:
        acronym += div[0]
    return acronym.upper()
