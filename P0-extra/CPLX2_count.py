bases = "A", "C", "T", "G"
count_a = 0
count_c = 0
count_t = 0
count_g = 0
counts = [count_a, count_c, count_t, count_g]

with open("CPLX2.txt") as file:
    dna_chain = file.read()
    dna_chain = dna_chain.split("\n")
    dna_chain_final = list()
    for line in dna_chain:
        if not line.startswith(">"):
           for i in range(len(bases)):
                counts[i] += line.count(bases[i])

    for element in range(len(bases)):
        print("Letter", bases[element], "is repeated", counts[element], "times")


