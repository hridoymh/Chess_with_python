import pygame

class Rect:
    def __init__(self,w,h,x,y,color):
        self.color = color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))