import pygame
from src import settings
from src.levels.mainmenu import MainMenu
from src.levels.settingsmenu import Settings
from src.levels.difficulty import Difficulty
from src.system.save_load import load, save
                
class SceneManager:
    """Scene manager, help change the scene to current scene"""
    pygame.init()
    pygame.mixer.init()
    def __init__(self):
        pygame.display.set_caption("NAME TO FIND")
        self.audio = load(settings.audio_file, settings.default_audio)
        self.clock = pygame.time.Clock()
        self.current_scene = "menu"
        self.difficulty = ""
        self.scenes = {
        "menu": MainMenu(self),
        "settings": Settings(self),
        "difficulty": Difficulty(self),
        }
        self.run()
        
    def run(self):
        """Scene manager run loop"""
        while True:
            scene = self.scenes[self.current_scene]
            scene.run()
            print(self.current_scene)
            if self.current_scene == "quit":
                pygame.quit()
                break

    def button_action(self, scene: str):
        """Change the current scene to scene"""
        self.current_scene = scene