#coding:utf-8

from readchar import readkey, key
import pygame

# Params
winRect = pygame.Rect(0, 0, 300, 300)
destOfCmd = (0, 0)
cmdSize = 60
fps = 60

# Colors
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
White = (255, 255, 255)
Black = (0, 0, 0)


def readCmdFunc():
    k = readkey()

def main():
    pygame.init()

    screen = pygame.display.set_mode(winRect.size)
    pygame.display.set_caption("Command mode test")
    screen.fill(Black)
    clock = pygame.time.Clock()

    command = 'name'

    running = True
    while running:
        k = readkey()
        while True:
            #
            clock.tick(fps)

            #
            screen.fill(Black)

            #

            if k == key.ESC:
                running = False
                break
            if k == key.BACKSPACE:
                command = command[:-1]
            if k == key.DOWN:
                command += k

            # Display the command string
            cmdTxt = pygame.font.SysFont(None, cmdSize).render(command, True, Red)
            screen.blit(cmdTxt, destOfCmd)

            # update display
            pygame.display.update()
            break


if __name__ == '__main__':
    main()
