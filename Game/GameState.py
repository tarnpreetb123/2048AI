from abc import ABCMeta, abstractmethod
import pygame
from Game import GameStateManager


class GameState(object):
    __metaclass__ = ABCMeta

    def __init__(self, display, gsm):
        self.display = display
        self.gsm = gsm

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class MenuState(GameState):

    def __init__(self, display, gsm):
        super(MenuState, self).__init__(display, gsm)

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.gsm.changeState(1)
        #elif key[pygame.K_e]:
         #   self.gsm.changeState(2)
        #elif key[pygame.K_r]:
         #   self.gsm.changeState(3)
        #elif key[pygame.K_t]:
         #   self.gsm.changeState(4)

    def draw(self):
        pygame.draw.rect(self.display, (200, 100, 200), pygame.Rect(30, 50, 200, 200))
