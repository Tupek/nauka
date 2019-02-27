def max_length(txt):
    wordlist = []
    for word in txt:
        if len(word) > 4:
            continue
        wordlist += [word]
    return wordlist

l = ["Kami", "siedzial", "na", "stole", "i", "patrzyl", "na", "czajnik"]
list = max_length(l)
print(list)

