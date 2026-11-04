import pygame
from src import settings

class Button:
    def __init__(self, text, x, y, action):
        self.font = pygame.font.SysFont("arial", int(40 * settings.scaley))
        self.text = text
        self.x = x
        self.y = y
        self.action = action
        
    def update(self, events):
        """Update Button"""
        mouse = pygame.mouse.get_pos()
        text_surface = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        if text_rect.collidepoint(mouse):  
            pygame.draw.rect(settings.screen, "blue", text_rect)
        else:
            pygame.draw.rect(settings.screen, "black", text_rect)
        settings.screen.blit(text_surface, text_rect)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and text_rect.collidepoint(mouse):
                self.action()
                print("pressed")