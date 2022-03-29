from classconnect4 import *

if __name__ == '__main__':
    
    Game = Connect4()

    while True:
    
        Game.affiche()
        if Game.tour:
            print('Au tour des jaunes')
        else:
            print('Au tour des rouges')
        actionchar = input('Action [0-6 = jouer, s = stop] : ')

        if actionchar in ['0', '1', '2', '3', '4', '5', '6']:
            Game.jouer(int(actionchar))
        elif actionchar == 's':
            break
        else:
            print('Action inconnue')
