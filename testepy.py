class Calc:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def mostra(self):
        print("Soma:", resp.soma())
        print("Subtracao:", resp.sub())
        print("Multiplicacao:", resp.mult())
        print("Divisao:", resp.div())

resp = Calc(12, 4)
resp.mostra()