from Bases import count_bases

s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")

sequences = s1, s2
sn = 0
for s in sequences:
    bases_dic = count_bases(s)
    sn += 1

    # Calculate the total sequence length
    tl = len(s)
    print("Sequence {} is {} bases in length".format(sn, tl))
    for key, value in bases_dic.items():
        if tl > 0:
            perc = round(100.0 * value / tl, 1)
        else:
            perc = 0
        print("Base {}".format(key))
        print("  Counter: {}".format(value))
        print("  Percentage: {}".format(perc))
    print()
