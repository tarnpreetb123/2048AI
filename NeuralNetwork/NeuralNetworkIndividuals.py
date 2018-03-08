from NeuralNetwork.NeuralNetwork import NeuralNetwork

class NeuralNetworkIndividuals:
    def __init__(self, numGames, genes=None):
        self.neuralNetwork = NeuralNetwork() if genes is None else NeuralNetwork(genes)
        self.fitness = None
        self.accumulatedFitness = None
        self.numGames = numGames
        self.score = [0 for i in range(numGames)]
        self.genes = []


    def calcFitness(self):
        averageScore = sum(self.score)/self.numGames
        self.fitness = averageScore

        if self.fitness < 0:
            self.fitness = 0.1

    def getNetGenes(self):
        return self.neuralNetwork.getParams()

    def makemove(self, board):
        return self.neuralNetwork.makemove(board)

    def getFitness(self):
        return self.fitness

    def setFitness(self, fitness):
        self.fitness = fitness

    def getAccumulatedFitness(self):
        return self.accumulatedFitness

    def setAccumulatedFitness(self, fitness):
        self.accumulatedFitness = fitness

    def setScore(self, i, value):
        self.score[i] = value

    def printData(self):
        print("Winner: ", self.score)

    def setParams(self, genes):
        self.neuralNetwork.setParams(genes)