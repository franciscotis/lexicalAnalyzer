from model.Token import Token
import re 

class Logic(Token):
    def __init__(self, value):
        Token.__init__(self,value)
        self.supported_neighbors = '([a-z]|[A-Z]|[0-9]|[(])'
        self.supported_value = ['&&','||']

    def isValid(self,currentChar):
        if(self.isLogicOperator(currentChar) and (self.value+currentChar in self.supported_value)):
            return True
        elif(self.notValidRelational(currentChar) and not self.isSpace(currentChar)):
            self.error = True
        return False

    def notValidRelational(self,currentChar):
        if(not self.validNeighbors(currentChar)):
            return True
        return False

    def returnValue(self, current_line):
        self.type = 'LOG' if not self.error else 'opMF'
        self.current_line = current_line
        return self.getToken()