from model.Token import Token
import re

class String(Token):
    def __init__(self, value):
        Token.__init__(self, value)
        self.error = True
        self.unknown_symbol = False
    
    def setError(self):
        self.error = self.unknown_symbol

    def isValid(self, currentChar):
        return self.isSymbol(currentChar)

    def isEscapedDelimeter(self, term):
        return (term=='\\"')

    def returnValue(self, current_line):
        self.type = 'CAD' if not self.error else 'caMF'
        self.current_line = current_line
        return self.getToken()