import numpy as np

class Connect4:
    def __init__(self, grid = np.full((6,7),None), tour = True):
        self.grid = grid # np array 6x7
        self.tour = tour # True = Jaune ; False = Red
        self.chars = {
            True : 'O',
            False : 'X',
            None : ' '
        }
    
    def jouer(self, col): 
        if self.grid[0,col] == None:
            # coup jouable
            ind = np.max(np.argwhere(self.grid[:,col] == None))
            self.grid[ind,col] = self.tour
            self.tour = not(self.tour)
        else:
            print('Coup impossible.')

    def affiche(self):
        output = ''
        for i in range(6): # i indice des lignes
            output += '|'
            for j in range(7): # j indice des colonnes
                output += self.chars[self.grid[i,j]]
            output += '|\n'
        output += '---------'
        print(output)
