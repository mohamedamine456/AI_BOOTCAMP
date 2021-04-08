def what_are_the_vars(*argv, **kwargs):
    obj = ObjectC()
    index = 0
    if len(argv) == 0 and len(kwargs) == 0:
        return (obj)

    argv_set = set()
    for arg in argv:
        obj.__setattr__("var_" + str(index), arg)
        #setattr(obj, "var_" + str(index), arg)
        argv_set.add("var_" + str(index))
        index += 1
    
    for key, value in kwargs.items():
        if key in argv_set:
            return (None)
        obj.__setattr__(key, value)
    return (obj)


class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("END")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("END")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
