# IMPORTS
import csv
import numpy
from Bio import SeqIO

# Function generating the data table 
def generateTrainData(fasta_file, csv_file):
	# Variable data 
	data = []

	# Open the class file
	with open(csv_file) as f: reader = dict(csv.reader(f))

	# Open the sequences file
	for record in SeqIO.parse(fasta_file, "fasta"):
		# Generate table [Id, Sequences, Class]
		if record.id in reader: data.append([record.id, record.seq.upper(), reader[record.id]])

	# Return data
	return data

# Function generating the data table 
def generateTestData(fasta_file, csv_file):
	# Variable data 
	data = []

	# Call classical function
	if csv_file: data = generateTrainData(fasta_file, csv_file)
	else: 
		# Open the sequences file and generate table [Id, Sequences]
		for record in SeqIO.parse(fasta_file, "fasta"): data.append([record.id, record.seq.upper()])
			
	# Return data
	return data

# Function generating mutated data
def generateDataMutated(data, mutation_rate):
	# Alphabet of nucletotide
	alphabet = ["A", "C", "G", "T"]
	# Open data file
	data_file = open("Data/data_mutated.fasta", "w")
	# Open target file
	target_file = open("Data/target_mutated.csv", "w")
	
	for iii in range(100):
		print(iii)
		# For each original data 
		for i, d in enumerate(data):
			# Initialize empty sequence
			sequence = ""
			# For each nucleotide of the initial sequence
			for j, nucleotide in enumerate(d[1]): 
				# Check if we generate mutation or not.
				mutation = numpy.random.choice([True, False], 1, p = [mutation_rate, 1 - mutation_rate])[0]
	
				# If there is a mutation, we generate the new nucleotide
				if mutation == True: 
					possible_mutation = alphabet.copy()
					try: possible_mutation.remove(nucleotide)
					except: pass
					final_mutation = numpy.random.choice(possible_mutation, 1)[0]
					sequence = sequence + final_mutation
				# If there's no mutation we let the initial nucleotide  
				else: sequence = sequence + nucleotide

			# Save the information of the sequence in the data and target files
			data_file.write(">" + str(iii) + d[0] + "_mutated \n" + sequence + "\n")	
			target_file.write(str(iii) + d[0] + "_mutated," + d[2] + "\n")
		
	# Close the data and target files
	data_file.close()
	target_file.close()


