from Game import GameState
from State import TrainingState

class GameStateManager:

    def __init__(self, display):
        self.display = display
        self.currentState = 0
        self.maxStates = 5
        self.states = [GameState.MenuState(display, self),
                       TrainingState.TrainingState(display, self)]

        #Add states starting with menu state


    def update(self):
        #Ask the current state to update itself
        self.states[self.currentState].update()

    def draw(self):
        #Ask the current state to draw itself
        self.states[self.currentState].draw()

    def changeState(self, newstate):
        if self.maxStates > newstate >= 0:
            self.currentState = newstate
