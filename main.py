import pygame as pg
from pygame.locals import *
import math as m
import random as r

from ufo import Ufo
from game import SCREEN_WIDTH , SCREEN_HEIGHT , draw_text

# Initialize pygame
pg.init()

# Create Window, set window caption, start clock
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ufos?!")
clock = pg.time.Clock()
speed_limit = pg.Vector2(1.5,1.5)
font = pg.font.SysFont('Arial', 30)

# Colors
bg = (247, 210, 166)
bullet_color = (128,140,140)

# Game Vars.
p1_magazine = []
enemy_x_start = r.randint(0,SCREEN_WIDTH)
enemy_y_start = r.randint(0,SCREEN_HEIGHT) 

p1_ufo = Ufo(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, screen, "PLAYER")
enemy_ufo = Ufo(enemy_x_start, enemy_y_start, screen, "ENEMY")
ctr = 59

# Game Loop
player_alive = True
running = True

def run_game(ctr, player_alive, running):
    # set clock / delta time in seconds since last frame
    # i.e. framerate independant physics
    dt = clock.tick(60) / 1000
    ctr += 1       
    
    screen.fill(bg)
    # QUIT Event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    p1_ufo.draw_player(dt, True)
    enemy_ufo.draw_cpu(dt, ctr, True)
    if p1_ufo.collision_detection(enemy_ufo):
        player_alive = False

    return ctr, player_alive , running

def game_over_menu():
    pass

while running:
    if player_alive:
        ctr, player_alive, running = run_game(ctr, player_alive, running)
    else:
        #game_over_menu()
        dt = clock.tick(60) / 1000
        
        screen.fill(bg)
        # QUIT Event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            player_alive = True
            ctr = 59
            enemy_ufo.ufo_pos.x = r.randint(0,SCREEN_WIDTH)
            enemy_ufo.ufo_pos.y = r.randint(0,SCREEN_HEIGHT) 
            p1_ufo.ufo_pos.x = SCREEN_WIDTH // 2
            p1_ufo.ufo_pos.y = SCREEN_HEIGHT // 2
            p1_ufo.ufo_vel.x = 0
            p1_ufo.ufo_vel.y = 0
            p1_ufo.ufo_accel.x = 0
            p1_ufo.ufo_accel.y = 0

        p1_ufo.draw_player(dt, False)
        enemy_ufo.draw_cpu(dt, ctr, False)
        
        draw_text(screen,"GAME OVER", font, "black", SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 10)
        draw_text(screen,"Press [Enter] to play again", font, "black", SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 20)

    # Updates display
    pg.display.flip() 
    
# De-initializes pygame
pg.quit() 
