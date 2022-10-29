#coding:utf-8
# Author : Yoshiyuki Kurose


import pygame
import sys
from pygame.locals import *

# my modules
from params import *
from objects import *
from gameModeHandler import *

# text handling module
from pygame_textinput.textinput import TextInput

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

# text box for the commands of LifeGame
text_box = TextInput(pygame.font.SysFont("yumincho", 30), Green)
#
while True:
    #
    # clock.tick(fps)
    # pygame.time.wait(100)
    events = pygame.event.get()

    #
    screen.fill(Black)

    #
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        # if event.type == KEYDOWN and event.key == K_SPACE:
        #     game_status = not game_status

        #
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
            #
            for y in range(world_size[1]):
                for x in range(world_size[0]):
                    #
                    if cell.rects[y][x].contains(mouse_rect):
                        cell.game_of_life.toggle_object(x+1, y+1)
        # 各種コマンドの処理
        if event.type == pygame.USEREVENT:

            if event.Text == 'start':
                game_status = True
            if event.Text == 'pause' or event.Text == 'stop':
                game_status = False
            if event.Text == 'quit':
                pygame.quit()
                sys.exit()
            if event.Text == 'grider':
                cell.game_of_life.glider_init()
            if event.Text == 'clear':
                cell.game_of_life.world_init_death()
            if event.Text == 'random':
                cell.game_of_life.randomize_world()


    #
    if game_status:
        cell.game_of_life.main_algorithm()
        cell.update()
    else:
        cell.update()
        pause()

    #
    text_box.update(events)
    screen.blit(text_box.get_surface(), (10, 550))
    pygame.display.update()
