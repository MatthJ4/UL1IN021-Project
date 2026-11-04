import pygame
from src import settings
from src.ui.button import Button
from src.ui.soundsettings import SoundSettings
from src.system.save_load import save
class Settings:
    """Settings Menu
    Arg: game: current Scenemanager
    """
    def __init__(self, game):
        self.game = game
        self.events = pygame.event.get()
        self.clock = pygame.time.Clock()
        self.button = Button("Return", settings.s_width // 2, 800 * settings.scaley, lambda: game.button_action("menu"))
        self.sound_settings = SoundSettings(200* settings.scalex, 250 * settings.scaley, self.game)
        
    def run(self):
        """Setting Menu main loop"""
        while True:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.game.current_scene = "quit"
                self.sound_settings.handle_event(event)
                    
            if self.game.current_scene != "settings":
                return self.game.current_scene
                    
            settings.screen.fill(settings.grey)
            
            self.sound_settings.draw(settings.screen)
            self.button.update(self.events)
            save(settings.audio_file, self.game.audio)
            
            pygame.display.flip()
            self.clock.tick(60)