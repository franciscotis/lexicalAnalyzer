from model.Token import Token

class Delimiter(Token):
    def __init__(self,value):
        Token.__init__(self,value)
        self.supported_neighbors = '([a-z]|[A-Z]|[0-9]|[{]|[}]|["]|[;]|[_])'
        self.value = value

    def isValid(self, currentChar):
        if(not self.validNeighbors(currentChar) and not self.isSpace(currentChar)):
            self.error = True
        return False
    
    def returnValue(self, current_line):
        self.type = 'DEL' if not self.error else 'deMF'
        self.current_line = current_line
        return self.getToken()