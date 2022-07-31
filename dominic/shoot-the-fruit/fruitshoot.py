from pgzero.builtins import Actor, animate, keyboard
import pygame
from pygame import display as screen
pygame.init()
myscreen = screen.set_mode((800,600))
apple = Actor("apple")


def draw():
    #screen.clear()
    apple.draw()





    
draw()
