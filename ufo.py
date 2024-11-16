import pygame as pg
import random as r
from game import SCREEN_WIDTH , SCREEN_HEIGHT


class Ufo():
    """
        ufo class x and y are center of ufo
    """
    def __init__(self, x, y, screen, ufo_type) -> None:
        self.x = x
        self.y = y
        self.ufo = pg.transform.scale(pg.image.load("./assets/"+ ufo_type +".png").convert_alpha(), (60,60))
        self.rect = self.ufo.get_rect()
        self.speed = 5
        self.screen = screen

        # Kinematic Movement stuffs
        self.ufo_pos = pg.Vector2(x,y)
        self.ufo_vel = pg.Vector2(0,0) # Don't move at start
        self.ufo_accel = pg.Vector2(0,0) # Don't speed up at start

        self.ACCEL = 20 
    def screen_collision(self):
        half_width = (self.ufo.get_width() // 2)
        half_height = (self.ufo.get_height() // 2)

        # Check for collisions with walls
        if self.ufo_pos.x + half_width > SCREEN_WIDTH:
            self.ufo_pos.x = SCREEN_WIDTH - half_width
            self.ufo_vel.x *= -0.2
        if self.ufo_pos.x - half_width < 0:
            self.ufo_pos.x = half_width
            self.ufo_vel.x *= -0.2
        if self.ufo_pos.y + half_height > SCREEN_HEIGHT:
            self.ufo_pos.y = SCREEN_HEIGHT - half_height
            self.ufo_vel.y *= -0.2 
        if self.ufo_pos.y - half_height < 0:
            self.ufo_pos.y = half_height 
            self.ufo_vel.y *= -0.2 

    def cpu_screen_collision(self):
        half_width = (self.ufo.get_width() // 2)
        half_height = (self.ufo.get_height() // 2)

        # Check for collisions with walls
        if self.ufo_pos.x + half_width > SCREEN_WIDTH:
            self.ufo_pos.x = SCREEN_WIDTH - half_width
            self.ufo_vel.x *= -0.2
            self.ufo_accel *= -0.2
        if self.ufo_pos.x - half_width < 0:
            self.ufo_pos.x = half_width
            self.ufo_vel.x *= -0.2
            self.ufo_accel *= -0.2
        if self.ufo_pos.y + half_height > SCREEN_HEIGHT:
            self.ufo_pos.y = SCREEN_HEIGHT - half_height
            self.ufo_vel.y *= -0.2 
            self.ufo_accel *= -0.2
        if self.ufo_pos.y - half_height < 0:
            self.ufo_pos.y = half_height 
            self.ufo_vel.y *= -0.2 
            self.ufo_accel *= -0.2


    def update(self,dt):
        # set initial accel to 0,0
        self.ufo_accel = pg.Vector2(0,0)
        
        # Check for movement updates
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.ufo_accel.y = -self.ACCEL * dt
        if keys[pg.K_s]:
            self.ufo_accel.y = self.ACCEL * dt
        if keys[pg.K_d]:
            self.ufo_accel.x = self.ACCEL * dt
        if keys[pg.K_a]:
            self.ufo_accel.x = -self.ACCEL * dt
        
        self.ufo_vel += self.ufo_accel
        self.screen_collision()        
        self.ufo_pos += self.ufo_vel + 0.5 * self.ufo_accel

        self.rect.center = (self.ufo_pos.x, self.ufo_pos.y)

    def draw_player(self, dt):
        """
            Draws ufo onto window
        """
        self.update(dt)
        self.screen.blit(self.ufo,(self.ufo_pos.x - self.ufo.get_width() // 2, self.ufo_pos.y - self.ufo.get_width() // 2))
    
    def update_cpu(self,dt,ctr):
        if ctr % 60 == 0:
            # set initial accel to 0,0
            self.ufo_accel = pg.Vector2(0,0)
            
            # Check for movement updates
            rand_dir = r.randint(0,3)
            if rand_dir == 0:
                self.ufo_accel.y = -10 * self.ACCEL * dt 
            if rand_dir == 1:
                self.ufo_accel.y = 10 * self.ACCEL * dt
            if rand_dir == 2:
                self.ufo_accel.x = 10 * self.ACCEL * dt
            if rand_dir == 3:
                self.ufo_accel.x = -10 * self.ACCEL * dt
            
            self.ufo_vel += self.ufo_accel
            
        self.cpu_screen_collision()
        self.ufo_pos += self.ufo_vel + 0.5 * self.ufo_accel

        self.rect.center = (self.ufo_pos.x, self.ufo_pos.y)

    def draw_cpu(self, dt, ctr):
        """
            Draws ufo onto window. Distances not hardcoded, that's just the center of the ufo
        """
        self.update_cpu(dt, ctr)
        self.screen.blit(self.ufo,(self.ufo_pos.x - self.ufo.get_width() // 2, self.ufo_pos.y - self.ufo.get_width() // 2))

    def collision_detection(self, ufo_b):
        return self.rect.colliderect(ufo_b.rect)