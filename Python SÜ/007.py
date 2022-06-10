
jz = int(input("Bitte gebe eine Jahreszahl ein: "))

if(jz%4 == 0):
    if (jz%100 == 0):
        if(jz%400 == 0):
            jz = True
    else:
        jz = True

if (jz == True):
    print("Es ist ein Schaltjahr.")
else:
    print("Es ist kein Schaltjahr.")