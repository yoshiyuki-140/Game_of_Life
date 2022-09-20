#coding:utf-8


from copy import deepcopy
from random import choice
from time import sleep
import sys
from pygame.locals import *
import pygame

# Parameters
Window = pygame.Rect(0, 0, 1000, 600)
world_size = '100x102'
world_size = [int(f) for f in world_size.split('x')]  # <- return list object
line_width = 1
fps = 60
game_status = True  # when this status is True, cells is updated


# Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

# Objects


class Cell(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.rect = pygame.Rect(
            #         v ここエラー出るかも               v ここエラー出るかも
            0, 0, int(Window.width/world_size[0]), int(Window.height/world_size[1]))
        self.rects = [[pygame.Rect(x*self.rect.width+line_width,
                                   y*self.rect.height+line_width,
                                   int((Window.width - line_width *
                                       (world_size[0]-1))/world_size[0]),
                                   int((Window.height - line_width*(world_size[1]-1)) / world_size[1]))
                       for x in range(world_size[0])]
                      for y in range(world_size[1])]
        self.game_of_life = GameOfLife()
        self.game_of_life.glider_init()

    def update(self):
        self.game_of_life.main_algorithm()
        for y in range(world_size[1]):
            for x in range(world_size[0]):
                if self.game_of_life.world[y][x] == True:
                    pygame.draw.rect(self.screen, Black, self.rects[y][x])
                else:
                    pygame.draw.rect(self.screen, White, self.rects[y][x])


class GameOfLife:
    def __init__(self):
        #世界の大きさdefoultで10
        self.world_size = world_size

        self.true_or_false = [True, False]

        #世界の状態をすべて死で初期化
        self.world = [[False for x in range(
            self.world_size[0])] for y in range(self.world_size[1])]

        self.tmp_world = deepcopy(self.world)

        self.count = 0

    def main_algorithm(self):
        self.previous_world = deepcopy(self.world)
        self.change_world()

    def glider_init(self):
        """conway's game of life における グライダーを作成する
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

    def random_init(self):
        """世界の状態をカオスに初期化する
        """
        self.world = [[choice(self.true_or_false) for i in range(
            self.world_size[0])] for j in range(self.world_size[1])]

    def change_world(self):
        """世代交代
        """
        for i in range(self.world_size[1]):
            for j in range(self.world_size[0]):

                self.tmp_world[i][j] = self.life_or_death(j, i)
        self.world = deepcopy(self.tmp_world)

    def toggle_object(self, i, j):
        """ (i,j) は ガウス平面の (x,y)座標 として扱え

        Args:
            i (int): 座標データなので1以上
            j (int): 座標データなので1以上
        """
        self.world[i-1][j-1] = not self.world[i-1][j-1]

    def life_or_death(self, x, y):
        """次の時代lifeならTrueを返すdeathならFalseをかえす
        """

        self.neighbor_count(x, y)
        # 最後のジャッジ変更した
        if self.world[y][x]:
            if self.count == 2 or self.count == 3:
                return True
            else:
                return False
        else:
            if self.count == 3:
                return True

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

<<<<<<< HEAD
# game mode
=======
# game modes


>>>>>>> create_line
def pause():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 80)
    Pause_msg = font.render("PAUSE", True, Blue)
    screen.blit(Pause_msg, (Window.centerx - Pause_msg.get_width() //
                2, Window.centery - Pause_msg.get_height()//2))


# main stream
pygame.init()
screen = pygame.display.set_mode(Window.size)
pygame.display.set_caption('The game of life')

#
bg = Black

#
cell = Cell()


#
clock = pygame.time.Clock()

#
while True:
    #
    clock.tick(fps)

    #
    screen.fill(bg)

    #
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            game_status = not game_status


    #
    if game_status:
        cell.update()
    else:
        pause()

    #
    pygame.display.flip()
