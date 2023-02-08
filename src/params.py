#coding:utf-8

import pygame

# Parameters
WINDOW = pygame.Rect(0, 0, 1000, 600)
WORLD_SIZE = '100x60'
WORLD_SIZE = [int(f) for f in WORLD_SIZE.split('x')]
LINE_WIDTH = 1
FPS = 60
game_status = True


# Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
