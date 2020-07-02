# IMPORT
import os
import Gene
import Data
import numpy
import K_mers
import Weight
import Matrix
import Fitness
import Solution
import Mutation
import itertools
import Objective
import Selection
import Crossover
import Population
import statistics
import Probabilities
from Bio import SeqIO
from sklearn import datasets




# HIV-1 \ GC \ 423 INSTANCES \ 18 CLASSES \ 146 FEATURES (Castor)


# HIV-1 \ GC \ 423 INSTANCES \ 18 CLASSES \ 146 FEATURES (Castor)
k = 8
data = Data.generateData("data/data.fasta", "data/target.csv")
K_mers = K_mers.generate_K_mers(data, k)
print("Number of features :", len(K_mers))
X, y = Matrix.generateMatrice(data, K_mers, k)
X = numpy.matrix(X)



data_mutated = Data.generateData("data/data_mutated.fasta", "data/target_mutated.csv")
print("Number of features :", len(K_mers))
X_mutated, y_mutated = Matrix.generateMatrice(data_mutated, K_mers, k)
X_mutated = numpy.matrix(X_mutated)


from sklearn import svm
from sklearn.metrics import f1_score
classifier = svm.SVC(kernel='linear', C = 1)
classifier.fit(X, y)
y_pred = classifier.predict(X_mutated)
score = f1_score(y_mutated, y_pred, average ="weighted") 
print("SVM", score)







"""
# HIV-1 
k = 8
mutation_rate = 0.1
alphabet = ["A", "C", "G", "T"]
data = Data.generateData("data/data.fasta", "data/target.csv")
data_mutated = data

if os.path.exists("data_mutated.fasta"): os.remove("data_mutated.fasta")
else: print("The file does not exist") 
file_data = open("data_mutated.fasta", "w")

if os.path.exists("target_mutated.csv"): os.remove("target_mutated.csv")
else: print("The file does not exist") 
file_target = open("target_mutated.csv", "w")


for i, d in enumerate(data):
	sequence = ""
	print(i , len(sequence))
	for j, nucleotide in enumerate(d[1]): 
		mutation = numpy.random.choice([True, False], 1, p = [mutation_rate, 1 - mutation_rate])[0]
	
		if mutation == True: 
			possible_mutation = alphabet.copy()
			try: possible_mutation.remove(nucleotide)
			except: pass
			final_mutation = numpy.random.choice(possible_mutation, 1)[0]
			sequence = sequence + final_mutation
		else: sequence = sequence + nucleotide

	file_data.write(">" + d[0] + "_mutated " + d[2] + "\n" + sequence + "\n")	
	file_target.write(d[0] + "_mutated," + d[2] + "\n")
	
file_data.close()
file_target.close()

"""

