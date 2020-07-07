##############
### IMPORT ###
##############
import numpy

# Function performing uniform crossover 
def crossover(selection, crossover_rate):
	# Information variables
	children = []
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
				
				# Apply the crossover 
				if crossover == True: 
					child1.append(parent2[l])
					child2.append(parent1[l])

				# Does not apply crossover 
				else:
					child1.append(parent1[l])
					child2.append(parent2[l])
			
			# Save the children
			children.append(child1)
			children.append(child2)

		# If there is only one element left 
		except:
			# Save the child without change 
			children.append(selection[i])

	# Return the children 
	return children

	
