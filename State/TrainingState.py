from Game import GameState
import math
import pygame
from random import randint
from GameBoard import GameBoard
from GeneticAlgorithm import Population


class TrainingState(GameState.GameState):

    def __init__(self, display, gsm):
        super(TrainingState, self).__init__(display, gsm)
        self.board = GameBoard.GameBoard(display)
        self.population = Population.Popuation(5)
        self.population.initialize()
        self.invalidMoves = 0

    def update(self):
        self.updateState()
        direction = self.population.makemove(self.board.board)
        canGo = self.board.update(direction)

        # print("check", self.board.checkIfCanGo())
        # print("canGo", canGo)

        if self.board.checkIfCanGo() == False:
            self.population.update(self.board.score)
            self.board.resetboard()
            self.invalidMoves = 0
        else:
            if canGo == False:
                self.invalidMoves += 1
            else:
                self.invalidMoves = 0

            if self.invalidMoves >= 2:
                self.population.update(self.board.score)
                self.board.resetboard()
                self.invalidMoves = 0



    def draw(self):
        self.board.draw()
        pass

    def updateState(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_q]:
            self.gsm.changeState(0)
        elif key[pygame.K_w]:
            self.gsm.changeState(1)