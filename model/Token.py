import re 
import abc

class Token:
    def __init__(self, value=''):
        self.type = ''
        self.value = value
        self.current_line = ''
        self.reserved_words = ''
        self.supported_neighbors = ''
        self.error = False
    
    def getToken(self):
        return "{} {} {}".format(self.current_line,self.type, self.value)

    def setType(self,type):
        self.type = type

    def setValue(self,value):
        self.value+= value

    def validNeighbors(self,currentChar):
        p = re.compile(self.supported_neighbors)
        return True if p.match(currentChar) is not None else False
    
    @abc.abstractmethod
    def isValid(self,currentChar):
        return

    @abc.abstractclassmethod
    def continueInvalidToken(self,currentChar):
        return

    @abc.abstractclassmethod
    def returnValue(self,current_line):
        return 

    @abc.abstractclassmethod
    def returnError(self,current_line):
        return
    
    @classmethod
    def isNumber(self, char):
        p = re.compile('([0-9])')
        return True if p.match(char) is not None else False

    @classmethod
    def isRealNumber(self,char):
        p = re.compile('([.])')
        return True if p.match(char) is not None else False

    @classmethod
    def isChar(self,char):
        p = re.compile('([a-z]|[A-Z])')
        return True if p.match(char) is not None else False

    @classmethod
    def is_underscore(self,char):
        p = re.compile('([_])')
        return True if p.match(char) is not None else False

    @classmethod
    def isBreakLine(self,term):
        if term == '\n' or term == '\r':
            return True

    @classmethod
    def isSpace(self, term):
        return True if term == '\n' or term == ' ' or term == '\r' or term == '\t' else False
        
    @classmethod
    def isArithmeticOperator(self,char):
        p = re.compile('([+]|-|[*]|[\/])')
        return True if p.match(char) is not None else False

    @classmethod
    def isCommentDelimiter(self,char):
        p = re.compile('([\/])')
        return True if p.match(char) is not None else False

    @classmethod
    def isDelimiter(self,char):
        p = re.compile('([;]|[,]|[(]|[)]|[{]|[}]|[\[]|[\]]|[.]|[+]|[-]|[*]|[/])')
        return True if p.match(char) is not None else False

    def compareArithmeticValid(self,char,term):
        if term+char== '++' or term+char == '--':
            return True
        else:
            return False

    @classmethod
    def isRelationalOperator(self,char):
        p = re.compile('(=|!|>|<)')
        return True if p.match(char) is not None else False

    def compareRelationalValid(self, char, term):
        return True if term+char == '==' or term+char =='!=' or term+char =='>=' or term+char =='<=' else False
    
    @classmethod
    def isLogicOperator(self, char):
        p = re.compile('(&|[|]|!)')
        return True if p.match(char) is not None else False

    def compareOperatorValid(self,char,term):
        if term+char=='&&' or term+char=='||':
            return True
        else:
            return False
