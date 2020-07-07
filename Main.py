###############
### IMPORTS ###
###############
import Model
import Algorithm

####################
### INFORMATIONS ###
####################
print("***************")
print("*** KEVOLVE ***")
print("***************\n")

print("Method based on genetic algorithm that uses machine learning to extract a bag of minimal sets of features maximizing a given performance threshold.\n")

##################
### PARAMETERS ###
##################

# Minimum length of k-mer(s)
k_min = 3
# Maximum length of k-mer(s)
k_max = 7
# Model folder path
model_path = "Output"
# Training fasta file path
training_fasta = "Input/data.fasta"
# Training fasta file path
training_csv = "Input/target.csv"
# Testing fasta file path
testing_fasta = "Input/data.fasta"
# Testing fasta file path
testing_csv = "Input/target.csv"

############
### MAIN ###
############

# Prediction
if model_path: Model.predict(model_path, testing_fasta, testing_csv)
# Extraction
else: Algorithm.extraction(training_fasta, training_csv, k_min, k_max)



