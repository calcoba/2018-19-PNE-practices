DNA_chain = input("Introduce the sequence::")
print("Total lenght:", len(DNA_chain))
bases = "A", "C", "T", "G"
for base in bases:
    count = DNA_chain.count(base)
    print(base, ":", count)