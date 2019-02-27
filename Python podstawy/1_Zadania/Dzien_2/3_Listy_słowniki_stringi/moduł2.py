def list_keys(d):
    for i in d:
        print(i, d[i], sep = " : ")


blabla = {
    "episode" : 4,
    "title" : "A New Hope"
    }
keys = list_keys(blabla)
