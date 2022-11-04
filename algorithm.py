# Imports
import math
import numpy
import heapq
import statistics
from sklearn.svm import SVC
from operator import itemgetter
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_predict
from sklearn.feature_selection import VarianceThreshold

# Function removing quasi-constant features (itemgetter divide by 10 execution time)
def varianceThreshold(X, K):
	# If it is possible to apply a variance filter
	try:
		# Instancies the filter method
		varianceThreshold = VarianceThreshold(threshold = 0.01)
		# Apply the filter
		X = varianceThreshold.fit_transform(X)
		# Compute the list of k-mers indices to retain 
		indices = [i for i, value in enumerate(varianceThreshold.get_support()) if value == True]
		# Update the list of k-mers
		K = dict.fromkeys(list(itemgetter(*indices)(list(K.keys()))), 0)
		# Clear the indices list
		indices.clear()
	# If not, pass on
	except: pass
	# Return the transformed samples matrix and the updated dictionary of k-mers
	return X, K

# Function generating the gene list
def generateGenes(n_features):
	genes = [i for i in range (n_features)]
	return genes

# Function initializing weights
def initialWeights(genes):
	weights = [1 for i in range(len(genes))]
	return weights

# Function updating weights
def updateWeights(weights, selection, n_features):
	for chromosome in selection:
		for gene in chromosome: 
			weights[gene] = weights[gene] + (math.ceil(1 / 1000 * n_features))
	return weights

# Function generating initial population
def generateInitialPopulation(n_chromosomes, genes, n_genes, weights): 
	# Converts weights into probabilities 
	probabilities = [weights[i] * (1 / sum(weights)) for i in range(len(weights))]
	# Generate the population according to the probabilities 
	population = [list(numpy.random.choice(genes, n_genes, p = probabilities, replace = False)) for i in range (n_chromosomes)]
	return population

# Function generating next population
def generateNextPopulation(n_chromosomes, genes, n_genes, weights):
	# Converts weights into probabilities 
	probabilities = [weights[i] * (1 / sum(weights)) for i in range(len(weights))]
	# Generate the population according to the probabilities
	population = [list(numpy.random.choice(a = genes, size = n_genes, p = probabilities, replace = False)) for i in range (int(n_chromosomes / 2))]
	return population

# Function merging population
def mergePopulation(population, temporaryPopulation):
	for i in temporaryPopulation: population.append(i)
	return population

# Function calculating fitness score
def fitnessCalculation(X, y, population):
	scores = []
	classifier = SVC(kernel = 'linear', C = 1, cache_size = 1000)
	stratifiedKFold = StratifiedKFold(n_splits = 5, shuffle = True, random_state = 0)
	for p in population: 
		y_pred = cross_val_predict(classifier, X[:,p], y, cv = stratifiedKFold, n_jobs = -1)
		score_weighted = f1_score(y, y_pred, average = "weighted")
		score_macro = f1_score(y, y_pred, average = "macro")
		scores.append([score_weighted, score_macro])
	return scores

# Fonction getting and displaying the performaces metric scores
def getScores(scores, max_global_weighted_score, max_global_unweighted_score):
	mean_weighted_score = round(statistics.mean([i[0] for i in scores]), 3)
	max_weighted_score = round(max([i[0] for i in scores]), 3)
	mean_unweighted_score = round(statistics.mean([i[1] for i in scores]), 3)
	max_unweighted_score = round(max([i[1] for i in scores]), 3)
	if max_global_weighted_score < max_weighted_score: max_global_weighted_score = max_weighted_score
	if max_global_unweighted_score < max_unweighted_score: max_global_unweighted_score = max_unweighted_score
	print("Mean weighted score", mean_weighted_score, 
		  "Max weighted score", max_weighted_score, 
		  "Mean unweighted score", mean_unweighted_score, 
		  "Max unweighted score",max_unweighted_score)
	return max_global_weighted_score, max_global_unweighted_score

# Function checking and saving for solution
def checkSolutions(solutions, population, scores, objective_score):
	# Save existing solutions
	for i, score in enumerate(scores):
		if score[0] >= objective_score and score[1] >= objective_score: solutions.append(population[i])
	# Remove duplicate solutions
	temporary = [tuple(x) for x in solutions]
	solutions = list(dict.fromkeys(temporary))
	# Print the number of actual identified solutions
	print("Number of Solutions", len(solutions))
	return solutions

# Function checking objective
def checkObjective(objective_score, scores):
	objective = False
	for s in scores:
		if s[0] >= objective_score and s[1] >= objective_score:
			objective = True
	return objective

# Fonction computing the number of attempts
def compute_n_attempts(objective_score, max_global_weighted_score, max_global_unweighted_score):
	try: n_attempts =  math.ceil(1 / (objective_score - (max_global_weighted_score + max_global_unweighted_score) / 2))
	except: n_attempts = 100
	if n_attempts > 100 or n_attempts < 1: n_attempts = 100
	return n_attempts

# Function selecting next population
def selection(scores, population):
	selection = []
	n = int(len(scores) / 2)
	index = heapq.nlargest(n, range(len(scores)), scores.__getitem__)
	for i in index: selection.append(population[i])
	return selection

# Function performing uniform crossover 
def crossover(selection, crossover_rate):
	children = []
	# Get the length of selected population
	n = len(selection)
	# Scrolls through the selected items two by two 
	for i in range(0, n, 2):
		try:
			# Temporary variables
			parent1 = selection[i]
			parent2 = selection[i+1]
			child1 = []
			child2 = []
			length = len(selection[i])
			# Scrolls through the genes 1 to 1
			for l in range(length):
				# Determines if there is a crossover or not
				crossover = numpy.random.choice([True, False], 1, p = [crossover_rate, 1 - crossover_rate])[0]
				# If crossover is True, apply the crossover 
				if crossover == True:
					# If the gene is not already in the chromosome
					if (parent1[l] not in parent2) and (parent2[l] not in parent1): 
						child1.append(parent2[l])
						child2.append(parent1[l])
					# If the gene is already in the chromosome
					else:
						child1.append(parent1[l])
						child2.append(parent2[l])
				# If crossover is False does not apply crossover 
				else:
					child1.append(parent1[l])
					child2.append(parent2[l])
			# Save the children
			children.append(child1)
			children.append(child2)
		# If there is only one element left 
		except:
			if (n % 2) == 0:
				# Save the child without change 
				children.append(selection[i])
				children.append(selection[i+1])
			else:
				children.append(selection[i])
	# Return the children
	return children

# Function generating mutation
def mutation(selection, mutation_rate, genes, n_genes, objective, n_attempts, attempt):
	# Scroll through each chormosome 
	for i, chromosome in enumerate(selection):
		# Scroll through each chormosome
		for j, gene in enumerate(chromosome): 
			# Determines if there is a mutation or not
			mutation = numpy.random.choice([True, False], 1, p = [mutation_rate, 1 - mutation_rate])[0]
			# If there is mutuation, apply it
			if mutation == True: 
				# Generate new gene
				new_gene =  numpy.random.choice(genes, 1)[0]
				# Generate new gene while already exist in the chromosome 
				while new_gene in chromosome: new_gene =  numpy.random.choice(genes, 1)[0]
				# Add the new gene
				chromosome[j] = new_gene
		# If the objective is not reached and this is the last attempt the chromosome is enlarged
		if objective == False and attempt + 1 == n_attempts:
			# For the number of genes to add to the current chromosome
			for r in range(n_genes - len(chromosome)):
				# Generate additional gene
				additional_gene = numpy.random.choice(genes, 1)[0] 
				# Generate additional gene while already exist in the chromosome 
				while additional_gene in chromosome: additional_gene =  numpy.random.choice(genes, 1)[0]
				# Add the additional gene
				chromosome.append(additional_gene)
	# Return the mutated selection
	return selection