# Imports
import os
import sys
from Bio import SeqIO

# Get variants
variants = []
for record in SeqIO.parse("data/1/SARS-CoV-2_train_1.fasta", "fasta"):
    indexes = [i for i, c in enumerate(record.description) if c == "|"]
    variants.append(record.description[indexes[len(indexes)-1] +1 :])
variants = set(variants)

# Remove fasta files
for i in range (1, 101):
	for variant in variants:
		os.remove("streme_output/" + str(i) + "/" + variant + "/" + variant + "_primary.fasta")
		os.remove("streme_output/" + str(i) + "/" + variant + "/" + variant + "_control.fasta")
		print("Remove fasta files from " + "streme_output/" + str(i) + "/" + variant)
