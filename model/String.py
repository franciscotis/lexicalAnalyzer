from model.Token import Token
import re

class String(Token):
    def __init__(self, value):
        Token.__init__(self, value)
        self.error = True
        self.unknown_symbol = False
    
    def setError(self):
        self.error = self.unknown_symbol

    def isEndOfLine(self ,currentChar): 
        if self.isBreakLine(currentChar) and self.value.count('"')==1:  
            self.error = True
            return True
        return False

    def isValid(self, currentChar):
        if self.isSymbol(currentChar) or currentChar==' ':
            return True
       

    def isEscapedDelimeter(self, term):
        return (term=='\\"')

    def returnValue(self, current_line):
        self.type = 'CAD' if not self.error else 'caMF'
        self.current_line = current_line
        return self.getToken()