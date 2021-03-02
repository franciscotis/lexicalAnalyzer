import re 
from FileManagement import FileManagement
from Token import Token
class Lexical:
    def __init__(self,filename):
        self.types = ("RES","ID","NUM","OPAR","OPRE","OPLO","DELCOM","DEL","CADCAR")
        self.reserved_words = ("var","const","typedef","struct","extends","procedure","function","start","return","if","else","then","while","read","print","int","real","boolean","string","true","false","global","local")
        self.file = FileManagement(filename)
        self.content = list(self.file.read_file())
        self.current_state = 0
        self.array_pointer = 0
        self.line = 1
        self.real_number = False

    def nextToken(self):
        if(self.array_pointer <= len(self.content)):
            term = ''
            while(True):
                currentChar = self.getNextChar()
                if(currentChar is not None):
                    if self.current_state==0:
                        term=''
                        if(self.isChar(currentChar)):
                            self.current_state = 1
                            term+=currentChar
                        elif(self.isNumber(currentChar)):
                            self.current_state = 2
                            term+=currentChar
                        elif(self.isArithmeticOperator(currentChar)):
                            self.current_state = 3
                            term+=currentChar
                        elif(self.isRelationalOperator(currentChar)):
                            self.current_state = 4
                            term+=currentChar
                        elif(self.isLogicOperator(currentChar)):
                            self.current_state = 5
                            term+=currentChar
                    elif(self.current_state ==1):
                        if(self.isChar(currentChar)):
                            term+=currentChar
                            self.current_state = 1
                        elif(self.isSpace(currentChar or not self.isChar(currentChar))):
                            self.current_state = 0
                            self.back()
                            if self.isReserved(term):
                                token = Token(self.types[0],term,self.line)
                                return token.getToken()
                            else:
                                token = Token(self.types[1],term,self.line)
                                return token.getToken()
                    elif(self.current_state==2):
                        if(self.isRealNumber(currentChar) and self.real_number):
                            self.real_number = False
                            self.current_state = 0
                            self.back()
                            token = Token(self.types[2],term,self.line)
                            return token.getToken()
                        elif(self.isRealNumber(currentChar) and not self.real_number):
                            self.real_number = True
                            term+=currentChar
                        elif(self.isNumber(currentChar)):
                            term+=currentChar
                        else:
                            self.current_state = 0
                            self.back()
                            token = Token(self.types[2],term,self.line)
                            return token.getToken()
                    elif self.current_state ==3:
                        if(self.compareArithmeticValid(currentChar,term)):
                            term+=currentChar
                        else:
                            self.current_state =0
                            self.back()
                            token = Token(self.types[3],term,self.line)
                            return token.getToken()
                    elif self.current_state ==4:
                        if(self.compareRelationalValid(currentChar,term)):
                            term+=currentChar
                        else:
                            self.current_state = 0
                            self.back()
                            token = Token(self.types[4],term,self.line)
                            return token.getToken()
                    elif self.current_state==5:
                        if(self.compareOperatorValid(currentChar,term)):
                            term+=currentChar
                        else:
                            self.current_state = 0
                            self.back()
                            token = Token(self.types[5],term,self.line)
                            return token.getToken()
                    
                    




    def getNextChar(self):
        if self.array_pointer < len(self.content):
            next_char = self.content[self.array_pointer]
            self.array_pointer+=1
            return next_char
        return None

    def isChar(self,char):
        p = re.compile('([a-z]|[A-Z])(([a-z]|[A-Z])|[0-9]|_)*')
        return True if p.match(char) is not None else False

    def isReserved(self, term):
        return True if term in self.reserved_words else False

    def isSpace(self, term):
        if term == '\n' or term == '\r':
            self.line+=1
        return True if term == '\n' or term == ' ' or term == '\r' or term == '\t' else False
        
    def isNumber(self, char):
        p = re.compile('([0-9])')
        return True if p.match(char) is not None else False

    def isRealNumber(self,char):
        p = re.compile('([.])')
        return True if p.match(char) is not None else False

    def isArithmeticOperator(self,char):
        p = re.compile('([+]|-|[*]|[\/])')
        return True if p.match(char) is not None else False

    def compareArithmeticValid(self,char,term):
        if term+char== '++' or term+char == '--':
            return True
        else:
            return False

    def isRelationalOperator(self,char):
        p = re.compile('(=|!|>|<)')
        return True if p.match(char) is not None else False

    def compareRelationalValid(self, char, term):
        return True if term+char == '==' or term+char =='!=' or term+char =='>=' or term+char =='<=' else False

    def isLogicOperator(self, char):
        p = re.compile('(&|[|]|!)')
        return True if p.match(char) is not None else False

    def compareOperatorValid(self,char,term):
        if term+char=='&&' or term+char=='||':
            return True
        else:
            return False

        
        


    def back(self):
        self.array_pointer-=1





    