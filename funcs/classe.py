class Calculadora:

    def soma(a, b):
        return a + b

    # sub = lambda a, b: a - b
    def sub(a, b): return a - b

    def mult(a, b): return a * b

    def div(a, b): return a / b


if __name__ == '__main__':
    calc = Calculadora
    print(calc.soma(5, 8))
    print(calc.sub(10, 7))
    print(calc.mult(4, 6))
    print(calc.div(16, 8))
