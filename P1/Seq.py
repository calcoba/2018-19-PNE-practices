class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):
        one = "ATGC"
        two = "TACG"
        translation = self.strbases.maketrans(one, two)
        strbases_comp = self.strbases.translate(translation)
        return Seq(strbases_comp)

    def reverse(self):
        strbases_rev = self.strbases[::-1]
        return Seq(strbases_rev)

    def count(self, base):
        n_base = self.strbases.count(base)
        return n_base

    def perc(self, base):
        tl = len(self.strbases)
        if tl > 0:
            nbase = self.count(base)
            perc = round(100.0 * nbase / tl, 1)
        else:
            perc = 0
        return perc


s1 = Seq("ATTCGATCC")
s2 = Seq("AAAGG")
s3 = s1.reverse()
s4 = s2.complement()
seq = s1, s2, s3, s4

str1 = s1.strbases
str2 = s2.strbases
str3 = s3.strbases
str4 = s4.strbases

for i in range(len(seq)):
    length = seq[i].len()
    for letter in ("A", "C", "T", "G"):
        counter = seq[i].count(letter)
        print("{} : {}".format(letter, counter))

    print("Sequence {} has a lenght of {}".format(i+1, length))
print(str1, str2, str3, str4)
