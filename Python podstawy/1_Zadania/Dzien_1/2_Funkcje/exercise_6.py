def calculate_net(x, y):
    z = (x / (y + 1))
    return z

gross = int(input("Podaj wartosc brutto: "))
vat = float(input("Podaj stawke vat: "))
if (vat >= 1):
    vat = vat / 100
else:
    vat = vat

netto = calculate_net(gross, vat)

print("Wartosc netto: ", netto)
#
