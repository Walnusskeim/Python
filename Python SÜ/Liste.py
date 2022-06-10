'''
Der User darf ahlen (oder'end') eingeben. Die Zahlen sollen in einer Liste
gespeichert werden. Wenn der User mit 'end' abbricht, soll die Liste mit der 
.sort() Methode sortiert werden und dann nochmals dem User mittels prin() 
Funktion ausgegeben werden.

31.01.22
Maximilian
'''

#erstellen einer list
user_input_list = []

#endlost loop der mit 'end' gebroche werden kann 
while(True):
    user_input = input("Hallo! Bitte gebe eine int Zahl ein (mit end kannst du den Loop abbrechen): ")
    if (user_input == 'end'):
        break
    #im loop die Zahlen mit input einlesen und zur Liste mit append() anhängen
    else:
        user_input = int(user_input)
        user_input_list.append(user_input)

#nach dem loop die Liste mit .sort() sortieren und mit print()ausgeben.
user_input_list.sort()
print(user_input_list)
print("Die höchste Zahl war: {}".format(max(user_input_list)))
print("Die niedrigste Zahl war: {}".format(min(user_input_list)))
