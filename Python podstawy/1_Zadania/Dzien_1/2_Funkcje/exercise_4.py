# tutaj napisz funkcję z zadania 1
def convert_to_usd(zlotys, usd = 3.85):
    z = zlotys / usd
    return z
# poniższe linijki przetestują Twoją funkcję:
print("385PLN = ", convert_to_usd(385), "USD")
print("100PLN = ", convert_to_usd(100), "USD")