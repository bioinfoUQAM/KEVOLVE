###############
### IMPORTS ###
###############
import sys
import configparser

import Model
import Algorithm

####################
### INFORMATIONS ###
####################
print("***************")
print("*** KEVOLVE ***")
print("***************\n")

print("Method based on genetic algorithm that uses machine learning to extract a bag of minimal sets of features maximizing a given performance threshold.\n")


############
### MAIN ###
############

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Config file is missing!!")
        sys.exit()

    # Get argument values from ini file
    config_file = sys.argv[1]
    config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation())

    with open(config_file, "r") as cf:
        config.read_file(cf)

    ##################
    ### PARAMETERS ###
    ##################

    params = dict()

    # Model folder path
    params["model_path"] = config.get("io", "model_path")
    # Training fasta file path
    params["training_fasta"] = config.get("io", "training_fasta")
    # Training fasta file path
    params["training_csv"] = config.get("io", "training_csv")
    # Testing fasta file path
    params["testing_fasta"] = config.get("io", "testing_fasta")
    # Testing fasta file path
    params["testing_csv"] = config.get("io", "testing_csv")

    # Minimum length of k-mer(s)
    params["k_min"] = config.getint("kmers", "k_min")
    # Maximum length of k-mer(s)
    params["k_max"] = config.getint("kmers", "k_max")

    # Extrcation/prediction modes
    params["extract"] = config.getboolean("kmers", "extract")

    # Algorithm parameters
    params["n_iterations"] = config.getint("algorithm", "n_iterations")
    params["n_results"] = config.getint("algorithm", "n_results")
    params["n_chromosomes"] = config.getint("algorithm", "n_chromosomes")
    params["n_genes"] = config.getint("algorithm", "n_genes")
    params["crossover_rate"] = config.getfloat("algorithm", "crossover_rate")
    #params["mutation_rate"] = config.getfloat("algorithm", "mutation_rate")
    params["objective"] = config.getboolean("algorithm", "objective")
    params["objective_score"] = config.getfloat("algorithm", "objective_score")
    params["cv_n"]  = config.getint("algorithm", "cv_n")
    params["cv_shuffle"] = config.getboolean("algorithm", "cv_shuffle")
    params["cv_n_jobs"] = config.getint("algorithm", "cv_n_jobs")

    # Preprocess parameters
    params["var_threshold"] = config.getfloat("preprocess", "var_threshold")

    ####################
    ### Main program ###
    ####################

    # Extraction mode
    if params["extract"]: 
        Algorithm.extraction(params)
    # Prediction mode
    else: 
        Model.predict(params["model_path"], params["testing_fasta"], params["testing_csv"])

