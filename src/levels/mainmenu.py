import pygame
from src.ui.button import Button
from src import settings

class MainMenu:
    """Main menu
    Arg: game: current scene manager"""
    def __init__(self, game):
        self.game = game
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.font =  pygame.font.SysFont("Times New Roman", 14)
        self.buttons = [Button("Start Game", settings.s_width // 2, 400 * settings.scaley, lambda: game.button_action("difficulty")),
                        Button("Settings", settings.s_width // 2, 600 * settings.scaley, lambda: game.button_action("settings")),
                        Button("Quit", settings.s_width // 2, 800 * settings.scaley, lambda: game.button_action("quit"))]

    def run(self):
        """ Main Menu run loop"""
        while True:
            pygame.mixer.music.stop()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.game.current_scene = "quit"
                    
            if self.game.current_scene != "menu":
                return self.game.current_scene
            
            settings.screen.fill(settings.grey)
            for btn in self.buttons:
                btn.update(self.events)

            pygame.display.flip()
            self.clock.tick(60)
