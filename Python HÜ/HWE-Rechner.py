'''
HWE-Rechner
Maximilian
May 2022
'''


def paralellschlatung(r1, r2):
    return (1/(1/r1+1/r2))

def serienschalltung(r1, r2):
    return r1+r2

def spannungsteiler(r1, r2, u_ges):
    u1 = r1 * (u_ges / (r1 + r2))
    u2 = r2 * (u_ges / (r1 + r2))
    return (u1, u2)

def stromteiler(r1, r2, i_ges):
    i1 = i_ges*((1/(1/r1+1/r2))/r1)
    i2 = i_ges*((1/(1/r1+1/r2))/r2)
    return (i1, i2)

def welcome():
        print("Willkommen zum HWE-Rechner")

while (True):
        welcome()
        choose = int(input("Willst du Stromteiler (1), Spannungsteiler(2), Paralellschaltung(3) oder Serienschaltung(4) rechnen: "))
        r1 = float(input("Gib R1 in \u03A9 ein: "))
        r2 = float(input("Gib R2 in \u03A9 ein: "))
        if (choose == 1):
            u_ges = float(input("Gib Uges in V ein: "))
            spannungsteiler(r1, r2, u_ges)
            print(" \nErgebnisse:\nU1 = {}V \nU2 = {}V".format(spannungsteiler(r1, r2, u_ges)[0],
                                                            spannungsteiler(r1, r2, u_ges)[1]))
            break
        elif (choose == 2):
            Uges = float(input("Gib Uges in V ein: "))
            stromteiler(r1, r2, i_ges)
            print(" \nErgebnisse:\nU1 = {}V \nU2 = {}V".format(spannungsteiler(r1, r2, u_ges)[0],
                                                            spannungsteiler(r1, r2, u_ges)[1]))
            break

        elif (choose == 3):
            paralellschlatung(r1, r2)
            print(" \nErgebnis:\n Rges = {}".format(paralell(r1,r2)))
            break

        elif (choose == 4):
            serienschalltung(r1, r2)
            print(" \nErgebnis:\n Rges = {}".format(serienschalltung(r1,r2)))
            break

        else:
            print("Du kannst nur 1,2,3,4 eingeben.")
            continue
