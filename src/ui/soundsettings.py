import pygame
from src import settings

class SoundSettings:
    """Sound setting buttons
    Args:
        x: x position
        y: y position
        game: the current SceneManager"""
    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.slider_width = 400 * settings.scalex
        self.slider_height = 40 * settings.scaley
        
        self.font = pygame.font.SysFont("Colibri", 24)

        self.music_slider = pygame.Rect(x, y, self.slider_width, self.slider_height)
        self.sfx_slider = pygame.Rect(x, y + 100 * settings.scaley, self.slider_width, self.slider_height)
        self.toggle_rect = pygame.Rect(x, y + 200 * settings.scaley, 70 * settings.scalex, 30 * settings.scaley)

        self.drag_music = False
        self.drag_sfx = False

        pygame.mixer.music.set_volume(self.game.audio["music_volume"])

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.music_slider.collidepoint(event.pos):
                self.drag_music = True
            elif self.sfx_slider.collidepoint(event.pos):
                self.drag_sfx = True
            elif self.toggle_rect.collidepoint(event.pos):
                self.toggle_music()

        elif event.type == pygame.MOUSEBUTTONUP:
            self.drag_music = False
            self.drag_sfx = False

        elif event.type == pygame.MOUSEMOTION:
            if self.drag_music:
                self.game.audio["music_volume"] = self.calculate_volume(event.pos[0], self.music_slider)
                pygame.mixer.music.set_volume(self.game.audio["music_volume"])

            if self.drag_sfx:
                self.game.audio["sfx_volume"] = self.calculate_volume(event.pos[0], self.sfx_slider)
    
    def calculate_volume(self, mouse_x, slider):
        volume = (mouse_x - slider.x) / slider.width
        return max(0.0, min(1.0, volume))

    def toggle_music(self):
        self.game.audio["music_enabled"] = not self.game.audio["music_enabled"]
        if self.game.audio["music_enabled"]:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def apply_sfx_volume(self, sound):
        sound.set_volume(self.game.audio["sfx_volume"])
    
    def draw_slider(self, screen, slider, volume):
        pygame.draw.rect(screen, (80, 80, 80), slider)
        filled = pygame.Rect(slider.x, slider.y, slider.width * volume, slider.height)
        pygame.draw.rect(screen, (0, 200, 0), filled)
        pygame.draw.rect(screen, (255, 255, 255), slider, 2)

    def draw(self, screen):
        settings.screen.blit(self.font.render("Music Volume", True, (255, 255, 255)),
                    (self.x, self.y - 38 * settings.scaley))
        settings.screen.blit(self.font.render("SFX Volume", True, (255, 255, 255)),
                    (self.x, self.y + 58 * settings.scaley))
        settings.screen.blit(self.font.render("Music", True, (255, 255, 255)),
                    (self.x, self.y + 168 * settings.scaley))

        self.draw_slider(screen, self.music_slider, self.game.audio["music_volume"])
        self.draw_slider(screen, self.sfx_slider, self.game.audio["sfx_volume"])

        color = (0, 180, 0) if self.game.audio["music_enabled"] else (180, 0, 0)
        pygame.draw.rect(screen, color, self.toggle_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.toggle_rect, 2)

        label = "ON" if self.game.audio["music_enabled"] else "OFF"
        text = self.font.render(label, True, (255, 255, 255))
        settings.screen.blit(text, text.get_rect(center=self.toggle_rect.center))                    
                 
