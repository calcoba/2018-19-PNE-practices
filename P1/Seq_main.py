from Seq import Seq

s1 = Seq("ATTCGATCC")
s2 = Seq("AAAGG")
s3 = s1.reverse()
s4 = s2.complement()
seq = s1, s2, s3, s4
bases = ("A", "C", "T", "G")
str1 = s1.strbases
str2 = s2.strbases
str3 = s3.strbases
str4 = s4.strbases
print(s1.perc("A"))
for i in range(len(seq)):
    print("Sequence {}: {}".format(i+1, seq[i].strbases))
    length = seq[i].len()
    bases_count = {}
    bases_percent = {}
    for letter in bases:
        bases_count.update({letter: seq[i].count(letter)})
        bases_percent.update({letter: str(seq[i].perc(letter))+"%"})
    bases_count = str(bases_count).replace("{", "").replace("}", "").replace("'", "")
    print("    Bases count:", bases_count)
    bases_percent = str(bases_percent).replace("{", "").replace("}", "").replace("'", "")
    print("    Bases percentage:", bases_percent)


    print("Sequence {} has a lenght of {}".format(i+1, length))

