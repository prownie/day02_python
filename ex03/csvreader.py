class CsvReader():

    def __init__(self, filename=None, sep=";", header=False, skip_top=0, skip_bottom=0):

        self.empty = 0
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self): #Called on the resulting value ans assign if to "as" when "with" is used ?
        try:
            self.file = open(self.filename, 'r')
        except (FileNotFoundError, OSError):
            print("File Not Found dans enter")
            self.empty = 1
        return(self)


    def __exit__(self, exception_type, exception_value, traceback): #used after exit
        pass


    def getheader(self):
        try:
            if self.header == True:
                self.header = self.file.readline()
                self.header = self.header[:len(self.header) - 1].split(";")
            elif self.header == False:
                self.header = None
            else:
                raise HeaderError("Wrong header format, needs to be True or False")
        except HeaderError:
            return(None)

    
    def skipline(self):
        pass


if __name__ == "__main__":
    with CsvReader("film.csv",";", True) as file:
        if file == None:
            print("File is corrupted")
        elif file.empty:
            print("File not found")
        else:
            header = file.getheader()
            data = file.getdata() 
