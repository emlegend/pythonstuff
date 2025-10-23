print("Tag des Datums eingeben:")
T = input()
T = int(T)
if T < 31:
    print("ok")
else:
    exit("ivalid")

print("Monat des Datums eingeben:")
M = input()
M = int(M)
if M <= 12 :
    print("ok")
else:
    exit("ivalid")

print("letzter Tag des Datums eingeben:")
LT = input()
LT = int(LT)
if LT == 31 or LT == 30 or LT == 28 :
    print("ok")
else:
    exit("ivalid")

if T <1 or T > LT:
    exit("ivalid")

print("Jahr eingeben:")
J = input()
J = int(J)
if J % 4 == 0:
    print("ok")
else:
    exit("ivalid")