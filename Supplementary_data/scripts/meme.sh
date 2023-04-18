# Start script
echo "BEGIN SCRIPT"
# Set meme path
export PATH=$HOME/meme/bin:$HOME/meme/libexec/meme-5.5.0:$PATH
# Iterate throught folds
for i in {1..100}; do
	# Iterate throught variants
	for variant in 'Alpha' 'Beta' 'Epsilon' 'Delta' 'Eta' 'Iota' 'Lambda' 'Kappa' 'Gamma' 'Omicron'; do
		# State psp to false
		isPSP=1
		# Iterate throught variants
		for mode in 'zoops' 'oops'; do 
			# Generate folders
			python3 generateMemeFolders.py ${i} ${variant} ${mode}
			if [ $isPSP -eq 1 ]; then
				# Compute psp
				psp-gen -pos streme/${i}/${variant}/${variant}_primary.fasta -neg streme/${i}/${variant}/${variant}_control.fasta -dna -minw 9 -maxw 9 ­­­­> meme_${mode}/${i}/${variant}/${i}_${variant}_priors.psp
				# Start meme
				meme streme/${i}/${variant}/${variant}_primary.fasta -dna -oc meme_${mode}/${i}/${variant} -nostatus -time 14272 -mod ${mode} -nmotifs 10 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 0 -psp meme_${mode}/${i}/${variant}/${i}_${variant}_priors.psp
				# State psp to true
				isPSP=0
			else
				# Start meme
				meme streme/${i}/${variant}/${variant}_primary.fasta -dna -oc meme_${mode}/${i}/${variant} -nostatus -time 14272 -mod ${mode} -nmotifs 10 -minw 9 -maxw 9 -objfun classic -revcomp -markov_order 0 -psp meme_zoops/${i}/${variant}/${i}_${variant}_priors.psp
				# Remove psp
				python3 removeMemePsp.py ${i} ${variant} ${mode}
			fi
		done
	done
done
# End script
echo "END SCRIPT"
