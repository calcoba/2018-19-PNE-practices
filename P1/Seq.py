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
