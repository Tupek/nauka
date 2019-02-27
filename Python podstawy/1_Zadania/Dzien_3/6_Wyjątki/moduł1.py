def safe_get(l):
    while True:
        try:
            x = input("Wprowadz index: ")
            index = int(x)
            print(l[index])
            break
        except ValueError:
            print("To nie jest licza!"
                  "Spróbuj ponownie.")
        except IndexError:
            print("W tablicy nie ma"
                  "takiego elementu!")

heroes = ["Harry", "Ron", "Hermione"]
a = safe_get(heroes)
