# Simple Animation with PyGame, Linda Cooper, 12/09/21, 2:14PM, v0.1

import pygame, sys, time
from pygame.locals import *

#Setup.PygAme
pygame.init()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_captions('Animation Example!')
