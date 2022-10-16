#coding:utf-8

import pygame


class CommandUtil:
    def __init__(self) -> None:
        self.screen = pygame.display.get_surface()
        self.window = self.screen.get_rect()
        self.textSize = 50

    def startCommandMode(self):
        self.commandInput()

    def commandInput(self):
        self.inStr = input(":")
        self.commandStr = pygame.font.SysFont(
            None, self.textSize).render(self.string, True, (0, 0, 0))
        self.screen.blit(self.commandStr, (self.window.centerx - self.commandStr.get_width() //
                                           2, self.window.bottom - self.commandStr.get_height() - 10))
        