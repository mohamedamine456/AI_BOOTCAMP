class TinyStatistician:
    def __init__(self):
        pass
    def mean(self, x) -> float:
        size = len(x)
        if size == 0:
            return (None)
        else:
            result = 0.0
            for item in x:
                result += float(item)
            return (result / float(size))

    def median(self, x):
        x.sort()
        size = len(x)
        if size == 0
            return (None)
        elif size % 2 == 1:
            med = size + 1  / 2
            return (x[med])
        
        else:
            med = size % 2
            result = (x[med] + x[med + 1]) / 2
            return (result)

    def quartiles(self, x, percentile):
        pass
