#Funcja sprawdza czy słowo jest palindromem np. Ala
def check_palindrome():
    x = input("Wprowadz slowo: ")
    x = x.lower()                       #zmiana liter na male
    if x == x[::-1]:
        return True
    else:
        return False

print(check_palindrome())