class Matrix:
    def __init__(self, data):
        self.data = []
        self.shape = (0, 0)
        if not isinstance(data, list):
            if not isinstance(data, tuple):
                print("Matrix takes list or tuple")
            elif len(data) > 2:
                print("We can't accept a tuple of more than 2 items")
            else:
                i = 0
                number = 0
                while i < data[0]:
                    sublist = []
                    j = 0
                    while j < data[1]:
                        sublist.append(float(number))
                        j += 1
                        number += 1
                    self.data.append(sublist)
                    i += 1
                self.shape = (data[0], data[1])
        else:
            lens = len(data[0])
            for item in data:
                if not isinstance(item, list):
                    print("tha Data should be a list of lists")
                    return
                elif len(item) != lens:
                    print("all sublists should be with the same dimensions")
                    return
            for sublist in data:
                new_sublist = []
                for item in sublist:
                    new_sublist.append(float(item))
                self.data.append(new_sublist)
            self.shape = (len(self.data), len(self.data[0]))

    def __add__(self, matrixb):
        if not isinstance(matrixb, Matrix) or self.shape != matrixb.shape:
            print("You can only add matrix to other with same dimension")
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] + matrixb.data[i][j])
                new_matrix.append(sublist)
            return (repr(Matrix(new_matrix)))

    def __radd__(self, vector):
        if not isinstance(vector, (list, tuple)) or len(vector) != self.shape[1]:
            print("You Should enter a Vector with same dimensions")
            return (repr(Matrix((0, 0))))
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] + vector[j])
                new_matrix.append(sublist)
            return (repr((Matrix(new_matrix))))

    def __sub__(self, matrixb):
        if not isinstance(matrixb, Matrix) or self.shape != matrixb.shape:
            print("You can only sub a matrix to other with same dimension")
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] - matrixb.data[i][j])
                new_matrix.append(sublist)
            return (repr(Matrix(new_matrix)))

    def __rsub__(self, vector):
        if isinstance(vector, (list, tuple)) == False or len(vector) != self.shape[1]:
            print("You Should enter a Vector with same dimensions")
            return (repr(Matrix((0, 0))))
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] - vector[j])
                new_matrix.append(sublist)
            return (repr((Matrix(new_matrix))))

    #---------------------------------------------------------------------------------------------#
    def __mul__(self, matrixb):
        if isinstance(matrixb, Matrix) == False or self.shape != matrixb.shape:
            print("You can only a matrix to other with same dimension")
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] * matrixb.data[i][j])
                new_matrix.append(sublist)
            return (repr(Matrix(new_matrix)))

    def __rmul__(self, vector):
        if isinstance(vector, (list, tuple)) == False or len(vector) != self.shape[1]:
            print("You Should enter a Vector with same dimensions")
            return (repr(Matrix((0, 0))))
        else:
            new_matrix = []
            for i in range(self.shape[0]):
                sublist = []
                for j in range(self.shape[1]):
                    sublist.append(self.data[i][j] * vector[j])
                new_matrix.append(sublist)
            return (repr((Matrix(new_matrix))))
    
    #---------------------------------------------------------------------------------------------#

    def __truediv__(self, nbr):
        if isinstance(nbr, (float, int)) == False:
            print("You can only divide by a number")
        else:
            if nbr == 0:
                print("Not that smart You can't devide by zero")
                return (None)
            else:
                new_matrix = []
                for sublist in self.data:
                    new_sub = []
                    for item in sublist:
                        new_sub.append(item / nbr)
                    new_matrix.append(new_sub)
                return (repr(Matrix(new_matrix)))

    def __rtruediv__(self, nbr):
        if isinstance(nbr, (float, int)) == False:
            print("The Matrix can only be devide by a number")
            exit()
        else:
            try:
                new_matrix = []
                for sublist in self.data:
                    new_sub = []
                    for item in sublist:
                        new_sub.append(nbr / item)
                    new_matrix.append(new_sub)
                return (repr(Matrix(new_matrix)))
            except ZeroDivisionError:
                print ("The Matrix Contains a zero a can't finish this operation")
                exit()

    #---------------------------------------------------------------------------------------------#
    def __str__(self):
        word = "(<Matrix>: ["
        i = 0
        while i < self.shape[0]:
            word += "["
            j = 0
            while j < self.shape[1]:
                word += str(self.data[i][j])
                j += 1
                if j < self.shape[1]:
                    word += ", "
            word += "]"
            i += 1
        word += "]"
        return (word)

    def __repr__(self):
        word = "(<Matrix>: {})".format(self.data)
        return (word)
