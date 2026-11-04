import pygame
from src import settings
from src.ui.button import Button
class Difficulty:
    """Difficulty Menu
    Arg: game: current SceneManager
    """

    def __init__(self, game):
        self.game = game
        self.events = pygame.event.get()
        self.clock = pygame.time.Clock()
        self.buttons = [Button("Easy", settings.s_width // 2, 400 * settings.scaley, lambda: self.choose_dif("Hard")),
                                Button("Medium", settings.s_width // 2, 600 * settings.scaley, lambda: self.choose_dif("Hard")),
                                Button("Hard", settings.s_width // 2, 800 * settings.scaley, lambda: self.choose_dif("Hard"))]
        
    def run(self):
        """Difficulty menu main loop"""
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.game.current_scene = "quit"
                    
            if self.game.current_scene != "difficulty":
                return self.game.current_scene

            settings.screen.fill(settings.grey)
            for btn in self.buttons:
                btn.update(self.events)
            
            pygame.display.flip()
            self.clock.tick(60)

    def choose_dif(self, diff):
        "Changes the difficulty of the game"
        self.game.difficulty = diff