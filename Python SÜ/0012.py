'''
More functions
Maximilian
28.03.22
'''

def spannungsteiler(r1,r2,u_ges):
    u1 = r1*(u_ges/(r1+r2))
    u2 = r2*(u_ges/(r1+r2))
    reutrn (u1,u2)

def stromteiler(r1,r2,I_ges):
    i1 = I_ges*(R_ges/r1)
    i2 = I_ges*(R_ges/r2)

### main part
print("### Willkommen zum Spannungsteiler rechnen! ###")
ui = input("Für Spannungsteiler U eingeben, für Stromteiler I.")

r1 = int(input("Bitte R1 in K\u03A9 eingeben ->"))
r2 = int(input("Bitte R1 in K\u03A9 eingeben ->"))

if(ui == 'U'):
    u = int(input("Bitte u_ges in V eingeben ->"))
    erg = spannungsteiler(r1, r2, u)
    print("U1={}V und U2={}V".format(erg[0], erg[1]))
else:
    I_ges = int(input("Bitte I_ges in mA eingeben ->"))
    erg2 = stromteiler(r1, r2, I_ges)
    print("I1={}mA und I2={}mA".format(erg[0], erg[1]))

