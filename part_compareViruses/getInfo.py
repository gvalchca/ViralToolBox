__author__ = 'Mirjam Figaschewski'


def getMetadata(substring, pdf, start=0, end=None):
    if end is None:
        end = len(pdf)
    substring_start = pdf.find(
        substring + '\n', start, end) + len(substring + '\n')
    substring_end = pdf.find('\n', substring_start)
    data = pdf[substring_start: substring_end]
    return data


def getSecStructInfo(pdf):
    # get naeme
    name = getMetadata('Virus name:', pdf)
    # get sequence
    seq = getMetadata('Sequence:', pdf)
    # get dot bracket notation for sequence
    secstruct = getMetadata('Structure in dot-bracket format:', pdf)
    # get energy of secondary structure
    seq_energy = getMetadata('Energy:', pdf)
    return name, seq, secstruct, seq_energy


def getProteinInfo(pdf):
    numProteins = int(getMetadata('Number of proteins:', pdf))
    if numProteins > 0:
        proteins = {}
        i = 1
        # for each protein get its aminoacid sequence and its domains
        while i <= numProteins:
            protein = 'Protein ' + str(i)
            protein_start = pdf.find(protein) + len(protein + '\n')
            if i < numProteins:
                next_protein = 'Protein ' + str(i + 1)
                protein_end = pdf.find(next_protein, protein_start)
            else:
                protein_end = len(pdf)
            # amino acid sequence
            aaSeq = getMetadata(
                'Aminoacidsequence:', pdf, protein_start, protein_end)
            # start and end in DNA sequence
            startInDNASequence = getMetadata(
                'Starting nucleotide position:',
                pdf, protein_start, protein_end)
            endInDNASequence = getMetadata(
                'Ending nucleotide position:', pdf, protein_start, protein_end)
            proteins[protein] = {
                'Aminoacidsequence:': aaSeq,
                'Starting nucleotide position:': startInDNASequence,
                'Ending nucleotide position:': endInDNASequence}
            # number of domains
            numDomains = int(getMetadata(
                'Number of domains:', pdf, protein_start, protein_end))
            # get information for each domain (position, description, ...)
            if numDomains > 0:
                domains = {}
                j = 1
                while j <= numDomains:
                    domain = 'Domain' + str(j)
                    domain_start = pdf.find(
                        domain, protein_start, protein_end) + \
                        len(domain + '\n')
                    domain_end = pdf.find('\n\n', domain_start)
                    # description = getMetadata(
                    #     'description', pdf, domain_start, domain_end)
                    startInProteinSequence = getMetadata(
                        'Starting aminoacid position:', pdf,
                        domain_start, domain_end)
                    endInProteinSequence = getMetadata(
                        'Ending aminoacid position:', pdf, domain_start, domain_end)
                    # identifier = getMetadata(
                    #     'identifier', pdf, domain_start, domain_end)
                    domains[domain] = {
                        'Starting aminoacid position:': startInProteinSequence,
                        'Ending aminoacid position:': endInProteinSequence}
                        #'description': description,
                        #'identifier': identifier}
                    j += 1
            elif numDomains == 0:
                i += 1
                continue
            proteins[protein].update(domains)
            i += 1
        return numProteins, proteins


def getInformation(pdf):
    # get sequence, dot bracket notation for sequence and
    # energy of secondary structure
    print 'Get sequences, secondary structure and its energy'
    name, seq, secstruct, seq_energy = getSecStructInfo(pdf)
    # get proteins and their domains
    print 'Get Proteins and their domains'
    numProteins, proteins = getProteinInfo(pdf)
    return name, seq, secstruct, seq_energy, numProteins, proteins


def main():
    f = open('sec_struct.txt').read()
    print getSecStructInfo(f)


if __name__ in "__main__":
    main()