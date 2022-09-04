
def betrag(zahl):
    if zahl < 0:
        return -zahl
    else:
        return zahl

def factorial(zahl):
    result = 1
    for i in range(2, zahl + 1):
        result *= i
    return result

while True:
    eingabe = input("Zahl eingeben: ")
    if eingabe == "exit":
        print("Programm beendet")
        break
    else:
        eingabe = int(eingabe)
        if eingabe <0:
            eingabe = betrag(eingabe)
    ergebnis = factorial(eingabe)
    print("Die Fakultät der Zahl {} ist {}".format(eingabe, ergebnis))
