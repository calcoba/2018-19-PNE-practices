class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self, base):
        return len(self.strbases)

    def complement(self, base):
        dict_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}
        translation = self.strbases.maketrans(dict_bases)
        strbases_comp = self.strbases.translate(translation)
        return strbases_comp

    def reverse(self, base):
        strbases_rev = self.strbases[::-1]
        return strbases_rev

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

    def call_function(self, name, base=""):
        fn = getattr(self, name)
        value = fn(base)
        return value
