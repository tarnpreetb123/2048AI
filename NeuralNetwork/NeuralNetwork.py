from pybrain.structure import FeedForwardNetwork
from pybrain.structure import SigmoidLayer, SoftmaxLayer, TanhLayer, LinearLayer, GaussianLayer
from pybrain.structure import FullConnection
import numpy as np
import math

class NeuralNetwork:

    def __init__(self, genes=None):

        self.net = FeedForwardNetwork()
        self.inLayer = TanhLayer(16)
        self.hiddenLayer = TanhLayer(10)
        self.hiddenLayer2 = TanhLayer(10)
        self.outLayer = SoftmaxLayer(4)

        self.net.addInputModule(self.inLayer)
        self.net.addModule(self.hiddenLayer)
        self.net.addModule(self.hiddenLayer2)
        self.net.addOutputModule(self.outLayer)

        self.in_to_hidden = FullConnection(self.inLayer, self.hiddenLayer)
        self.hidden1_to_hidden2 = FullConnection(self.hiddenLayer, self.hiddenLayer2)
        self.hidden2_to_out = FullConnection(self.hiddenLayer2, self.outLayer)

        self.net.addConnection(self.in_to_hidden)
        self.net.addConnection(self.hidden1_to_hidden2)
        self.net.addConnection(self.hidden2_to_out)

        self.net.sortModules()

        # Set the params to the provided params
        if genes is not None:
            self.net._setParameters(genes)

    def makemove(self, board):
        inputs = []
        inputs.append(np.reshape(board, 16).tolist())
        # print(inputs)

        for i in range(len(inputs[0])):

            if inputs[0][i] != 0:
                inputs[0][i] = math.log(inputs[0][i], 2)

        largest = max(inputs[0])

        for i in range(len(inputs[0])):
            inputs[0][i] /= largest
            inputs[0][i] = round(inputs[0][i], 2)

        # print(inputs)
        #print(inputs[0])
        #print(self.net.params)

        output = self.net.activate(inputs[0])
        largest = max(output)
        index = [i for i, j in enumerate(output) if j == largest]
        return index[0] + 1

    def printParams(self):
        print(self.net.params)

    def getParams(self):
        return self.net.params
