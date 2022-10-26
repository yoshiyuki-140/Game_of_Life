#coding:utf-8
# Author : Yoshiyuki Kurose


import pygame
import sys
from pygame.locals import *

# my modules
from params import *
from objects import *
from gameModeHandler import *
from commandmode import CommandUtil

# main stream
pygame.init()
screen = pygame.display.set_mode(Window.size)
pygame.display.set_caption('The game of life')

# by gameModeHandler
showStartScreen()

screen.fill(Black)
cell = Cell()

#
clock = pygame.time.Clock()

#
while True:
    #
    clock.tick(fps)
    pygame.time.wait(100)

    #
    screen.fill(Black)

    #
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            game_status = not game_status

        #
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
            #
            for y in range(world_size[1]):
                for x in range(world_size[0]):
                    #
                    if cell.rects[y][x].contains(mouse_rect):
                        cell.game_of_life.toggle_object(x+1, y+1)
        # AddRandmizeKey
        if event.type == KEYDOWN and event.key == K_r and not game_status:
            cell.game_of_life.randomize_world()

        # AddGriderGenerateKey
        if event.type == KEYDOWN and event.key == K_g and not game_status:
            cell.game_of_life.glider_init()

        # AddClearAllKey
        if event.type == KEYDOWN and event.key == K_c and not game_status:
            cell.game_of_life.world_init_death()

        # AddCommandKey
        if event.type == KEYDOWN and event.key == K_COLON and not game_status:
            cmdIns = CommandUtil
            cmdStr = cmdIns.returnStrForCommand(commands)

    #
    if game_status:
        cell.game_of_life.main_algorithm()
        cell.update()
    else:
        cell.update()
        pause()

    #
    pygame.display.update()
