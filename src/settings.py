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
default_keybinds = {"left": pygame.K_q, "right": pygame.K_d, "up": pygame.K_z, "down": pygame.K_s, "jump": pygame.K_SPACE}
save_dir = "saves"
keybinds_file = os.path.join(save_dir, "keybinds.json")
save_file = os.path.join(save_dir, "save.json")
audio_file = os.path.join(save_dir, "audio.json")
default_audio = {"music_volume" : 1.0, "sfx_volume" : 1.0, "music_enabled" : True}