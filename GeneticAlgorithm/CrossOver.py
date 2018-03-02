import math
import random
from NeuralNetwork import NeuralNetworkIndividuals

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

        if random.randint(1, 1000) <= 100:
            newGene[i] = newGene[i] * random.uniform(-1, 1)

    return NeuralNetworkIndividuals.NeuralNetworkIndividuals(numGames, genes=newGene)
