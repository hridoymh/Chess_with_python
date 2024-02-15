import pygame


size = 80
pieces = {'b': 'black-bishop.png', 'k': 'black-king.png', 'n': 'black-knight.png', 'p': 'black-pawn.png', 'q': 'black-queen.png', 'r': 'black-rook.png', 'B': 'white-bishop.png', 'K': 'white-king.png', 'N': 'white-knight.png', 'P': 'white-pawn.png', 'Q': 'white-queen.png', 'R': 'white-rook.png'}


def arr2d(s):
    new = s.split('\n')
    for i in range(len(new)):
        new[i] = new[i].split(' ')
    
    return new


