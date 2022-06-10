'''
Wiederholung am 24.01.2022
Maximilian
'''

geheim = 42;
counter = 1;

while(True):
	user_input = int(input("{}. Versuch - Bitte Zahl eingeben ->".format(counter))
	if (user_input == geheim):
		print("Bravo! Nach {} Versuchen erraten!".format(Counter))
    elif (user_input < geheim):
        print("Sorry, meine Zahl ist groesser")
    else:
        print("Sorry, meine Zahl ist kleiner")
    counter = counter + 1 