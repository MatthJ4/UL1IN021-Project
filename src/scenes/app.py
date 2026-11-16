import pygame
from src.ui.button import Button
from src import settings
from src.system import capteur

class App:
    """The main app
    Arg: game: current scene manager"""
    def __init__(self, app):
        self.app = app
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.font =  pygame.font.SysFont("Times New Roman", 14)
        self.buttons = [Button("Record", 200*settings.scalex, 100*settings.scaley, lambda: app.button_action())]

    def run(self):
        """ Main Menu run loop"""
        while True:
            pygame.mixer.music.stop()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.app.current_scene = "quit"
                    
            if self.app.current_scene != "main":
                return self.app.current_scene
            
            settings.screen.fill(settings.grey)
            for btn in self.buttons:
                btn.update(self.events)
            capteur.instrument()

            pygame.display.flip()
            self.clock.tick(60)
