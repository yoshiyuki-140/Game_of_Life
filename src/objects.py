#coding:utf-8
# Objects

import pygame
from copy import deepcopy
from random import choice
from params import *


class Cell(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(0,0,int(WINDOW.width/WORLD_SIZE[0]), 
                                int(WINDOW.height/WORLD_SIZE[1]))
        self.rects = [[pygame.Rect(x*(self.rect.width+LINE_WIDTH),
                        y*(self.rect.height+LINE_WIDTH),
                        int((WINDOW.width - LINE_WIDTH * (WORLD_SIZE[0]-1))/WORLD_SIZE[0]),
                        int((WINDOW.height - LINE_WIDTH*(WORLD_SIZE[1]-1)) / WORLD_SIZE[1]))
                        for x in range(WORLD_SIZE[0])]
                        for y in range(WORLD_SIZE[1])]

        self.game_of_life = GameOfLife(WORLD_SIZE=WORLD_SIZE)

    def update(self):
        for y in range(WORLD_SIZE[1]):
            for x in range(WORLD_SIZE[0]):
                if self.game_of_life.world[y][x] == True:
                    pygame.draw.rect(self.screen, Black, self.rects[y][x])
                else:
                    pygame.draw.rect(self.screen, White, self.rects[y][x])


class GameOfLife:
    """lifeGame's rule"""

    def __init__(self, WORLD_SIZE: tuple):
        #世界の大きさdefoultで10
        self.WORLD_SIZE = WORLD_SIZE

        self.true_or_false = [True, False]

        self.resetWorld()

        self.tmp_world = deepcopy(self.world)
        self.previous_world = deepcopy(self.world)

        self.count = 0

    def update(self):
        self.previous_world = deepcopy(self.world)
        self.change_world()

    def createBar(self):
        for i in range(10):
            self.world[15][i+20] = True

    def createGlier(self):

        self.world[1][1] = True
        self.world[1][2] = False
        self.world[1][3] = True
        self.world[2][1] = False
        self.world[2][2] = True
        self.world[2][3] = True
        self.world[3][1] = False
        self.world[3][2] = True
        self.world[3][3] = False

    def resetWorld(self):
        self.world = [[False for x in range(
            self.WORLD_SIZE[0])] for y in range(self.WORLD_SIZE[1])]

    def setRandom(self):
        self.world = [[choice(self.true_or_false) for i in range(
            self.WORLD_SIZE[0])] for j in range(self.WORLD_SIZE[1])]

    def change_world(self):
        """
        世代交代
        """
        for i in range(self.WORLD_SIZE[1]):
            for j in range(self.WORLD_SIZE[0]):
                self.tmp_world[i][j] = self.liveOrdie(j, i)
        self.world = deepcopy(self.tmp_world)

    def toggle_object(self, x, y):
        """
        Args:
            x (int): coordinate of x axis
            y (int): coordinate of y axis
        """
        self.world[y-1][x-1] = not self.world[y-1][x-1]

    def liveOrdie(self, x, y):

        self.countLivingCell(x, y)
        # 最後のジャッジ変更した
        if self.world[y][x]:
            if self.count == 2 or self.count == 3:
                return True
            return False
        else:
            if self.count == 3:
                return True
            return False
    def createSpaceShip(self,x=0,y=0):
        # 1行目
        for yi in range(4):
            for xi in range(6):
                # at 1 row
                if yi==0 and xi == 4:
                    self.world[y+yi][x+xi] = True
                    continue
                # at 2 row
                if yi == 1 and xi == 5:
                    self.world[y+yi][x+xi] = True
                    continue
                # at 3 row
                if yi == 2 and (xi == 5 or xi == 0):
                    self.world[y+yi][x+xi] = True
                    continue
                # at 4 row
                if yi == 3 and (xi != 0):
                    self.world[y+yi][x+xi] = True
                    continue
                self.world[y+yi][x+xi] = False
                    
    def countLivingCell(self, x, y):
        """周辺の状態をカウントする
        """
        self.count = 0
        if self.world[(y-1) % self.WORLD_SIZE[1]][(x-1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.WORLD_SIZE[1]][(x) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.WORLD_SIZE[1]][(x+1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y) % self.WORLD_SIZE[1]][(x-1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y) % self.WORLD_SIZE[1]][(x+1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.WORLD_SIZE[1]][(x-1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.WORLD_SIZE[1]][(x) % self.WORLD_SIZE[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.WORLD_SIZE[1]][(x+1) % self.WORLD_SIZE[0]] == True:
            self.count += 1
