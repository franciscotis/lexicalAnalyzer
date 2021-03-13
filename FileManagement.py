class FileManagement:
    def __init__(self, filename):
        self.filename = filename
        self.filecontent = ''

    def read_file(self):
        with open(self.filename, 'r', encoding='utf-8') as arquivo:
            for line in arquivo:
                if line=='\n':
                    self.filecontent+='\n'
                else:
                    self.filecontent+=line
        return self.filecontent

        
    
        