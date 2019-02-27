from random import randint

guessed = False
rnd = randint(1, 10)
print("Zgaduj zgadula!!!")
while True:
    try:
        while not guessed:
            str_num = input("Podaj liczbę 1 - 10:")
            num = int(str_num)
            if num > 10 or num < 1:
                print("Liczby w przedziale 1 - 10.")
            elif num == rnd:
                print("Brawo!")
                guessed = True
            else:
                print("Pudło!")
    except ValueError:
        print("To nie jest liczba!"
                "Spróbuj ponownie.")
