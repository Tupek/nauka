def find_first_and_last(list):
    f = list[0:1]
    l = list[-1:]
    btt = [f, l]
    btt_tuple = tuple(btt)
    return btt_tuple



ha = ("mama", "kot", "pies", "Kara")
a = find_first_and_last(ha)
print(a)