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
text_box = TextInput(pygame.font.SysFont("msmincho", 40), Black)
while True:
    #
    clock.tick(fps)
    pygame.time.wait(100)
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
            cmds = event.Text.rstrip('\n').split(" ")
            if len(cmds) == 1:
                if cmds[0] == 'start':
                    game_status = True
                if cmds[0] == 'pause' or cmds[0] == 'stop':
                    game_status = False
                if cmds[0] == 'quit' or cmds[0] == 'exit':
                    pygame.quit()
                    sys.exit()
                if cmds[0] == 'glider':
                    cell.game_of_life.createGlier()
                if cmds[0] == 'spaceShip':
                    cell.game_of_life.createSpaceShip()
                if cmds[0] == 'bar':
                    cell.game_of_life.createBar()
                if cmds[0] == 'random':
                    cell.game_of_life.setRandom()
                if cmds[0] == 'clear':
                    cell.game_of_life.resetWorld()
            # arg cmds[0]s
            if len(cmds) > 1:
                if len(cmds) >= 3 and cmds[0] == 'spaceShip':
                    cell.game_of_life.createSpaceShip(
                        int(cmds[1]), int(cmds[2]))

    #
    if game_status:
        cell.game_of_life.main_algorithm()
        cell.update()
    else:
        cell.update()
        pause()

    # ここの書き方下手だよね
    # textboxの背景をつけるのとそのblit
    text_box.update(events)
    rectOfTextBox =  text_box.get_surface().get_rect()
    rectOfTextBox.topleft = 10,550
    screen.fill(Green,rectOfTextBox)
    screen.blit(text_box.get_surface(),rectOfTextBox.topleft)

    pygame.display.update()
