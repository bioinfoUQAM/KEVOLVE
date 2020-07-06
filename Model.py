# IMPORTS
import joblib
from sklearn import svm
from statistics import mode 
from collections import Counter 
from sklearn.metrics import f1_score

# FUNCTIONS
def fit(X, y, Indexes):
	for i, f in enumerate(Indexes):
		classifier = svm.SVC(kernel = 'linear', C = 1, probability = True, random_state = 0, cache_size = 2000)
		classifier.fit(X[:,f], y)
		joblib.dump(classifier, "Output/Model/pkl/model_" + str (i) + ".pkl")

def predict(X, Models, Features, y):
	# TODO
	Predictions = []
