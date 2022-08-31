from random import randint

name = ['Max', 'Peter', 'Paul', 'Monika', 'Anna']
verb = ['kauft', 'isst', 'trint', 'schläft', 'sieht']
ende = ['Meer', 'Ball', 'Apfel', 'Haus' , 'Welt']

def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked

while True:
    print(pick(name) + " " + pick(verb) + " " "im" " " + pick(ende), end = '.\n')
    input()
