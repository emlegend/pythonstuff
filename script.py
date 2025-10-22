#RNg
import random
random.seed()
# Werte und Berechnung
a = random.randint(1, 10)
b = random.randint(1, 1)
c = a + b
print("Die Aufgabe:",a, "+",b)

# Eingabe
print("Bitte eine Zahl eingeben:")
z = input()

#Eingabe in eine Zahl umwandeln
zahl = int(z)

#Ausgabe
if zahl == c:
    print(zahl,"ist richtig")
else:
    print(zahl,"falsch")
    print("ergebnis:", c)
