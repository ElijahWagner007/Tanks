import pygame as pg
from pygame.locals import *
import math as m

from ufo import Ufo
from game import SCREEN_WIDTH , SCREEN_HEIGHT

# Initialize pygame
pg.init()

# Create Window, set window caption, start clock
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ufos?!")
clock = pg.time.Clock()
speed_limit = pg.Vector2(1.5,1.5)

# Colors
bg = (247, 210, 166)
bullet_color = (128,140,140)

# Game Vars.
p1_magazine = []

p1_ufo = Ufo(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, screen, "PLAYER")
enemy_ufo = Ufo(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4, screen, "ENEMY")
ctr = 59

# Game Loop
running = True
while running:
    # set clock / delta time in seconds since last frame
    # i.e. framerate independant physics
    dt = clock.tick(60) / 1000
    ctr += 1       
    
    screen.fill(bg)
    # QUIT Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    p1_ufo.draw_player(dt)
    enemy_ufo.draw_cpu(dt, ctr)
    
    # Updates display
    pg.display.flip() 
    
# De-initializes pygame
pg.quit() 
