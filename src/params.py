#coding:utf-8

import pygame

# Parameters
Window = pygame.Rect(0, 0, 1000, 600)
world_size = '200x120'
world_size = [int(f) for f in world_size.split('x')]  # <- return list object
line_width = 1
fps = 60
game_status = True  # when this status is True, any ells will be updated


# Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)
