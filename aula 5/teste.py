class Pessoa:#classe
                #o self é o que referencia o objeto chamando o método.
    def __init__(self, nome, idade):#o init é o construtor, serve para inicializar os atributos do objeto
        #atributos:
        self.nome = nome
        self.idade = idade

    #método
    def gritar(self):
        print('AAAAA!')

#objeto
leandro = Pessoa('João', 18)

print(leandro.nome)
leandro.gritar()