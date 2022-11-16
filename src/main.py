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
text_box = TextInput(pygame.font.SysFont("msmincho", 30), Red)
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
            cmd = event.Text
            if cmd == 'start':
                game_status = True
            if cmd == 'pause' or cmd == 'stop':
                game_status = False
            if cmd == 'quit' or cmd == 'exit':
                pygame.quit()
                sys.exit()
            if cmd == 'glider':
                cell.game_of_life.glider_init()
            if cmd == 'spaceShip':
                cell.game_of_life.createSpaceShip()
            if cmd == 'clear':
                cell.game_of_life.world_init_death()
            if cmd == 'random':
                cell.game_of_life.randomize_world()
            if cmd == 'bar':
                cell.game_of_life.create_bar()
            # arg cmds
            if len(cmd.split(" ")) > 1:
                args = [word.strip('\n') for word in cmd.split(" ")]
                if len(args) >= 3 and args[0] == 'spaceShip':
                    cell.game_of_life.createSpaceShip(int(args[1]),int(args[2]))



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
