# Function checking for solution
def checkSolutions(population, scores, objective_score):
	solutions = []
	for i, score in enumerate(scores):
		if score[0] >= objective_score and score[1] >= objective_score: 
			solutions.append(population[i])
	return solutions
	
# Function saving solution	
def saveSolutions(results, solutions):
	for i in solutions: results.append(i)
	results = [list(item) for item in set(tuple(row) for row in results)]
	return results
