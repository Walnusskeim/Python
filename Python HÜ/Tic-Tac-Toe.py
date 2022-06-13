'''
Tic-Tac-Toe
Maximilian
June 2022
'''

y_dim = 3
x_dim = 3

def display (playingfield):
    for x in range (x_dim):
        print(" {}".format(x), end=" ")
    print()

    for y in range(y_dim):
        for x in range(x_dim):
            print("|{}".format(playingfield[x][y]),end ='')
        print("| {}".format(y))

def check_for_win ():
    for row in range(0,3,1):
        if(plaing_field[0][row]== playing_field[1][row] == playing_field[2][row] != " "):
            return 1
        elif (playing_field[row][0] == playing_field[row][1] == playing_field[row][2] != " "):
            return 1
    if(playing_field[0][0] == playing_field[1][1] == playing_field[2][2] != " "):
            return 1
    elif(playing_field[2][0] == playing_field[1][1] == playing_field[0][2] != " "):
            return 1
    return 0

### Main program starts here ###
playing_field = [[" " for i in range(y_dim)] for j in range (x_dim)]

display(playing_field)

#some variables:
counter = 0
player = 1
symbol = 'X'

#game loop starts here:
while True:
    x_cord = int(input("PLayer {} enter x-coordinate ->".format(player)))
    y_cord = int(input("PLayer {} enter y-coordinate ->".format(player)))
    if (x_cord >= x_dim or y_cord >= y_dim or x_cord < 0 or y_cord < 0):
        print("You coordinate is out of range! Try again!")
        continue
    else:
        if (playing_field[x_cord][y_cord] == ' '):
            # field is free
            playing_field[x_cord][y_cord] = symbol
        else:
            print("This field is already taken!")
            continue

    #update counter:
    counter = counter + 1

    #check for draw
    if (counter == 9):
        print("The game is a DRAW!")
        break

    #check for win
    if (check_for_win()):
        print("GG Player {} you won !!!".format(player))
        break