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

def seq_type(seq):
    if re.search('^[ACGTUN]+$', seq): # If the seq contains these characters is DNA or RNA
        if "U" not in seq and "T" in seq: # If the seq contains T but not U, is DNA
            return('DNA')
        elif "T" not in seq and "U" in seq: # If the seq contains U but not T, is RNA
            return('RNA')
        else:
            return('DNA or RNA') 
    else:
        return('The sequence is not DNA nor RNA')

# Code to calculate the percentage of each nucleotide:

if seq_type(args.seq)=="DNA": # If it contains any of these nucleotides
     dna_char = ["A", "G", "C", "T"]
     for base in dna_char: # For each nucleotide, compute its percentage
            print("The percentatge of nucleotide", base, "is", args.seq.count(base) / len(args.seq) * 100, "%")
elif seq_type(args.seq)=="RNA": # If it contains any of these nucleotides
     dna_char = ["A", "G", "C", "U"]
     for base in dna_char: # For each nucleotide, compute its percentage
            print("The percentatge of nucleotide", base, "is", args.seq.count(base) / len(args.seq) * 100, "%")
elif seq_type(args.seq)=="DNA or RNA": # If it contains any of these nucleotides
     dna_char = ["A", "G", "C"]
     for base in dna_char: # For each nucleotide, compute its percentage
            print("The percentatge of nucleotide", base, "is", args.seq.count(base) / len(args.seq) * 100, "%")
else:
    print ('The sequence is not DNA nor RNA') # If it does not contain any of the nucleotides, print this message

