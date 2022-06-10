'''
Wiederholung am 28.02.2022
Maximilian
'''

x = inout("Bitte eine Zahl eingeben:")
print("x hat den datentyp {}".format(type(x)))

y = int(x)
print("y hat den daten-typ {}".format(type(y)))

if (y < 0):
    print("y ist negativ")
elif (y > 0):
    print("y ist positiv)
else:
    print("y ist genau Null") 
    
while (y >= 0):
    print(y)
    y = y - 1 
   
b = "hello berat"

for buchstabe in b:
    print(buchstabe) 

my_emty_List = []
my_second_list = ["hello", "Max", 12, 13.345]

for eintrag in my_second_list:
    print(eintrag)
    
print(my_second_list[1]) 