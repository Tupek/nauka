def censor(args):
    cenz = ["Java", "C#", "Ruby", "PHP"]
    lista = args.split()
    for item in cenz:
        for words in lista:
            if item in words:
                pos = lista.index(words)
                lista.remove(words)
                lista.insert(pos, "****")
    return " ".join(lista)


c = censor("Java is the best, but PHP is the bestest!")  # ;-)
print (c)