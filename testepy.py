"""
    Author: Dalerem Teixeira
    E-Mail: dalerem2022@gmail.com
    Rede social: https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/
"""

__author__ = "Dalerem Teixeira"
__email__ = "dalerem2022@gmail.com"
__redesocial__ = "https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/"

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