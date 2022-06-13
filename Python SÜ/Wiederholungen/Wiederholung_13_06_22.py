import random

while True:
    #user greetings and ask for upper number limit
    ui = (int(input("Wie viele Zahlen möchtest du generieren? ")))
    try:
        ui = int(ui)
        break
    except ValueError:
        print("Bitte eine Zahl eingeben!")
        continue

zahlen = []
for i in range(ui):
    zahlen.append(random.randint(0,10000000000000))
print(zahlen)