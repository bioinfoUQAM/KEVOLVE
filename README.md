# Kevolve
* Kevolve v1.0 Help file																		  
* Feature extractor for viral genomic classification                               
* Copyright (C) 2020  Dylan Lebatteux, Abdoulaye Banire Diallo    
* Author : Dylan Lebatteux, Amine M. Remita													  
* Contact : lebatteux.dylan@courrier.uqam.ca

### Description
 Kevolve is a method based on genetic algorithm that uses machine learning to extract a bag of minimal sets of features maximizing a given performance threshold.

### Required softwares
* [python](https://www.python.org/downloads/) 
* [scikit-learn](https://scikit-learn.org/stable/install.html) 
* [numpy](https://numpy.org/install/)
* [scipy](https://www.scipy.org/install.html)                        
* [biopython](https://biopython.org/wiki/Download)    

### Parameters
List of parameters requiring adjustment should be defined in a config file (see the example config_example.ini):
* k_min : Minimum length of k-mer(s)
* k_max : Maximum length of k-mer(s)
* model_path : Model folder path for prediction
* training_fasta : Training fasta file path
* training_csv : Training cv file path
* testing_fasta : Testing fasta file path
* testing_csv : Testing cv file path
* n_iterations : Maximum iteration limit
* n_results = Stop criterion when n_results solution has been identified
* n_chromosomes : Number of feature subset generated at each iteration 
* n_genes : Number of features in the initial population
* objective_score = Score to be achieved by the objective function (between 0 and 1) 

### Utilization
Specify the parameters of the previous section in the Main.py file.
Then run the following command :
```sh
$ python -W ignore Main.py config_example.ini

```
where config_example.ini is a config file containing the list of the required parameters.

Complementary information : 
- The training_fasta and training_csv are required for feature extraction and model construction.
- If the path of a model is filled in, the agorithm will automatically proceed to the prediction step.
- If testing_fasta and testing_csv are not specified there will be no prediction.
- If testing_fasta is specified alone, there will be a prediction without evaluation.
- Finally, if testing_fasta and testing_csv are both specified, there will be prediction with evaluation.

### Input
* FASTA : Contains the sequences in fasta format. Example : 
```sh
>id_sequence_1.description_sequence_1 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
>id_sequence_2.description_sequence_2						
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC
...
...
...
>id_sequence_n-1.description_sequence_n-1												 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
>id_sequence_n.description_sequence_n															 
CTCAACTCAGTTCCACCAGGCTCTGTTGGATCCGAGGGTAAGGGCTCTGTATTTTCCTGC 
```

* CSV :  Contains the classes associated with each sequence. Example :
```sh
id_sequence_1,class_sequence_1																 
id_sequence_2,class_sequence_2																		 
...																		 
...																			 
...	
id_sequence_n-1,class_sequence_n-1																 
id_sequence_n,class_sequence_n	
```

* For more detailed examples see the data sets in the Data folder   

### Output
* Model : Folder containing the prediction model as well as the list of identified features and their relative indexes.                                         
* k_mers.csv : File of the extracted k-mers list   
* indexes.csv: List of indexes of the features of each identified subse
* Prediction_Evaluation.txt : Results file of the evaluation of the testing set 
* Prediction.csv : Results file of the prediction of unknown genomic sequences without evaluation        
* Prediction_Evaluation.csv : Results file of the prediction of unknown genomic sequences with evaluation 
                                             
