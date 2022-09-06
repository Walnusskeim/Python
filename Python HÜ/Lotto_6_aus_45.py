'''
Lotto Simulation bei der der Computer sechs zufällig generierte Zahlen erstellt
und der User sie auf Anhieb erraten muss.
31.01.22
Maximilian
'''

import random

#empty list to hold lotto numbers
lotto_numbers = []

#add the random numbers to the list
while (len(lotto_numbers) < 6):
    zz = random.randint(1,45)
    if (zz not in lotto_numbers):
        lotto_numbers.append(zz)

#ask the user to insert random numbers      
while(True):
        user_input = int(input("Bitte gib deine Lottozahlen (zwischen 1 und 45) ein: "))
        if (user_input > 45):
            print("Die höchste Zahl beträgt 45. Versuch es noch mal.")
        elif (user_input < 1):
            print("Die niedrigste Zahl beträgt 1. Versuch es noch mal.")
        else:
            lotto_numbers.append(user_input)
        if (user_input == 'end'):
            break


#reveal the generated numbers
print(lotto_numbers)

