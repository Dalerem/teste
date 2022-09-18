"""
    Author: Dalerem Teixeira
    E-Mail: dalerem2022@gmail.com
    Rede social: https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/
"""

__author__ = "Dalerem Teixeira"
__email__ = "dalerem2022@gmail.com"
__redesocial__ = "https://www.linkedin.com/in/d%C3%A1lerem-teixeira-949a48236/"

class Calc:
    """
        Classe para fazer calculo
    """
    def __init__(self, a, b):
        """
            Construtor para os calculos

        :param a: valor a
        :param b: valor b
        """
        self.a = a
        self.b = b

    def soma(self):
        """
            Função soma

        :return: soma dos valores a e b
        """
        return self.a + self.b

    def sub(self):
        """
            Função subtração

        :return: subtração dos valores a e b
        """
        return self.a - self.b

    def mult(self):
        """
            Função multiplicação

        :return: multiplicação dos valores a e b
        """
        return self.a * self.b

    def div(self):
        """
            Função divisão

        :return: divisão dos valores a e b
        """
        return self.a / self.b

    def mostra(self):
        """
            Função que motra as operações

        :return: operações soma, subtração, multiplicação e divisão
        """
        print("Soma:", resp.soma())
        print("Subtracao:", resp.sub())
        print("Multiplicacao:", resp.mult())
        print("Divisao:", resp.div())

x = float(input("Digite um numero: "))
y = float(input("Digite outro numero: "))

resp = Calc(x, y)
resp.mostra()