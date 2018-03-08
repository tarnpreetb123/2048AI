import math
import random
from NeuralNetwork import NeuralNetworkIndividuals

#: mutation probability
mutationProb = 0.1
mutationStdDev = 0.5
initRangeScaling = 10.

def CrossOver(netIndividual1, netIndividual2, numGames):
    genesA = netIndividual1.getNetGenes()
    genesB = netIndividual2.getNetGenes()

    # Crossover by taking first half of geneA and second half of geneB
    midPoint = math.floor(len(genesA)/2)
    endPoint = math.floor(len(genesA))

    newGene = genesA[0: midPoint].tolist()

    # print(genesA)
    # print(genesB)
    # print(newGene)
    newGene.extend(genesB[midPoint: endPoint])

    # Mutate 1/1000 chance
    for i in range(len(newGene)):

        if random.random() < mutationProb:
            # newGene[i] = newGene[i] * random.uniform(-1, 1)
            newGene[i] = newGene[i] + random.gauss(0, mutationStdDev)

    return NeuralNetworkIndividuals.NeuralNetworkIndividuals(numGames, genes=newGene)

def mutate(newGene):
    for i in range(len(newGene)):

        if random.random() < mutationProb:
            # newGene[i] = newGene[i] * random.uniform(-1, 1)
            newGene[i] = newGene[i] + random.gauss(0, mutationStdDev)
    return newGene
