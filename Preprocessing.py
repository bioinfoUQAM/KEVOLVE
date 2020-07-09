# Import
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold

# Function of MinMaxScaler (0, 1)
def minMaxScaling(X):
	minMaxScaler = MinMaxScaler(feature_range = (0, 1), copy = False)
	X = minMaxScaler.fit_transform(X)
	return X

# Function removing quasi-constant features
def varianceThreshold(X, k_mers):
	# Instancies the filter method  
	varianceThreshold = VarianceThreshold(threshold = 0.01)

	# Apply the filter
	X = varianceThreshold.fit_transform(X)

	# Update list of k_mers
	for i, value in enumerate(varianceThreshold.get_support()):
		if value == False: k_mers[i] = None
	k_mers = list(filter(lambda a: a != None, k_mers))

	# Return new Matrix and k-mers list
	return X, k_mers
