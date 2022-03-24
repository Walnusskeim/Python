'''
Strucktrogramm
Maximilian
'''

import random


counter = 1
dice_list = [] 

while(True):
    counter1 = random.randint(1,6)
    counter2 = random.randint(1,6)
    if(counter1 and counter2 == 6):
        break
    else:
        counter = counter + 1
        d = "{} + {}".format(counter1, counter2)
        dice_list.append (d) 
        
print("Du hast {} Versuche gebraucht.".format(counter)) 
print("Das sind die Ergebinsse: {}".format(dice_list)) 
