# IMPORT
import numpy

# Function generating mutation
def mutation(selection, mutation_rate, genes, objective):

	# Scroll through each chormosome 
	for i, chromosome in enumerate(selection):
		# Scroll through each chormosome
		for j, gene in enumerate(chromosome): 
			# Determines if there is a mutation or not
			mutation = numpy.random.choice([True, False], 1, p = [mutation_rate, 1 - mutation_rate])[0]

			# If there is mutuation, apply it
			if mutation == True: new_gene = numpy.random.choice(genes, 1)[0]
				
		# If the objective is not reached the chromosome is enlarged
		if objective ==  False: 
			additional_gene = numpy.random.choice(genes, 1)[0] 
			selection[i].append(additional_gene)

	# Return the mutated selection 
	return selection
