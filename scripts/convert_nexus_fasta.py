#!/usr/bin/env python3

from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str, required=True)
args = parser.parse_args()

new_filename = os.path.splitext(args.file)[0] + ".fasta"

with open(new_filename, 'w') as fasta_file:
    SeqIO.write(SeqIO.parse(args.file, 'nexus'), fasta_file, 'fasta')
