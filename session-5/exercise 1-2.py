from Bases import count_bases

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
