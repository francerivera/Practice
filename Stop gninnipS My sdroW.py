def spin_words(sentence):
    x = sentence.split()
    i = []
    for word in x:
        if len(word) >= 5:
            i.append(word[::-1])
        else:
            i.append(word)
    return " ".join(i)
