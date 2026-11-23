import pygame
from src import settings
from src.scenes.app import App
from src.system.capteur import Instrument
                
class SceneManager:
    """Scene manager, help change the scene to current scene"""
    pygame.init()
    pygame.mixer.init()
    def __init__(self):
        pygame.display.set_caption("Gestophone.exe")
        self.clock = pygame.time.Clock()
        self.current_scene = "main"
        self.scenes = {"main": App(self)}
        self.run()
        
    def run(self):
        """Scene manager run loop"""
        while True:
            scene = self.scenes[self.current_scene]
            scene.run()
            if self.current_scene == "quit":
                Instrument.close()
                pygame.quit()
                break

    def change_scene(self, scene: str):
        """Change the current scene to scene"""
        self.current_scene = scene

    def change_mode(self, instrument):
        return not(instrument.mode)
        