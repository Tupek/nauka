def divide(a, b):
    try:
        a = int(a)
        b = int(b)
        if a <= 0 or b <= 0:
            print("none")
        else:
            print("Ok")
    except ValueError:
        print("none")

a = input("Wprowadz pierwsza liczbe: ")
b = input("Wprowadz druga licze: ")

f = divide(a, b)