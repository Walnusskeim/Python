'''
Taschenrechner mit Funktionen
Zusammenarbeit mit Berat Aybak
Maximilian
May 2022
'''


def plus(z1, z2):
    erg = 0
    erg = z1 + z2
    return erg

def minus(z1, z2):
    erg = 0
    erg = z1 - z2
    return erg

def mal(z1, z2):
    erg = 0
    erg = z1 * z2
    return erg

def dividieren(z1, z2):
    erg = 0
    erg = z1 / z2
    return erg

print("████████╗ █████╗ ███████╗ ██████╗██╗  ██╗███████╗███╗   ██╗██████╗ ███████╗ ██████╗██╗  ██╗███╗   ██╗███████╗██████╗")
print("╚══██╔══╝██╔══██╗██╔════╝██╔════╝██║  ██║██╔════╝████╗  ██║██╔══██╗██╔════╝██╔════╝██║  ██║████╗  ██║██╔════╝██╔══██╗")
print("   ██║   ███████║███████╗██║     ███████║█████╗  ██╔██╗ ██║██████╔╝█████╗  ██║     ███████║██╔██╗ ██║█████╗  ██████╔╝")
print("   ██║   ██╔══██║╚════██║██║     ██╔══██║██╔══╝  ██║╚██╗██║██╔══██╗██╔══╝  ██║     ██╔══██║██║╚██╗██║██╔══╝  ██╔══██╗")
print("   ██║   ██║  ██║███████║╚██████╗██║  ██║███████╗██║ ╚████║██║  ██║███████╗╚██████╗██║  ██║██║ ╚████║███████╗██║  ██║")
print("   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝")
print("##############################################################################################################################")
print("##############################################################################################################################")


while True:
    erg = 0
    z1 = float(input("Bitte erste Zahl eingeben ->"))
    op = input("Bitte den Operant (+,-,*,/) eingeben ->")
    z2 = float(input("Bitte die zweite Zahl eingeben ->"))

    if (op == "+"):
        erg = plus(z1, z2)
    if (op == "-"):
        erg = minus(z1, z2)
    if (op == "*"):
        erg = mal(z1, z2)
    if (op == "/"):
        erg = dividieren(z1, z2)

    print("Das ergebnis ist{}".format(erg))