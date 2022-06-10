'''
Kleines Zahlenrate-Spiel
mit der fixen Untergrenze 0
Spieler wird nach der Übergrenze gefragt
Maximilian
Jan. 2022
'''

import random 


#user greetings and ask for upper number limit
ui = int(input("Hallo! Bitte gib ein Nummernlimit ein."))

#calculate the secret random number
z = random.randint(0,ui)

#counter variable to count the tries of the user
count = 1

#game loop starts 
while(True):
    ui = int(input("Bitte eine Zahl eingeben: ")) 
    if(ui == z):
        print("Super! Das ist die richtige Zahl.") 
        print("Du hast {} Versuche gebraucht".format(count)) 
        break 
    elif(ui > z):
        print("Deine Zahl war zu groß.")
        print("Das war dein {} versuch".format(count))
        count = count + 1 
    else: 
        print("Deine Zahl war zu klein.")
        print("Das war dein {} versuch".format(count)) 
        count = count + 1 
    
        
