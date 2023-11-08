#1 crie uma classe Retangulo que tenha os atributos base e altura e os métodos area() e perimetro(). Crie um objeto e teste os métodos

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        print(self.base * self.altura)

    def perimetro(self):
        print(2 * (self.base + self.altura))

testeArea = Retangulo(12, 5)
testeArea.area()

testePerimetro = Retangulo(11, 7)
testePerimetro.perimetro()