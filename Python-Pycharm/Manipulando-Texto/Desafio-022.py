# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa:
print('-' * 50)
nome = str(input('Digite seu nome completo: ')).strip() # .strip remove o espaço.
print('-' * 50)
print('Analisando seu nome...')
print('-' * 50)

# O nome com todos as letras maiúsculas.
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

# O nome com todas minúsculas.
print('Seu nome em minúsculo é {}'.format(nome.lower()))

# Quantas letras ao todo (sem considerar espaços).
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # -nome.count(' '), tira o espaço entre o nome e sobrenome.

#Quantas letras tem o primeiro nome.
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print('-' * 50)