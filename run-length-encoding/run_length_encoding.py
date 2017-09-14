"""Implement run-length encoding and decoding.
"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
unencoded string will only contain A-Z (lower or upper) and whitespace.
data to be encoded never contain any numbers and numbers inside data to
be decoded always represent the count for the following character."""


def decode(code):
    """Decode a mixed letters/number string to only letters"""

    # if any(char.isdigit() for char in code):
    #     if char.isalpha in code.strip().upper():
    #         outcode.append(char)
    #     else:
    #         outcode.append(int(char)*(char+1))

    # elif:
        # pass to encode
    bases = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for nucleotide in dna:
        if nucleotide in bases.keys():
            continue
        else:
            return ''
    return ''.join(bases[nucleotide] for nucleotide in dna)

def encode(code):
    """encode an AZ mixed case string)"""
    #remove whitespace + make all upper
    '' == ''
    # if element = letter .append and continue

    #elif element = number, element +1 multiplied by elephant
