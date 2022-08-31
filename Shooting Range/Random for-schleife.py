
zahl = 7
spring_counter = 0

for i in range (1,30):
    print("Was ist", i, "x", zahl, "?")
    antwort = input()
    if antwort == "stopp":
        break
    if antwort == "spring":
        spring_counter = spring_counter + 1
        print("Sprung! Aber Achtung! \nDu darfst nur noch {} mal springen!".format(spring_counter + 1))
        continue
    if spring_counter == 4:
        print("Du darfst nicht mehr springen!")
        continue
    richtig = i * zahl
    if int(antwort) == richtig:
        print("Richtig!")
    else:
        print("Falsch!")
        print("Die richtige Antwort ist", richtig)
print("Fertig")

