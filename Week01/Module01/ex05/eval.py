class Evaluator:
    def zip_evaluate(self, words, coefs):
        if len(words) != len(coefs) or isinstance(words, list) == False or isinstance(coefs, list) == False:
            return (-1)
        else:
            new_list = list(zip(words, coefs))
            result = 0
            for item in new_list:
                result += len(str(item[0])) * float(item[1])
            return (result)

    def enumerate_evaluate(self, words, coefs):
        if len(words) != len(coefs) or isinstance(words, list) == False or isinstance(coefs, list) == False:
            return (-1)
        else:
            result = 0
            for count, (word, coef) in enumerate(zip(words, coefs)):
                result += len(str(word)) * float(coef)
            return (result)
