import sys, re
from argparse import ArgumentParser

# Code to recognize the input sequence:
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Sequence to upper case:
args.seq = args.seq.upper()


# Code to calculate the percentage of each nucleotide:

if re.search('^[ACGTU]+$', args.seq): # If it contains any of these nucleotides
     dna_char = ["A", "G", "C", "T", "U"]
     for base in dna_char: # For each nucleotide, compute its percentage
            print("The percentatge of nucleotide", base, "is", args.seq.count(base) / len(args.seq) * 100, "%")
else:
    print ('The sequence is not DNA nor RNA') # If it does not contain any of the nucleotides, print this message
