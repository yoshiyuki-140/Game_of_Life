#coding:utf-8
# game mode

import pygame
from pygame.locals import *
import sys
from params import *

def start():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 100)
    Start_msg = font.render("START", True, Red)
    screen.blit(Start_msg, (Window.centerx - Start_msg.get_width() //
                2, Window.centery - Start_msg.get_height()//2))

def showStartScreen():
    running = True
    while running:
        start()
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                running = False
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

        pygame.display.flip()
    #

def pause():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 100)
    Pause_msg = font.render("PAUSE", True, Blue)
    screen.blit(Pause_msg, (Window.centerx - Pause_msg.get_width() //
                2, Window.centery - Pause_msg.get_height()//2))
