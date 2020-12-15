from random import randint
import pygame
from time import sleep
from settings import *
# from gameScreen import tilesHeight,tilesWide,width,height


class snakeEnemy:
    def __init__(self, x, y, length):
        # global tilesWide,tilesHeight,width,height
        self.x = x
        self.y = y
        self.length = length
        self.body = self.createBody([1, 0])
        self.changeMap = []
        self.grid = []
        self.dead = False

    def createBody(self, currentVector: list):
        body = []
        for i in range(0, self.length):
            body.append({'x': self.x, 'y': self.y-i,
                         'vX': currentVector[0], 'vY': currentVector[1]})

        return body

    # def move(self, grid):
    #     for i, piece in enumerate(self.body):
    #         piece['x'] += piece['vX']
    #         piece['y'] += piece['vY']
    #         for g in grid:
    #             if piece['x'] == g[0] and piece['y'] == g[1]:
    #                 print('selcted')
    #                 self.changeMap.append(
    #                     [piece['x'], piece['y'], piece['vX']*-1, -1])
    #                 piece['x'] -= piece['vX']
    #                 self.changeMap.append(
    #                     [piece['x'], piece['y']-1, piece['vX'], 0])
    #         for change in self.changeMap:

    #             if change[0] == piece['x'] and change[1] == piece['y']:
    #                 piece['vX'] = change[2]
    #                 piece['yX'] = change[3]
    def move(self):

        for i, b in enumerate(self.body):
            if b['y'] < 0:
                #print('I AM BELLOW ONE ', self.body[i]['y'])
                self.body[i]['y'] += 1
                #print('I AM ABOVE ONE ', self.body[i]['y'])

            else:
                self.body[i]['x'] += b['vX']
                for g in self.grid:
                    # print('GGGGGGG: ', g)
                    # print(b, g)
                    if i == 0:
                        if (g[0] == b['x']) and (g[1] == b['y']):

                            self.bounce(i)
                            break
                        elif b['x'] == 0 or b['x'] == tilesWide:

                            self.bounce(i)
                    else:
                        for c in self.changeMap:
                            if b['x'] == c[0] and b['y'] == c[1]:
                                # print(
                                #     'I AM NOT THE LEADER BUT I AM BOUNCING ', b, c)
                                self.bounce(i)
                if self.dead == True:
                    self

    def bounce(self, i):
        self.body[i]['vX'] *= -1
        self.body[i]['y'] += 1
        self.body[i]['x'] += self.body[i]['vX']
        self.changeMap.append(
            [self.body[i]['x']-self.body[i]['vX'], self.body[i]['y']-1])

    def show(self, win):
        for piece in self.body:
            # pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
            #     100, 100, 100, 100))
            print('MESSED UP BODY ', piece)
            pygame.draw.rect(win, (255, 0, 0), pygame.Rect(
                piece['x']*(width/tilesWide), piece['y']*(height/tilesHeight), width/tilesWide, height/tilesHeight))
            # print('PIECE ', piece['x'], piece['y'])
        return win
