b = 18
b = int (b)
c = 22
c =int(c)

print("Geben sie ihr Gehalt in euro ein")
a =  input()
a = int(a)
print("Geben sie ihr  in Zivilstand  ein (ledig oder verheiratet )")
zivilstand = input()


if a <= 2500 and zivilstand == ledig:
 X =  a/100*18
elif a <= 2500 and zivilstand == verheiratet:
 X = a / 100 * 16

elif a > 4000 and zivilstand == ledig :
 X = a / 100 * 30
elif a > 4000 and zivilstand == verheiratet:
    X = a/100*26

elif zivilstand == ledig:
    X = a/100*20

else:
    X = a/100*22

print("es ergibt sich ein Betrag von", X, "euro")