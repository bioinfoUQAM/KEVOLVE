# IMPORT
import Gene
import Data
import numpy
import K_mers
import Weight
import Matrix
import Model
import Fitness
import operator
import Solution
import Mutation
import Objective
import Selection
import Crossover
import Population
import statistics
import Probabilities
from sklearn import datasets


# GENERATE DATA
k = 4 # Ajouter k_min et k_max
print("Loading data")
data = Data.generateData("Input/data.fasta", "Input/target.csv")
print("Generating K-mers")
K_mers = K_mers.generate_K_mers(data, k)
print("Number of features :", len(K_mers))
X, y = Matrix.generateMatrice(data, K_mers, k)
X = numpy.matrix(X)


# INITIALIZE VIARIABLES
n_features = numpy.size(X,1)
n_iterations = 250
n_results = 100
n_chromosomes = 200
n_genes = 3
crossover_rate = 0.2
mutation_rate = 1 / n_genes
objective = False
objective_score = 0.85


# MAIN
results = []
temporaryPopulation = []
genes = Gene.generateGenes(n_features)
weights = Weight.initialWeights(genes)
probabilities = Probabilities.calculProbabilities(weights)

# EVOLUTION
for n in range(n_iterations):

	print("\nIteration", n + 1)

	if n == 0: 
		population = Population.generateInitialPopulation(n_chromosomes, genes, n_genes, probabilities)
		print("Size of the population", len(population))
	else:
		population = Population.generateNextPopulation(n_chromosomes, genes, n_genes, probabilities)
		population = Population.mergePopulation(population, temporaryPopulation)
		print("Size of the population", len(population))
	
	scores = Fitness.fitnessCalculation(X, y, population)
	print("Mean weighted score", round(statistics.mean([i[0] for i in scores]), 3), 
	      "Max weighted score", round(max([i[0] for i in scores]), 3), 
	      "Mean macro score", round(statistics.mean([i[1] for i in scores]), 3), 
	      "Max macro score", round(max([i[1] for i in scores]), 3))

	solutions = Solution.checkSolutions(population, scores, objective_score)
	print("Number of Solutions", len(solutions))

	results = Solution.saveSolutions(results, solutions)
	print("Number of Results", len(results))

	if objective ==  False: objective = Objective.checkObjective(objective_score, scores)
	print("Objective :", objective)
	
	if objective ==  False: 
		n_genes = n_genes + 1
		mutation_rate = 1 / n_genes
	print("Number of genes :", n_genes)

	selection = Selection.selection(scores, population)
	print("Number of selection", len(selection))

	weights = Weight.updateWeights(weights, selection)
	print("Update weights")

	probabilities = Probabilities.calculProbabilities(weights)
	print("Update probabilities")

	selection = Crossover.crossover(selection, crossover_rate)
	print("Apply crossovers")

	selection = Mutation.mutation(selection, mutation_rate, genes, objective)
	print("Apply mutation")

	temporaryPopulation.clear()
	temporaryPopulation = selection
	
	if n_results <= len(results): break

print("Number of results =", len(results))




feature_sets = []
for result in results: 
	print(result)
	feature_sets.append(result)


Indexes = []
Selected_k_mers = []

for f in feature_sets:
	index = []
	for i in f: 
		if K_mers[i] not in Selected_k_mers: 
			Selected_k_mers.append(K_mers[i])
			index.append(Selected_k_mers.index(K_mers[i]))
		else: index.append(Selected_k_mers.index(K_mers[i]))

	Indexes.append(index)

print("TRAIN")

for i, indice in enumerate (Indexes):
	for j, ele in enumerate(indice):
		print(K_mers[feature_sets[i][j]],  Selected_k_mers[ele])


feature_sets = Indexes

# FIT
print("Number of features :", len(K_mers))
X, y = Matrix.generateMatrice(data, Selected_k_mers, k)
X = numpy.matrix(X)


Models = Model.fit(X, y, feature_sets)
targets = Models[0].classes_
n_targets = len(targets)
# PREDICT

k = 7
dataTest = Data.generateData("Data/data_Test.fasta", "Data/target_Test.csv")
################################################
# GENERATE MATRICE ONLY FOR EXTRACTED FEATURES #
################################################
print("TEST")
X_test, y_test = Matrix.generateMatrice(dataTest, Selected_k_mers, k)

X_test = numpy.matrix(X_test)

print(X_test)

y_pred = []

print(len(X_test), len(y_test))

# Pour chaque instance 
for i, x in enumerate(X_test):
	print("\n Instance:", i, y_test[i])
	scores = []
	for n in range(n_targets): scores.append(0)
	print(scores)
	# Pour chaque model
	for j, model in enumerate(Models):
		probabilities = []

		# Calcul les probabilités de prediction de l'instance par rapport à chaque classes
		for p in model.predict_proba(x[:,feature_sets[j]]): 
			# Sauvegarde un de tableau de n_targets probabilités
			probabilities.append(p.tolist())
		
		# Pour chaque tableau de probabilité
		for p in probabilities:
			#print("Model :", j)
			# Sauvegarde les probabilités associées à chaque classes
			for n in range(n_targets):
				#print(p[n], targets[n])
				scores[n] = scores[n] + p[n]

	for n in range(n_targets): print(scores[n], targets[n])
		
	# Recupère le meilleur score et son index
	index, value = max(enumerate(scores), key=operator.itemgetter(1))

	print(index, value, y_test[i], targets[index])
	
	y_pred.append(targets[index])	

from sklearn.metrics import f1_score
print("f1-score =", f1_score(y_test, y_pred, average ="weighted"))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

for i, e in enumerate(y_test):
	print(e, y_pred[i])



