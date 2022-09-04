
def div_and_round(a,b,c=None):
    erg = a / b
    return round(erg, c)

#Aufruf mit nur zwei Parametern
print(div_and_round(12,7))

#Aufrufe mit dem optionalen dritten Parameter
print(div_and_round(12,7,2))
print(div_and_round(12,7,5))


def summe(a,b,*weitere):
    erg = a + b
    for x in weitere:
        erg = erg + x
    return erg

#Aufruf mit nur zwei Parametern
print(summe(12,7))
#Aufruf mit beliebig vielen Parametern
print(summe(12,7,6,7,12))
print(summe(12,7,45,3,9,2,13))
