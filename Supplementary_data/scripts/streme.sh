echo "BEGIN SCRIPT"

export PATH=$HOME/meme/bin:$HOME/meme/libexec/meme-5.5.0:$PATH

for i in {1..100}; do
	for variant in 'Alpha' 'Beta' 'Epsilon' 'Delta' 'Eta' 'Iota' 'Lambda' 'Kappa' 'Gamma' 'Omicron'; do
		python3 generatePrimaryControl.py ${i} ${variant}
		streme --verbosity 1 --oc streme/${i}/${variant} --dna --time 14400 --minw 10 --maxw 10 --nmotifs 10 --align center --p streme/${i}/${variant}/${variant}_primary.fasta --n streme/${i}/${variant}/${variant}_control.fasta
	done
done
echo "END SCRIPT"
