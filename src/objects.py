#coding:utf-8
# Objects

import pygame
from copy import deepcopy
from random import choice
from params import *


# cell の オブジェクト update メソッドで screenにblitする。
# 画面に対する描写自体は、main streamで行う(pygame.display.update()メソッドを使用)。
class Cell(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(
            0, 0, int(Window.width/world_size[0]), int(Window.height/world_size[1]))
        self.rects = [[pygame.Rect(x*(self.rect.width+line_width),
                                   y*(self.rect.height+line_width),
                                   int((Window.width - line_width *
                                       (world_size[0]-1))/world_size[0]),
                                   int((Window.height - line_width*(world_size[1]-1)) / world_size[1]))
                       for x in range(world_size[0])]
                      for y in range(world_size[1])]
        self.game_of_life = GameOfLife(world_size=world_size)
        self.game_of_life.createGlier()

    def update(self):
        for y in range(world_size[1]):
            for x in range(world_size[0]):
                if self.game_of_life.world[y][x] == True:
                    pygame.draw.rect(self.screen, Black, self.rects[y][x])
                else:
                    pygame.draw.rect(self.screen, White, self.rects[y][x])


# Game rules
class GameOfLife:
    """
    このライフゲームの要となる法則を定義している。
    """

    def __init__(self, world_size: tuple):
        #世界の大きさdefoultで10
        self.world_size = world_size

        self.true_or_false = [True, False]

        #世界の状態をすべて死で初期化
        # ここでself.worldクラス変数が定義される
        self.resetWorld()

        self.tmp_world = deepcopy(self.world)
        self.previous_world = deepcopy(self.world)

        self.count = 0

    def main_algorithm(self):
        self.previous_world = deepcopy(self.world)
        self.change_world()
    # 入れるならここに入れる
    # if you enter to life game objects, you should input to here

    def createBar(self):
        for i in range(10):
            self.world[15][i+20] = True

    def createGlier(self):
        """
        conway's game of life における グライダーを作成する
        """

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
        """world init command
        """
        self.world = [[False for x in range(
            self.world_size[0])] for y in range(self.world_size[1])]

    def setRandom(self):
        """
        世界の状態をカオスに初期化する
        """
        self.world = [[choice(self.true_or_false) for i in range(
            self.world_size[0])] for j in range(self.world_size[1])]

    def change_world(self):
        """
        世代交代
        """
        for i in range(self.world_size[1]):
            for j in range(self.world_size[0]):
                self.tmp_world[i][j] = self.life_or_death(j, i)
        self.world = deepcopy(self.tmp_world)

    def toggle_object(self, x, y):
        """ ガウス平面の (x,y)座標 として扱え

        Args:
            x (int): 座標データなので1以上
            y (int): 座標データなので1以上
        """
        self.world[y-1][x-1] = not self.world[y-1][x-1]

    def life_or_death(self, x, y):
        """次の時代lifeならTrueを返すdeathならFalseをかえす
        """

        self.neighbor_count(x, y)
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
                    
    def neighbor_count(self, x, y):
        """周辺の状態をカウントする
        """
        self.count = 0
        if self.world[(y-1) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.world_size[1]][(x) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y-1) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x-1) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x) % self.world_size[0]] == True:
            self.count += 1
        if self.world[(y+1) % self.world_size[1]][(x+1) % self.world_size[0]] == True:
            self.count += 1
