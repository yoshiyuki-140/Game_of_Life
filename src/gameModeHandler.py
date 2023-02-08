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
    screen.blit(Start_msg, (WINDOW.centerx - Start_msg.get_width() //
                2, WINDOW.centery - Start_msg.get_height()//2))

def displayStartScreen():
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

def pause():
    screen = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 100)
    Pause_msg = font.render("PAUSE", True, Blue)
    screen.blit(Pause_msg, (WINDOW.centerx - Pause_msg.get_width() //
                2, WINDOW.centery - Pause_msg.get_height()//2))
    