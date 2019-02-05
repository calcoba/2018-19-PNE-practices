def count_bases(seq):
    """Counting the number of each base in the sequence"""

    n_bases = {}
    bases = "A", "C", "T", "G"
    for i in bases:
        n_bases.update({i: seq.count(i)})

    return n_bases


s = input("Please enter the sequence: ")
bases_dic = count_bases(s)

# Calculate the total sequence length
tl = len(s)

for key, value in bases_dic.items():
    if tl > 0:
        perc = round(100.0 * value / tl, 1)
    else:
        perc = 0
    print("Base {}".format(key))
    print("  Counter: {}".format(value))
    print("  Percentage: {}".format(perc))