def distance(seq1, seq2):
    mismatches = 0
    if len(seq1) == len(seq2):
        for pos in range(0, len(seq1)):
            if seq1[pos] != seq2[pos]:
                mismatches += 1
    else:
        raise ValueError
    return mismatches
