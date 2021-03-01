class Token:
    def __init__(self,type, value, current_line):
        self.type = type
        self.value = value
        self.current_line = current_line

    def getToken(self):
        return "{} - <{}, {}>".format(self.current_line,self.type, self.value)

    def setType(self,type):
        self.type = type

    def setValue(self,value):
        self.value = value
