# IMPORT 
import heapq

# Function selecting next population
def selection(scores, population):
	selection = []
	n = int(len(scores) / 2)
	index = heapq.nlargest(n, range(len(scores)), scores.__getitem__)
	for i in index: selection.append(population[i])
	return selection
