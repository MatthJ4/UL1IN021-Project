import pygame
import os
pygame.init()
screen_info = pygame.display.Info()
s_width = screen_info.current_w
s_height = screen_info.current_h
scalex = s_width / 1920
scaley = s_height / 1080
screen = pygame.display.set_mode((s_width, s_height))
grey = (200, 200, 200)