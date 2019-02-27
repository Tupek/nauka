def phone(numb):
        l = ["791065522", "602764904"]
        try:
                b = numb in l
                return b
## Tu nie wiem co zrobic, zeby pokazywalo blad gdy nie ma wypisanego takiego nr na liscie                      
        except Exception:
                raise ("NIe ma takiego numeru.")


numb = input(str("Podaj nr tel: "))
a = phone(numb)
print(a)