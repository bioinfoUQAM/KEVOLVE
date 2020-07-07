# IMPORT
import numpy

# Function generating initial population
def generateInitialPopulation(n_chromosomes, genes, n_genes, probabilities): 
	population = []
	for i in range (n_chromosomes):	
		population.append(list(numpy.random.choice(genes, n_genes, p = probabilities)))
	return population

# Function generating next population
def generateNextPopulation(n_chromosomes, genes, n_genes, probabilities):
	population = []
	for i in range (int(n_chromosomes / 2)):	
		population.append(list(numpy.random.choice(genes, n_genes, p = probabilities)))
	return population

# Function merging population
def mergePopulation(population, temporaryPopulation):
	for i in temporaryPopulation: population.append(i)
	return population
