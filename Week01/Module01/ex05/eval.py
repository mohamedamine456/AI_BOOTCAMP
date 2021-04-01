class Evaluator:
    def zip_evaluate(self, words, coefs):
        if len(words) != len(coefs) or isinstance(words, list) == False or isinstance(coefs, list) == False:
            return (-1)
        else:
            lengths = []
            for word in words:
                lengths.append(len(word))
            new_list = list(zip(lengths, coefs))
            return (new_list)

    def enumerate_evaluate(self, words, coefs):
        pass
