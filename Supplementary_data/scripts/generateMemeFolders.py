# Imports
import os
import sys
from Bio import SeqIO

# Create folders
print(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3])
if not os.path.exists("meme_" + sys.argv[3] + "/" + str(sys.argv[1])): os.mkdir("meme_" + sys.argv[3] + "/" + str(sys.argv[1]))
if not os.path.exists("meme_" + sys.argv[3] + "/" + str(sys.argv[1]) + "/" + sys.argv[2]): os.mkdir("meme_" + sys.argv[3] + "/" + str(sys.argv[1]) + "/" + sys.argv[2])
