
a = input("Gib die erste Zahl ein: ")
b = input("Gib die zweite Zahl ein: ")
c = input("Gib die Rechenoperation ein: ")

if c == "+":
    print(int(a) + int(b))
elif c == "-":
    print(int(a) - int(b))
elif c == "*":
    print(int(a) * int(b))
elif c == "/":
    print(int(a) / int(b))
else:
    print("Falsche Eingabe")

