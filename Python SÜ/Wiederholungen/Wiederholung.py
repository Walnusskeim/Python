'''
Wiederholung der Python Grundlagen
Maximilian
Jan. 2022
'''

eins = 12
zwei = 2.3456
drei = "Hello"
vier = False

#user output input
print("Guten Morgen!")
print("Der Wert von zwei = ",zwei)
print("zwei = {:.2f} un drei = {}" .format(zwei,drei))

fuenf = input("Bitte eine Zahl eingeben ->")
print("fuenf hat den datentyp: ",type(fuenf))
fuenf = float(fuenf)
print("fuenf hat den datentyp: ",type(fuenf))

x = int(input("bitte eine zahl (0-100) eingeben ->"))

if (x <= 33):
    print("Deine Eingabe wear kleiner gleich 33")
    
elif (x <= 66):
    print("Deine Eingabe war zwischen 34 und 66") 
   
else:
    print("Deine Eingabe war zwischen 67 und 100") 