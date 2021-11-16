# Imports
import data
import numpy
import kmers
import matrix
import algorithm

# Function to extract feature subsets
def extract(parameters):
	# Table of solutions
	solutions = []
	# Number of attempts at the first iteration 
	n_attempts = 1
	# Variable checking if a solution has been identified 
	objective = False
	# Population retained at each iteration
	temporaryPopulation = []	
	# Load the training data
	D = data.loadData(parameters["training_fasta"])
	# Get the k-mers existing in the sequences
	K = kmers.getKmers(parameters["k"], D)
	# Generate the samples matrix (X) and the target values (y)
	X, y = matrix.generateSamplesTargets(D, K , parameters["k"])
	# Variance threshold preprocessing
	X, K = algorithm.varianceThreshold(X, K, parameters["variance_threshold"])
	# Get the number of features
	n_features = numpy.size(X, 1)
	# Initialize the number of genes 
	n_genes = parameters["n_genes"]
	# Initialize gene indexes
	genes = algorithm.generateGenes(n_features)
	# Initialize the weights
	weights = algorithm.initialWeights(genes)

	# Iterate through the number of iterations
	for n in range(parameters["n_iterations"]):
		# Initialize the global scores 
		max_global_weighted_score = 0
		max_global_unweighted_score = 0
		# Iterate through the number of attempts
		for attempt in range(n_attempts):
			print("Iteration: " + str(n + 1) + " | Attempt(s):", str(attempt + 1) + " / " + str(n_attempts))
			# Generate the initial population
			if n == 0: 
				population = algorithm.generateInitialPopulation(parameters["n_chromosomes"], genes, n_genes, weights)
			# Generate the next population
			else:
				population = algorithm.generateNextPopulation(parameters["n_chromosomes"], genes, n_genes, weights)
				population = algorithm.mergePopulation(population, temporaryPopulation)
			# Evaluate the population
			scores = algorithm.fitnessCalculation(X, y, population)
			# Update the scores maximum scores
			max_global_weighted_score, max_global_unweighted_score = algorithm.getScores(scores, max_global_weighted_score, max_global_unweighted_score)
			# Check if they are sone solutions
			solutions = algorithm.checkSolutions(solutions, population, scores, parameters["objective_score"])
			# Check if the goal is reached 
			if objective ==  False: objective = algorithm.checkObjective(parameters["objective_score"], scores)
			# Display the progress of the research 
			print("Number of genes :", n_genes, "\n")
			# Update the number of gene and the mutatiom rate
			if objective == False and attempt + 1 == n_attempts: n_genes = n_genes + 1
			# Select the part of the next generation
			selection = algorithm.selection(scores, population)
			# Update weights
			weights = algorithm.updateWeights(weights, selection, n_features)
			# Apply crossovers
			selection = algorithm.crossover(selection, parameters["crossover_rate"])
			# Apply mutation
			selection = algorithm.mutation(selection, parameters["mutation_rate"], genes, n_genes, objective, n_attempts, attempt)
			# Clear the actual population
			temporaryPopulation.clear()
			# Add the selection to the temporary population
			temporaryPopulation = selection
			# If the objectif is not reached, update the number of attempts
			if attempt + 1 == n_attempts and objective == False: n_attempts = algorithm.compute_n_attempts(parameters["objective_score"], max_global_weighted_score, max_global_unweighted_score)
			# If the objectif is reached, update the number of attempts to 1
			elif attempt + 1 == n_attempts and objective == True: n_attempts = 1
		# If the number of solution is reached, stop the algorithm
		if parameters["n_solutions"] <= len(solutions): break
	# Save the identified solutions
	print("Identified solutions (" + str(len(solutions)) + ") saved at : " + parameters["k_mers_path"])
	kmers.saveExtractedKmers(K = K, solutions = solutions, path = parameters["k_mers_path"])