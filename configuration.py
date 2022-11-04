# Import
import configparser

# Fonction to get the parameters from the configuration file
def getParameters(configuration_file):
	# Initialize the parser
	configurationParser = configparser.ConfigParser()
	# Read the configuration file
	configurationParser.read(configuration_file)
	# Get the parameters
	parameters = dict()
	parameters["k"] = int(configurationParser.get("parameters", "k"))
	parameters["n_genes"] = int(configurationParser.get("parameters", "n_genes"))
	parameters["model_path"] = str(configurationParser.get("parameters", "model_path"))
	parameters["k_mers_path"] = str(configurationParser.get("parameters", "k_mers_path"))
	parameters["n_solutions"] = int(configurationParser.get("parameters", "n_solutions"))
	parameters["n_iterations"] = int(configurationParser.get("parameters", "n_iterations"))
	parameters["n_chromosomes"] = int(configurationParser.get("parameters", "n_chromosomes"))
	parameters["testing_fasta"] = str(configurationParser.get("parameters", "testing_fasta"))
	parameters["training_fasta"] = str(configurationParser.get("parameters", "training_fasta"))
	parameters["prediction_path"] = str(configurationParser.get("parameters", "prediction_path"))
	parameters["evaluation_mode"] = str(configurationParser.get("parameters", "evaluation_mode"))
	parameters["objective_score"] = float(configurationParser.get("parameters", "objective_score"))
	parameters["mutation_rate"] = float(configurationParser.get("parameters", "mutation_rate"))
	parameters["crossover_rate"] = float(configurationParser.get("parameters", "crossover_rate"))
	# Return the parameter dictionary
	return parameters