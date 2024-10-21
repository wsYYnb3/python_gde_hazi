class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadasa(self, jarat):
        self.jaratok.append(jarat)

    def jaratok_listazasa(self):
        for jarat in self.jaratok:
            print(jarat)
