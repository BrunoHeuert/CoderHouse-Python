#classe Retangulo
class Retangulo:
    def __init__(self, base, altura):
        #atributos base e altura
        self.base = base
        self.altura = altura

    #método area
    def area(self):
        print(self.base * self.altura)
    #método perimetro
    def perimetro(self):
        print(2 * (self.base + self.altura))

#objeto testeArea recebendo a classe
testeArea = Retangulo(12, 5)
#escrevendo o objeto
testeArea.area()

#objeto testePerimetro recebendo a classe
testePerimetro = Retangulo(11, 7)
#escrevendo o objeto
testePerimetro.perimetro()
