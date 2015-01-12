#! /usr/bin/python
import sys
import msa_functions
import os

args = sys.argv

def main():
    r, err = os.pipe()
    err = os.fdopen(err, 'w')
    msa_functions.checkargs(args,err)
    fastafile = args[1]
    outfile = args[2]
    print "Infile is",fastafile,"\nOutfile is",outfile
    msa_functions.checkclustal(err)
    msa_functions.checkfasta(fastafile,err)
    print "Starting clustalo"
    msa_functions.runclustal(fastafile,outfile,err)



if __name__ == "__main__":
    main()
