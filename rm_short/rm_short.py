### The purpose of this is to remove contigs shorter than an assigned length from the genome assembly
### I know I can do it manually ... XD
### to use :
### python rm_short.py -input genome.faa -output outputfilename -length N

from Bio import SeqIO
import argparse

##################################################

parser = argparse.ArgumentParser(description = 'The purpose of this is to remove contigs > 500 bp from the genome assembly')
# create argparse
parser.add_argument('-input',
                    help = 'genome assembly, .fasta or .faa.')
# create argument using parser.add_argument
parser.add_argument('-output',
					help = 'output file name')
parser.add_argument('-length',
					help = 'assigned length')
args = parser.parse_args()

##################################################


reader = SeqIO.parse(args.input, format="fasta")
# args.input becomes a file handle for SeqIO
output = [] 
# Setup an empty list for temparary storage

for record in reader:
    if len(record.seq) >= int(args.length) :
		# set up reading condition 
        output.append(record)
		# add the results to empty list
		
SeqIO.write(output, args.output + ".fasta", "fasta")
# write the file using output (list) and name as args.output.fasta
