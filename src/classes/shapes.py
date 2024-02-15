import pygame

class Rect:
    def __init__(self,w,h,x,y,t,color):
        self.color = color
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.type = t
        self.isactive = False
        self.activecolor = (color[0],color[1],color[2]-100)
    def draw(self, surface):
        if self.isactive:
            pygame.draw.rect(surface, self.activecolor, pygame.Rect(self.x, self.y, self.w, self.h))
            return
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.w, self.h))
    def activate(self):
        self.isactive = True
    def deactivate(self):
        self.isactive = False