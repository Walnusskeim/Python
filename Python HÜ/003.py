'''
Drittes Übungsfile - Themen: User I/O und Verzweigungen
Vorbereitung zur Taschenrechner HÜ
Dez. 2021
Maximilian
'''

#als erstes den user nach zahlen und operator fragen
z1 = input("Bitte erste Zahl eingeben ->")
z1 = float(z1)
op = input("Bitte den operant (+,-,*,/) eingeben ->")
z2 = float (input("Bitte die zweite Zahl eingeben ->"))

erg = 0.00
#if verzweigung
if (op == "+"):
    #dieser block wird nur ausgefühlt wenn das if-statement wahr ist!!
    erg = z1 + z2
if (op == "-"):
    erg = z1 - z2
if (op == "*"):
    erg = z1 * z2
if (op == "/"):
    erg = z1 / z2

print("Erg = {:.2f}".format(erg))