# # Function initializing weights
def initialWeights(genes):
	weights = []
	for i in range (len(genes)): weights.append(1)
	return weights

# # Function updating weights
def updateWeights(weights, selection):
	for chromosome in selection:
		for gene in chromosome: 
			weights[gene] = weights[gene] + 1
	return weights


