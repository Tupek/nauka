def square_area(x, y):
    z = x * y
    return z

first = int(input("Podaj dlugosc pierwszego boku: "))
second = int(input("Podaj dlugosc drugiego boku: "))

square = square_area(first, second)
print("Pole wynosi:", square)
