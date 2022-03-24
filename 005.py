'''
Übung zu Funtionen
Maximilian
24.01.22
'''

def my_parallel_calc(a,b):
    r_ges = a*b/(a+b)
    return r_ges


print("### Willkommen zum Parallel-Widerstand-berechnen ###") 
r1 = float(input("Bitte den Wert von R1 in k\u03A9 eingeben ->"))
r2= float(input("Bitte den Wert von R2 in k\u03A9 eingeben ->"))
r_ges = my_parallel_calc(r1,r2)
print("R_ges={}".format(r_ges))