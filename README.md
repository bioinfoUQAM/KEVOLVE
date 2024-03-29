# KEVOLVE
* KEVOLVE v1.2 Help file																		  
* K-mers based feature identifier for viral genomic classification                            
* Copyright (C) 2023  Dylan Lebatteux and Abdoulaye Banire Diallo    
* Author : Dylan Lebatteux												  
* Contact : lebatteux.dylan@courrier.uqam.ca

### Description
KEVOLVE, an approach based on a Genetic Algorithm  including a Machine-Learning kernel to extract a bag of minimal subsets of k-mers features maximizing a given classification score threshold. 

### Required softwares
* [python](https://www.python.org/downloads/) 
* [scikit-learn](https://scikit-learn.org/stable/install.html) 
* [numpy](https://numpy.org/install/)                        
* [biopython](https://biopython.org/wiki/Download)  
* [joblib](https://joblib.readthedocs.io/en/latest/)

### Parameters
List of parameters requiring adjustment in the configuration_file.ini :
* k : Length of k-mers
* model_path : Path of the prediction models directory
* training_fasta : Training fasta file path
* testing_fasta: Testing fasta file path
* reference_sequence : Reference sequence file path (file to format GenBank)
* k_mers_path : Path of the directory to save the extracted sets of k-mers
* prediction_path : Path of the directory to save the predictions
* analysis_report_path : Path of the directory to save the the analysis reports
* k_mers_to_analyze_path : Path of the file of k-mers to analyze
* n_iterations : Maximum number of generations of the genetic algorithm
* n_solutions : Maximum number of solutions to identify
* n_chromosomes : Number of feature subset generated at each iteration
* n_genes : Number of k-mers in the initial population
* objective_score : Score to be achieved by the objective function (default = 0.99)
* mutation_rate : Initial mutation rate (default = 0.1)
* crossover_rate : Percentage of crossover in each generation (default = 0.2)
* evaluation_mode : Evaluation mode during the prediction (True/False), require labelled sequences for the predicted set

### Utilization
1) Specify the parameters of the previous section in the configuration_file.ini.
2) Run the following command :
```sh
$ python main.py configuration_file.ini
```
3) Select an option:
- 1.Extract k-mers | Required parameters: k, training_fasta, k_mers_path, n_iterations, n_solution, n_chromosomes, n_genes, objective_score, mutation_rate and crossover_rate
- 2.Fit a model | Required parameters: model_path, training_fasta and k_mers_path
- 3.Predict a sequences | Required parameters: testing_fasta, model_path, prediction_path and evaluation_mode
- 4.Motif analyzer | Required parameters: training_fasta, k_mers_to_analyze_path and reference_sequence and analysis_report_path
- 5.Exit/Quit

### Fasta file format example for n sequences: 

```sh
>id_sequence_1|target_sequence_1 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
>id_sequence_2|target_sequence_2						
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC
...
...
...
>>id_sequence_n-1|target_sequence_n-1									 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
>id_sequence_n|target_sequence_n													 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
```
* The character "|" is used to separate the sequence ID from its target. 
* The target must be specified in the fasta file for a prediction with evaluation_mode = True.
* For more detailed examples see the data sets in the input folder   

### Output    
* k_mers.fasta: File of the extracted k-mers list 
* model.pkl : Prediction model generated by KEVOLVE                                        
* Prediction.csv : Results file of the prediction of unknown genomic sequences   
* Signature.xlsx : Analysis report associated with a discriminative k-mers

### Reference to cite KEVOLVE
* [Lebatteux, Dylan, and Abdoulaye Baniré Diallo. "Combining a genetic algorithm and ensemble method to improve the classification of viruses." 2021 IEEE International Conference on Bioinformatics and Biomedicine (BIBM). IEEE, 2021.](https://ieeexplore.ieee.org/abstract/document/9669670)

### Reference to cite KANALYZER (Option 4: Motif analyzer)
* [Lebatteux, Dylan, et al. "KANALYZER: a method to identify variations of discriminative k-mers in genomic sequences." 2022 IEEE International Conference on Bioinformatics and Biomedicine (BIBM). IEEE Computer Society, 2022.](https://www.computer.org/csdl/proceedings-article/bibm/2022/09995370/1JC2uDIO8cE)
                                                                                  
