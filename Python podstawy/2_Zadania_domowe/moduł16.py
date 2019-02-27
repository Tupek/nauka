def div():
    try:
        a = input("Podaj pierwsza liczbe: ")
        b = input("Podaj druga liczbe: ")
        a = int(a)
        b = int(b)
        if a < 0:
            a = a - a - a
        elif b < 0:
            b = b - b - b
        else:
            pass
        try:
            return a / b
        except ZeroDivisionError:
            return None
    except ValueError:
        return None

    

c = div()
print(c)