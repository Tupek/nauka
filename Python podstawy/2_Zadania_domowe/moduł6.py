def is_divided_by_4 (x):
    z = x % 4
    return z

num = int(input("Podaj liczbe do sprawdzenia: "))
num_check = is_divided_by_4(num)

print("Podana liczba jest podzielna przez 4:", num_check == 0)
