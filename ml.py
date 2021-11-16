# Imports
import os
import data
import kmers
import numpy
import matrix
import joblib
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Function to build the ensemble prediction model
def fit(parameters):
	# Load the training data
	D_train = data.loadData(parameters["training_fasta"])
	# Iterate through the fasta file
	for fasta in (os.listdir(parameters["k_mers_path"])):
		# Get the k-mers of the actual file
		K = kmers.loadKmers(parameters["k_mers_path"] + "/" + fasta)
		# Generate the samples matrix (X_train) and the target values (y_train)
		X_train, y_train =  matrix.generateSamplesTargets(D_train, K , parameters["k"])
		# Instantiate a linear svm classifier
		clf = SVC(kernel = 'linear', C = 1, probability = True, random_state = 0, cache_size = 1000)
		# Fit the classifier
		clf.fit(X_train, y_train)
		# Get index of the separator
		index = fasta.index(".")
		# Get he filename
		file_name = fasta[0:index]
		# Save the model
		joblib.dump(clf, parameters["model_path"] + "/" + file_name + ".pkl")
		# Information message
		print("Model: " + file_name + ".pkl saved at: " + parameters["model_path"])

# Function to predict a set of sequences
def predict(parameters):
	# Table of predictions
	y_pred = []
	# Table of classes
	classes = []
	# Table of belonging probabilities
	probabilities = numpy.empty(0, float)
	# Load the testing data
	D_test = data.loadData(parameters["testing_fasta"])

	# Compute the belonging probability for each model
	for fasta, model in zip(os.listdir(parameters["k_mers_path"]), os.listdir(parameters["model_path"])):
		# Get the current model
		clf = joblib.load(parameters["model_path"] + "/" + model)
		if len(classes) == 0: classes = clf.classes_
		# Get the current k-mers
		K = kmers.loadKmers(parameters["k_mers_path"] + "/" + fasta)
		# Generate the samples matrix (X_test) and the target values (y_test)
		X_test, y_test = matrix.generateSamplesTargets(D_test, K , parameters["k"])
		# Load the current model
		clf =  joblib.load(parameters["model_path"] + "/" + model)
		# Compute the membership probabilities for the initial sub-model 
		if probabilities.shape[0] == 0: probabilities = clf.predict_proba(X_test)
		# Sum the membership probabilities of the additional sub-models 
		else: probabilities += clf.predict_proba(X_test)
	
	# Iterate membership probabilities
	for p in probabilities:
		# Get the maximum score of the array
		max_score = numpy.max(p)
		# Get the index asocciated to the high score of the array
		index = numpy.where(p == max_score)
		# Save the prediction
		y_pred.append(classes[index][0])

	# If evaluation mode is egal to True
	if parameters["evaluation_mode"] == "True":
		# If the target values list is empty
		if len(y_test) == 0: print("Evaluation cannot be performed because target values are not given")
		# Else display the classification report
		else: print("Classification report \n", classification_report(y_test, y_pred))
	# Save the predictions
	f = open(parameters["prediction_path"] + "/prediction.csv", "w")
	# Write the header
	f.write("id,y_pred\n")
	# Iterate through the predictions
	for i, y in enumerate(y_pred): 
		# Save the current prediction
		f.write(D_test[i][0] + "," + y + "\n")
	# Close the file
	f.close()
	# Displays a confirmation message
	print("Predictions saved at the path:", parameters["prediction_path"])