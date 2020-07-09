# Imports
import os
import csv
import Data
import numpy
import joblib
import Matrix
import operator
import Preprocessing
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Function of building prediction model
def fit(X, y, Indexes):
	
	# Clear model folder
	filesToRemove = [os.path.join("Output/Model/pkl",f) for f in os.listdir("Output/Model/pkl")]
	for f in filesToRemove: os.remove(f) 

	# Save model
	for i, f in enumerate(Indexes):
		classifier = svm.SVC(kernel = 'linear', C = 1, probability = True, random_state = 0, cache_size = 2000)
		classifier.fit(X[:,f], y)
		joblib.dump(classifier, "Output/Model/pkl/model_" + str (i) + ".pkl")

# Fonction of prediction
def predict(model_path, fasta_path, csv_path):
	# Load model
	Models = []
	print("Load model...")
	list_models = os.listdir(model_path + "/Model/pkl")
	for i, model in enumerate(list_models): Models.append(joblib.load(model_path + "/Model/pkl/model_" + str(i) + ".pkl"))
	targets = Models[0].classes_
	n_targets = len(targets)

	# Get indexes
	Indexes = []
	f = open(model_path + "/Model/indexes.csv", "r")
	reader =  csv.reader(f, delimiter = ",")
	for r in reader:
		index = []
		for i in r: 
			try: index.append(int(i))
			except: pass
		Indexes.append(index)	

	# Get k-mers
	Selected_k_mers = []
	f = open(model_path + "/Model/k_mers.csv", "r")
	reader =  csv.reader(f, delimiter = ",")
	for r in reader: Selected_k_mers.append(r[0])
	print("Number of features :", len(Selected_k_mers))

	# Get values of k_min and k_max
	k_min =  len(min(Selected_k_mers, key = len))
	k_max =  len(max(Selected_k_mers, key = len))
	print("k_min", k_min, "| k_max", k_max)

	# Generate testing matrix
	print("Generate data...")
	data_test = Data.generateTestData(fasta_path, csv_path) 
	X_test, y_test = Matrix.generateMatrice(data_test, Selected_k_mers, k_min, k_max)
	X_test = Preprocessing.minMaxScaling(X_test)
	X_test = numpy.matrix(X_test)

	# Prediction
	y_pred = []
	print("Prediction...")
	# For each instance 
	for i, x in enumerate(X_test):
		scores = []
		# Initialize score for each class
		for n in range(n_targets): scores.append(0)
		# For each sub-model
		for j, model in enumerate(Models):
			probabilities = []
			# Compute the prediction probabilities of the instance with respect to each class
			for p in model.predict_proba(x[:,Indexes[j]]): 
				# Save the probability table
				probabilities.append(p.tolist())
			# For each probability table
			for p in probabilities:
				# Saves the sum of the probabilities associated with each class
				for n in range(n_targets):
					scores[n] = scores[n] + p[n]
		# Get the high score and his index finger
		index, value = max(enumerate(scores), key=operator.itemgetter(1))	
		# Set the class relative to the retrieved index
		y_pred.append(targets[index])	

	# Prediction with evaluation
	if y_test: 
		# Compute performances metrics
		classificationReport = classification_report(y_test, y_pred, digits = 3)
		confusionMatrix = confusion_matrix(y_test, y_pred)
		print("\nClassification report of model evaluation\n", classificationReport)
		print("Confusion matrix \n", confusionMatrix)
	
		# Save results of prediction evaluation
		f = open("Output/Prediction_Evaluation.txt", "w")
		f.write("Classification report of prediction evaluation\n" +  classificationReport);
		f.write("\nConfusion matrix \n" + str(confusionMatrix));
		f.close()

		# Save prediction with evaluation
		f = open("Output/Prediction_Evaluation.csv", "w")
		f.write("id,y_pred,y_true\n");
		for i, y in enumerate(y_pred): f.write(data_test[i][0] + "," + y + "," + y_test[i] + "\n");
		f.close()
	# Prediction without evaluation
	else:
		# Save prediction without evaluation
		f = open("Output/Prediction.csv", "w")
		f.write("id,y_pred\n");
		for i, y in enumerate(y_pred): f.write(data_test[i][0] + "," + y + "\n");
		f.close()

