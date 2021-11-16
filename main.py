# Imports
import ml
import sys
import kevolve
import configuration

# Main program loop
while(True):
	# Display the menu
	print("\n#########################")
	print("######## KEVOLVE ########")
	print("#########################")
	print("\n1) Extract k-mers\n2) Fit an ensemble model\n3) Predict a sequences\n4) Exit/Quit")
	# Get the selected option
	option = int(input("\nSelect an option: "))
	# Get/Update the parameters
	parameters = configuration.getParameters(configuration_file = sys.argv[1])
	# Extract the discriminating k-mers
	if option == 1:
		print("\nKEVOLVE: extraction mode\n")
		kevolve.extract(parameters)
	# Fit a model using a set of k-mers
	elif  option == 2: 
		print("\nKEVOLVE: training mode\n")
		ml.fit(parameters)
	# Predict a set of sequences
	elif  option == 3: 
		print("\nKEVOLVE: testing mode\n")
		ml.predict(parameters)
	# Quit the program
	elif option == 4: 
		print("Program exit")
		sys.exit(0)
	# If the mode specified is not valid
	else: print("The specified option is not valid")