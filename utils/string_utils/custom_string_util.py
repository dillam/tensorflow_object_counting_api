
def word_count(str):
    counts = dict()
    words = str.split(":")

    for word in range(0, len(words)):
        words[word] = words[word].strip()
        if words[word] in counts:
            counts[words[word]] += 1
        else:
            counts[words[word]] = 1

    del counts['']
    return counts
