def to_rna(dna):
    """Transcribe DNA to RNA"""
# I cheated so much on this one, trying to be too clever and got nowhere
    bases = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for nucleotide in dna:
        if nucleotide in bases.keys():
            continue
        else:
            return ''
    return ''.join(bases[nucleotide] for nucleotide in dna)
