#crie uma variável chamada saldo e atribua o valor de 950,60. Em seguida, pergunte ao usuário quanto dinheiro ele deseja sacar e armazene a resposta em uma variável chamada saque. 
#Subtraia o valor de saque do valor de saldo e imprima a mensagem "Seu novo saldo é {saldo}"

saldo = 950.60
saque = float(input('Você atualmente possui {:.2f}, quanto você deseja sacar? '.format(saldo))) 
print('Seu novo saldo é R${:.2f}'.format(saldo - saque))


#faça um programa que crie uma lista com 5 frutas e permita que o usuário digite o nome de uma fruta. Se for uma fruta repetida deverá ser desconsiderada.

lista = ['abacaxi', 'abacate', 'banana', 'laranja', 'morango']
fruta = str(input('Digite a fruta que desejas adicionar! '))
lista.append(fruta)
listaAtualizada = set(lista)
print(listaAtualizada)


#faça um programa que peça ao usuário para digitar uma frase e substitua todas as vogais por asteriscos

frase = input('Digite uma frase! ')
novaFrase = frase.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')
print(novaFrase)