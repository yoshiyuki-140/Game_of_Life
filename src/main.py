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
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW.size)
    pygame.display.set_caption('The game of life')

    # by gameModeHandler
    displayStartScreen()

    screen.fill(Black)
    cell = Cell()

    #
    clock = pygame.time.Clock()

    # text box for the commands of LifeGame
    text_box = TextInput(pygame.font.SysFont("msmincho", 40), Black)
    running = True
    while running:
        #
        clock.tick(FPS)
        events = pygame.event.get()

        #
        screen.fill(Black)

        #
        for event in events:
            if event.type == QUIT:
                running = False

            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            #
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_rect = pygame.Rect(event.pos[0], event.pos[1], 1, 1)
                #
                for y in range(WORLD_SIZE[1]):
                    for x in range(WORLD_SIZE[0]):
                        #
                        if cell.rects[y][x].contains(mouse_rect):
                            cell.game_of_life.toggle_object(x+1, y+1)
            # inputed command judge
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
                    if cmds[0] == 'spaceship':
                        cell.game_of_life.createSpaceShip()
                    if cmds[0] == 'bar':
                        cell.game_of_life.createBar()
                    if cmds[0] == 'random':
                        cell.game_of_life.setRandom()
                    if cmds[0] == 'clear':
                        cell.game_of_life.resetWorld()
                #
                if len(cmds) > 1:
                    if len(cmds) == 2:
                        # このスキップコマンドはスキップする回数をあげすぎると処理落ちします
                        if cmds[0] == 'skip':
                            for _ in range(int(cmds[1])):
                                cell.game_of_life.update()
                                cell.update()

                    if len(cmds) >= 3 and cmds[0] == 'spaceShip':
                        cell.game_of_life.createSpaceShip(
                            int(cmds[1]), int(cmds[2]))

        #
        if game_status:
            cell.game_of_life.update()
            cell.update()
        else:
            cell.update()
            pause()

        # I don't know dirty rect update method
        text_box.update(events)
        rectOfTextBox = text_box.get_surface().get_rect()
        rectOfTextBox.topleft = 10, 550
        screen.fill(Green, rectOfTextBox)
        screen.blit(text_box.get_surface(), rectOfTextBox.topleft)

        pygame.display.update()

    quit()
