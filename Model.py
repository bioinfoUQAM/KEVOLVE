# IMPORTS
from sklearn import svm
from statistics import mode 
from collections import Counter 
from sklearn.metrics import f1_score

# FUNCTIONS
def fit(X, y, Features):
	Models = []
	for i, f in enumerate(Features):
		classifier = svm.SVC(kernel = 'linear', C = 1, probability = True, random_state = 0, cache_size = 1000)
		Models.append(classifier.fit(X[:,f], y))
	return Models



def predict(X, Models, Features, y):
	
	Predictions = []
	for i, f in enumerate(Features):
		y_pred = Models[i].predict(X[:,f])
		score = f1_score(y, y_pred, average ="weighted")
		print(i, score)
		Predictions.append(y_pred)
	y_pred = []
	for i in range(len(Predictions[0])): 
		List = []
		for j in range(len(Predictions)):List.append(Predictions[j][i])
		y_pred.append(Counter(List).most_common(1)[0][0])

	print("f1-score =", f1_score(y, y_pred, average ="weighted"))
	

