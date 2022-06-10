'''
Zweites Übungsfile - Themen: User I/O und Verzweigungen
Dez. 2021
Maximilian
'''


#nun startet das eingentliche Programm mit einer Frage and den User
#datentypen: int-Ganze, Zahl float-Kommazahl, string

user_input = input("Bitte eine Zahl eingeben ->") 
user_input_2 = input("Bitte noch eine Zahl eingeben ->") 
#welcher datentyp ist user_input?
print("user_input ist vom datentyp: {}".format(type(user_input)))



#nun eine einfache Ausgabe mit print()
print("Deine Eingabe war: {}".format(user_input)) 

#stings addierien
#erg = user_input + user_input_2
#print("Erg = {}".format(erg))

#stings in float umwandeln
user_input = float(user_input) 
user_input_2 = float(user_input_2)
erg = user_input + user_input_2
print("Erg = {:.3f}".format(erg))
