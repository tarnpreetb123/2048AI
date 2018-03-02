from NeuralNetwork import NeuralNetworkIndividuals
from itertools import accumulate
import random
from GeneticAlgorithm import CrossOver
import numpy as np
from matplotlib import pyplot as plt
import copy as cp

class Popuation:
    def __init__(self, numGames):
        self.pop = []
        self.popSize = 40
        self.currentGeneration = 0
        self.currentGame = 0
        self.currentIndividual = 0
        self.currentPopGame = []
        self.numGames = numGames
        self.averageFitness = np.array([[0, 0]])

    def initialize(self):

        for i in range(self.popSize):
            self.pop.append(NeuralNetworkIndividuals.NeuralNetworkIndividuals(self.numGames))
            # self.currentPopGame.append(0)

        print(self.pop)

    def makemove(self, board):
        return self.pop[self.currentIndividual].makemove(board)

    def update(self, score):

        # Save the game data
        print("Score: ", score)
        print("CurrentGame: ", self.currentGame, " CurrentNet: ", self.currentIndividual, " CurrentGeneration: ", self.currentGeneration)

        self.pop[self.currentIndividual].setScore(self.currentGame, score)

        # Update the currentGame
        self.currentGame += 1
        # if max games are reached update the currentNet
        if self.currentGame == self.numGames:
            self.currentGame = 0
            self.currentIndividual += 1
        # if max nets are reached update the generation and crossover/evolve each net
        if self.currentIndividual == self.popSize:
            self.currentIndividual = 0
            self.currentGeneration += 1

            sumFitness = 0.1
            for i in range(self.popSize):
                self.pop[i].calcFitness()
                print(self.pop[i].getFitness())
                sumFitness += self.pop[i].getFitness()
                # print(self.pop[i].printData())

            # print("sorted")
            self.pop.sort(key=lambda x: x.getFitness(), reverse=True)

            self.pop[0].setFitness(self.pop[0].getFitness() * 100)
            self.pop[1].setFitness(self.pop[1].getFitness() * 50)
            self.pop[2].setFitness(self.pop[2].getFitness() * 50)

            # print("normalize")
            for i in range(self.popSize):
                self.pop[i].setFitness(self.pop[i].getFitness()/sumFitness)

            # print("sorted")
            self.pop.sort(key=lambda x: x.getFitness(), reverse=True)

            allFitness = []
            for i in range(self.popSize):
                allFitness.append(self.pop[i].getFitness())

            accumulateFitness = list(accumulate(allFitness))

            for i in range(self.popSize):
                self.pop[i].setAccumulatedFitness(accumulateFitness[i])

            newPop = []
            for i in range(self.popSize):
                a = self.getParent()
                b = self.getParent()

                newPop.append(CrossOver.CrossOver(a, b, self.numGames))

            newPop[0] = cp.deepcopy(self.pop[0])
            newPop[1] = cp.deepcopy(self.pop[0])
            newPop[2] = cp.deepcopy(self.pop[0])
            newPop[3] = cp.deepcopy(self.pop[0])
            newPop[4] = cp.deepcopy(self.pop[0])
            self.pop = newPop
            # print(newPop)
            # print(len(newPop))

            averageFitness = sumFitness/ self.popSize
            self.averageFitness = np.append(self.averageFitness, [[self.currentGeneration, averageFitness]], axis=0)
            x, y = self.averageFitness.T
            plt.ion()
            plt.scatter(x, y)
            plt.pause(0.05)
            plt.show()

    def getParent(self):
        randomInt = random.random()

        for i in range(self.popSize):
            if randomInt < self.pop[i].getAccumulatedFitness():
                return cp.deepcopy(self.pop[i])
            else:
                return cp.deepcopy(self.pop[0])
