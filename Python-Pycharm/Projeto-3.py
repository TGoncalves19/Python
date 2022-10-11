# Tipos Primitivos e Saídas de Dados.

# print(type())
# print(type('Thiago')) #"String" (str)
# print(type(5)) #"Inteiro (int)
# print(type(5.1)) #"Float"
# print(type(True)) #"Booleana" (Verdadeiro ou Falso)

# Type classe "string" (texto)
# n1 = input('Digite um valor: ')
# print(type(n1))

# Type classe "inteiro" (1, 2, 3...)
# n1 = int(input('Digite um valor: '))
# print(type(n1))

# Type classe "float" (1.5, 2.7, 3.1...)
# n1 = float(input('Digite um valor: '))
# print(type(n1))

# Desafio 003 - Crie um programa que leia dois números e mostre a soma entre eles.
#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
#soma = n1 + n2
#print('A soma entre {} mais {} é igual: {}'.format(n1, n2, soma))

#Desafio 004 - Faça um programa que leia algo pelo teclado e mostre na tela o su tipo primitivo e todas as informações sobre ele
nome = input('Digite algo: ')
print('O tipo primitivo deste valor é: ', type(nome))
print('Só tem espaços? ', nome.isspace())
print('É um número? ', nome.isnumeric())
print('É alfabético?', nome.isalpha())
print('É alfanumérico? ', nome.isalnum())
print('Está em maiúsculas? ', nome.isupper())
print('Está em minúsculas? ', nome.islower())
print('Está capitalizado? ', nome.istitle())




