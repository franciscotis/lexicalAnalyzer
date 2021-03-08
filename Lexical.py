import re 
from FileManagement import FileManagement
from model.Token import Token
from model.Identifier import Identifier
from model.Digit import Digit
from model.Arithmetic import Arithmetic
from model.Relational import Relational
from model.Logic import Logic

class Lexical:
    def __init__(self,filename):
        self.types = ("RES","ID","NUM","OPAR","OPRE","OPLO","DELCOM","DEL","CADCAR")
        self.file = FileManagement(filename)
        self.content = list(self.file.read_file())
        self.current_state = 0
        self.array_pointer = 0
        self.real_number = False
        self.current_token = None
        self.current_line = 1

    def nextToken(self):
        if(self.array_pointer <= len(self.content)):
            while(True):
                currentChar = self.getNextChar()
                if(currentChar is not None):
                    if self.current_state==0:
                        if(Token.isChar(currentChar)):
                            self.current_state = 1
                            self.current_token = Identifier(currentChar)
                        elif(Token.isNumber(currentChar)):
                            self.current_state = 2
                            self.current_token = Digit(currentChar)
                        elif(Token.isArithmeticOperator(currentChar)):
                            self.current_state = 3
                            self.current_token = Arithmetic(currentChar)
                        elif(Token.isRelationalOperator(currentChar)):
                            self.current_state = 4
                            self.current_token = Relational(currentChar)
                        elif(Token.isLogicOperator(currentChar)):
                            self.current_state = 5
                            self.current_token = Logic(currentChar)
                    elif(self.current_state ==1):
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 1
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 1
                            else:
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                    elif(self.current_state==2):
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 2
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 2
                            else:
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                    elif self.current_state ==3:
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 3
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 3
                            elif Token.isSpace(currentChar):
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                    elif self.current_state ==4:
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 3
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 3
                            elif Token.isSpace(currentChar):
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                    elif self.current_state==5:
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 5
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 5
                            elif Token.isSpace(currentChar):
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                return self.current_token.returnValue(self.current_line)
                else:
                    if(self.current_token):
                        token = self.current_token.returnValue(self.current_line)
                        self.current_token = None
                        return token

                    
    def getNextChar(self):
        if self.array_pointer < len(self.content):
            next_char = self.content[self.array_pointer]
            self.array_pointer+=1
            return next_char
        return None

    def back(self):
        self.array_pointer-=1





    