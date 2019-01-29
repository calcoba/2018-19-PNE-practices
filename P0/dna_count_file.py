file = open("DNA_chain")
sequence = file.read().replace("\n", "")
print("Total lenght:", len(sequence))
bases = "A", "C", "T", "G"
for base in bases:
    count = sequence.count(base)
    print(base, ":", count)