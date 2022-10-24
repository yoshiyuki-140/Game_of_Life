#coding:utf-8

import pygame
from readchar import readkey, key


class CommandUtil:
    def __init__(self) -> None:
        self.screen = pygame.display.get_surface()
        self.window = self.screen.get_rect()
        self.command = str(':')

    def returnCommandMode(self, commands:list):
        while True:
            k = readkey()
            self.command += k
            self.blitCommand()
            if k == key.ENTER:
                if self.command in commands:
                    return self.command

            if k == key.BACKSPACE:
                self.command = self.command[:-2]  # commandの最後の文字を削除
                self.blitCommand()
    def blitCommand(self):
        font = pygame.font.SysFont(None,50)
        cmdMsg = font.render(self.command,True,(0,0,0))
        self.screen.blit(cmdMsg,0,self.window.bottom - cmdMsg.get_rect().height - 10)
        pygame.display.update()
