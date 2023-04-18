# Imports
import os
import sys
from Bio import SeqIO

# Get variants
print(sys.argv[0], sys.argv[1], sys.argv[2])
variants = []
for record in SeqIO.parse("data/" + str(sys.argv[1]) + "/SARS-CoV-2_train_" + str(sys.argv[1]) + ".fasta", "fasta"):
    indexes = [i for i, c in enumerate(record.description) if c == "|"]
    variants.append(record.description[indexes[len(indexes)-1] +1 :])
variants = set(variants)

# Create folders
if not os.path.exists("streme/" + str(sys.argv[1])): os.mkdir("streme/" + str(sys.argv[1]))
if not os.path.exists("streme/" + str(sys.argv[1]) + "/" + sys.argv[2]): os.mkdir("streme/" + str(sys.argv[1]) + "/" + sys.argv[2])

# Open primary/control fasta files
fasta_file_primary = open("streme/" + str(sys.argv[1]) + "/" + sys.argv[2] + "/" + sys.argv[2] + "_primary.fasta", "w")
fasta_file_control = open("streme/" + str(sys.argv[1]) + "/" + sys.argv[2] + "/" + sys.argv[2] + "_control.fasta", "w")
   
# Fill primary/control fasta files
for record in SeqIO.parse("data/" + str(sys.argv[1]) + "/SARS-CoV-2_train_" + str(sys.argv[1]) + ".fasta", "fasta"):
	if record.description.count(sys.argv[2]): fasta_file_primary.write(">" + record.description + "\n" + str(record.seq).upper() + "\n")
	else: fasta_file_control.write(">" + record.description + "\n" + str(record.seq).upper() + "\n")
   
# Close primary/control fasta files    
fasta_file_primary.close()
fasta_file_control.close()
