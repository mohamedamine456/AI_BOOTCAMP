import decimal

class Vector:
    def __init__(self, numbers):
        if isinstance(numbers, list) == False:
            if isinstance(numbers, int) == False:
                print("Vector takes list of numbers or number")
            else:
                self.values = []
                for i in range(0, numbers):
                    self.values.append(float(i))
                self.size = len(self.values)
        else:
            self.values = []
            for number in numbers:
                self.values.append(float(number))
            self.size = len(self.values)

    def __add__(self, vectorb):
        if isinstance(vectorb, Vector) == False or vectorb.size != self.size:
            print("the argument Should be a Vector with same dimension")
        else:
            new_vector = []
            for i in range(self.size):
                new_vector.append(self.values[i] + vectorb.values[i])
            return (repr(Vector(new_vector)))
    
    def __radd__(self, number):
        if isinstance(number, (float, int)) == False:
            print("Error: You can't add something to vector but float or int")
            exit()
        else:
            new_vector = []
            for nbr in self.values:
                new_vector.append(nbr + float(number))
            return (repr(Vector(new_vector)))

    def __sub__(self, vectorb):
        if isinstance(vectorb, Vector) == False or vectorb.size != self.size:
            print("the argument Should be a Vector with same dimension")
        else:
            new_vector = []
            for i in range(self.size):
                new_vector.append(self.values[i] - vectorb.values[i])
            return (repr(Vector(new_vector)))

    def __rsub__(self, number):
        if isinstance(number, (float, int)) == False:
            print("Error: You can't substract something from vector but float or int")
            exit()
        else:
            new_vector = []
            for nbr in self.values:
                new_vector.append(nbr - float(number))
            return (repr(Vector(new_vector)))

    def __mul__(self, vectorb):
        if isinstance(vectorb, Vector) == False or vectorb.size != self.size:
            print("the argument Should be a Vector with same dimension")
        else:
            new_vector = []
            for i in range(self.size):
                new_vector.append(self.values[i] * vectorb.values[i])
            return (repr(Vector(new_vector)))

    def __rmul__(self, number):
        if isinstance(number, (float, int)) == False:
            print("Error: You can't multiply something to vector but float or int")
            exit()
        else:
            new_vector = []
            for nbr in self.values:
                new_vector.append(nbr * float(number))
            return (repr(Vector(new_vector)))

    def __true_div__(self, number):
        if isinstance(number, (float, int)) == False:
            print("The Division applied with a float or int only")
            exit()
        else:
            try:
                new_vector = []
                for nbr in self.values:
                    new_vector.append(nbr / number)
                return (repr(Vector(new_vector)))
            except ZeroDivisionError:
                print("Trying to divide the vector by zero not that smart")
                exit()

    def __rtrue_div__(self, number):
        if isinstance(number, (float, int)) == False:
            print("The Division applied with a float or int only")
            exit()
        else:
            try:
                new_vector = []
                for nbr in self.values:
                    new_vector.append(number / nbr)
                return (repr(Vector(new_vector)))
            except ZeroDivisionError:
                print("The Vector contain a zero which cause division prob")
                exit()

    def __str__(self):
        word = ""
        i = 0
        while i < self.size:
            word += str(self.values[i])
            i += 1
            if i < self.size:
                word += ", "
        return (word)

    def __repr__(self):
        word = "(<Vector>: {})".format(self.values)
        return (word)
