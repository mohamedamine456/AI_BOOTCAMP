#import sys
#sys.path.append('../ex02')
#from vector import Vector

class Matrix:
    def __init__(self, data):
        self.data = []
        self.shape = (0, 0)
        if isinstance(data, list) == False:
            if isinstance(data, tuple) == False:
                print("Matrix takes list or tuple")
                return
            elif len(data) > 2:
                print("We can't accept a tuple of more than 2 items")
                return
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
                if isinstance(item, list) == False :
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

    #---------------------------------------------------------------------------------------------#
    def __add__(self, matrixb):
        if isinstance(matrixb, Matrix) == False or self.shape != matrixb.shape:
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
        if isinstance(vector, (list, tuple)) == False or len(vector) != self.shape[1]:
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

    #---------------------------------------------------------------------------------------------#
    def __sub__(self, matrixb):
        if isinstance(matrixb, Matrix) == False or self.shape != matrixb.shape:
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
    
    def __repr__(self):
        word = "(<Matrix>: {})".format(self.data)
        return (word)
