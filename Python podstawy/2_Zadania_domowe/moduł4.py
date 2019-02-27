age = float(input("Podaj wiek psa: "))
if (age <= 2):
    def dogs_age(x, y = 10.5):
        z = x * y
        return z
else:
    def dogs_age(x, y = 4, c = 21):
        z = (x - 2) * y + c
        return z

dog = dogs_age(age)
print("Wiek psa w psich latach to: ", dog)