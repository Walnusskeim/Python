#Geisterspiel

from random import randint

print("Geisterspiel")

du_bist_mutig = True
score = 0

while du_bist_mutig:
    geistertuer = randint(1, 3)
    print("Vor die sind drei Türen.")
    print("Hinter einer ist der Geist.")
    print("Welche Tür öffnest du?")

    tuer = int(input("1, 2 oder 3? "))

    if tuer == geistertuer:
        print("GEIST")
        du_bist_mutig = False
    else:
        print("Kein Geist! "
              "Du bist ein Zimmer weiter.")
        score = score + 1

print("Laufe weg!")
print("Du hast {} Punkte erreicht.".format(score))
print("Das Spiel ist beendet.")

