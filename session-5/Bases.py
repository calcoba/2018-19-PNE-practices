def count_bases(seq):
    """Counting the number of each base in the sequence"""

    n_bases = {}
    b_set = set(seq)
    for i in b_set:
        n_bases.update({i: seq.count(i)})

    return n_bases

