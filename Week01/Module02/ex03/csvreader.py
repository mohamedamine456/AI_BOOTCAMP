import csv

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if filename == None:
            self = None
        else:
            self.filename = filename
            self.sep = sep
            self.header = header
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
            try:
                self.reader = csv.reader(self.filename, delimiter=self.sep)
            except FileNotFoundError:
                self = None

    def __enter__(self):
        """print("You Entered The CsvReader")
        if self.name == None or self.reader == None:
            print("File is Corrupted")
            return"""
        pass

    def __exit__():
        """print("End of class: Exit Block")
        return"""
        pass
    
    def get_data(self):
        if self.reader == None or self == None:
            print("File is Corrupted")
            return
        else:
            if self.header == False:
                next(self.reader)
                data = reader[self.skip_top:self.skip_bottom]
                return (data)
    
    def getheader(self):
        if self.reader == None or self == None:
            print("File is Corrupted")
            return
        else:
            if self.header = None:
                print("File header set to False")
                return
            else:
                return (self.reader[0])
