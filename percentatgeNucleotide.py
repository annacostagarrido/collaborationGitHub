import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper()


# podriem posar una funcio que identifiques si es dna o rna (reutilitzant la que hem fet abans) i a partir d'aquí fer el codi següent:

if re.search('^[ACGTU]+$', args.seq):
     dna_char = ["A", "G", "C", "T", "U"]
     for base in dna_char:
            print("The percentatge of nucleotide", base, "is", args.seq.count(base) / len(args.seq) * 100, "%")
else:
    print ('The sequence is not DNA nor RNA')
