# Desafio 016 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127 e R: O número 6.127 tem a parte inteira 6.

'''from math import floor
num_1 = float(input('Digite um número: '))
num_2 = floor(num_1)
print('O número {}, tem a porção inteira de {}.'.format(num_1, num_2))

# Importando o TRUNC
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua prção inteira é {}.'.format(num, trunc(num)))'''

# Desafio resolvido sem importa comandos.
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))