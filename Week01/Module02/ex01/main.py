class Objectc(object):
    def __init__(self):
        pass

    def doom_printer(obj):
        if obj is None:
            print("ERROR")
            print("END")
            return
        for attr in dir(obj):
            if attr[0] != '-':
                value = getattr(obj, attr)
                print("{}: {}".format(attr, value))
        print("END")

def what_are_the_vars(**args):    
