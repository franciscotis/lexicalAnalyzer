from Lexical import Lexical
import glob
class ProgramStart:
    def __init__(self):
        self.txtfiles = []
        for file in glob.glob("entrada*.txt"):
            self.txtfiles.append(file)
        print(self.txtfiles)

    def analyze(self):
        for file in self.txtfiles:
            lexical = Lexical(file)
            lexical.run()

