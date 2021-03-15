import re 
from FileManagement import FileManagement
from model.Token import Token
from model.Identifier import Identifier
from model.Digit import Digit
from model.Arithmetic import Arithmetic
from model.Relational import Relational
from model.Logic import Logic
from model.Delimiter import Delimiter
from model.Comment import Comment

class Lexical:
    def __init__(self,filename):
        print(filename)
        self.file = FileManagement(filename)
        self.content = list(self.file.read_file())
        self.content.append(' ')
        self.current_state = 0
        self.array_pointer = 0
        self.real_number = False
        self.current_token = None
        self.current_line = 1
        self.token_list = []
        self.can_read = True


    def run(self):
        result = self.nextToken()
        while(result!= None):
            result = self.nextToken()
        self.file.print_file(self.token_list)

    def nextToken(self):
        if(self.array_pointer <= len(self.content)):
            while(True):
                currentChar = self.getNextChar()
                if(currentChar is not None):
                    if self.current_state==0:
                        self.current_token = None
                        if(Token.isChar(currentChar)):
                            self.current_state = 1
                            self.current_token = Identifier(currentChar)
                        elif(Token.isNumber(currentChar)):
                            self.current_state = 2
                            self.current_token = Digit(currentChar)
                        elif(Token.isArithmeticOperator(currentChar)):
                            nextChar = self.content[self.array_pointer]
                            if(Token.isCommentDelimiter(currentChar, nextChar)):
                                self.current_state = 7
                                self.current_token = Comment(currentChar+nextChar)
                            else:
                                self.current_state = 3
                                self.current_token = Arithmetic(currentChar)
                        elif(Token.isRelationalOperator(currentChar)):
                            self.current_state = 4
                            self.current_token = Relational(currentChar)
                        elif(Token.isLogicOperator(currentChar)):
                            self.current_state = 5
                            self.current_token = Logic(currentChar)
                        elif(Token.isDelimiter(currentChar)):
                            self.current_state = 6
                            self.current_token = Delimiter(currentChar)
                        elif(currentChar == '\n'):
                            self.current_line+=1
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
                                self.token_list.append(self.current_token.returnValue(self.current_line))
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
                                self.token_list.append(self.current_token.returnValue(self.current_line))
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
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                self.token_list.append(self.current_token.returnValue(self.current_line))
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
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                self.token_list.append(self.current_token.returnValue(self.current_line))
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
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                    elif self.current_state==6:
                        if(self.current_token.isValid(currentChar) and not Token.isSpace(currentChar)):
                            self.current_token.setValue(currentChar)
                            self.current_state = 6
                        else:
                            if(not self.current_token.validNeighbors(currentChar) and not Token.isSpace(currentChar)):
                                self.current_token.setValue(currentChar)
                                self.current_state = 6
                            elif Token.isSpace(currentChar):
                                self.current_state = 0
                                self.back()
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                            else:
                                self.current_state = 0
                                self.back()
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                    elif self.current_state==7:
                        if(self.current_token.isInlineComment()):
                            if(self.current_token.isEndInlineComment(currentChar)):
                                self.current_state = 0
                                self.back()
                            else:
                                self.current_state = 7
                        elif(self.current_token.isBlockComment() and not Token.isSpace(currentChar)):
                            nextChar = self.getNextChar()
                            if(nextChar==None):
                                self.current_state = 0
                                self.token_list.append(self.current_token.returnValue(self.current_line))
                                return self.current_token.returnValue(self.current_line)
                            elif(self.current_token.isEndBlockComment(currentChar+nextChar)):
                                self.current_state = 0
                            else: self.current_state = 7
                else:
                    if(self.current_token):
                        token = self.current_token.returnValue(self.current_line)
                        self.current_token = None
                        self.token_list.append(token(self.current_line))
                        return token
                    return
        else:
            return None
                    
                   
    def getNextChar(self):
        if self.array_pointer < len(self.content):
            next_char = self.content[self.array_pointer]
            self.array_pointer+=1
            return next_char
        return None

    def back(self):
        self.array_pointer-=1





    