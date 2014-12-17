#! /usr/bin/python2.7

import sys
import os
from Bio.Seq import Seq
from Bio import SeqIO
import subprocess


# runs RNAfold and returns the output
def runRNAfold(RNA):
    cmd = ['echo']
    cmd.append(RNA)
    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['RNAfold'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.stdout.read()
    return str(output)


# takes the output of an RNAfold or RNAcofold and returns
# the secondary structure
def get_sec_struc(output):
    out_split = output.split()
    return out_split[1]


# parses the output of RNAfold and RNAcofold and returns the energy score
def get_score(output):
    out_split = output.split("\n")[1].split(" ")[2]
    out_split = out_split[:-1]
    energy = 0.0
    try:
        energy = float(out_split)
    except ValueError, e:
        print "Error: ", e
        print output
    return energy


def get_sec_struct(rna_string):
    output = runRNAfold(rna_string)
    return get_sec_struct(out_split), get_score(output)

################### -- main -- ###################
if __name__ == '__main__':
    print "test"
    rna = "ACACGACGUAGCGUUAGACGUGACGUAGACGUAGAC"
    output = runRNAfold(rna)
    print output
    print get_sec_struc(output)
    print get_score(output)
