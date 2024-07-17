class Calculator:
    @staticmethod
    def summa(a, b):
        return a + b

num = Calculator()
result = num.summa(15, 19)
print(result)

class Calculators(Calculator):
    def string_num(self, a, b):
        res = super().summa(str(a), str(b))
        return res

konk = Calculators()

k = konk.string_num(15, 19)
print(k)





