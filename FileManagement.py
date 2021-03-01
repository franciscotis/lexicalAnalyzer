class FileManagement:
    def __init__(self, filename):
        self.filename = filename
        self.filecontent = ''

    def read_file(self):
        with open(self.filename, 'r') as arquivo:
            for line in arquivo:
                self.filecontent+=line
        return self.filecontent

        
    
        