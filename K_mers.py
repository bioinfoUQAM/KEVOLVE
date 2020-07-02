# IMPORTS
import re

# FUNCTION
def generate_K_mers(data, k):
	# List of k-mer
	K_mers = []
	dict = {}

	# Initialization of the dictionary
	for i in range(k + 1):
		for d in data:
			for j in range(0, len(d[1]) - i + 1, 1): 
				dict[d[1][j:j + i]] = 0;
		
	# Remove patterns not used
	for key in dict.keys():
		if bool(re.match('^[ACGT]+$', str(key))) == True: K_mers.append(str(key))
	
	# Return K_mer
	return K_mers
