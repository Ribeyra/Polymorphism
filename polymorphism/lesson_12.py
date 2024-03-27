class Calculator:
    def __init__(self, acc=0):
        self.acc = acc

    def sum(self, num):
        self.acc += num
        return self.__class__(self.acc)

    def sub(self, num):
        self.acc -= num
        return self.__class__(self.acc)

    def mul(self, num):
        self.acc *= num
        return self.__class__(self.acc)

    def result(self):
        return self.acc


class CalcLogger:
    def __init__(self, calculator):
        self.calculator = calculator

    def sum(self, num):
        num1 = self.calculator.result()
        res = self.calculator.sum(num).result()
        print(f"Первое число: {num1} Второе число: {num} Сумма: {res}")
        return self.__class__(self.calculator)

    def sub(self, num):
        num1 = self.calculator.result()
        res = self.calculator.sub(num).result()
        print(f"Первое число: {num1} Второе число: {num} Разность: {res}")
        return self.__class__(self.calculator)

    def mul(self, num):
        num1 = self.calculator.result()
        res = self.calculator.mul(num).result()
        print(f"Первое число: {num1} Второе число: {num} Результат: {res}")
        return self.__class__(self.calculator)

    def result(self):
        return self.calculator.acc


calc = Calculator()
# класс Calculator использует fluent-interface
calc.sum(3).sub(4).mul(1).result()  # -1

calc = Calculator()
calc = CalcLogger(calc)
calc.sum(3).sub(4).mul(1).result()  # -1
# => Первое число: 0 Второе число: 3 Сумма: 3
# => Первое число: 3 Второе число: 4 Разность: -1
# => Первое число: -1 Второе число: 1 Результат: -1
