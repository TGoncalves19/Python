# importando a biblioteaca MATCH.

import math #1 - importa a biblioteca inteira.
from math import sqrt, ceil, floor # 2 - importa um comando específico.

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.0f}.'.format(num, raiz))
print('Comando ceil() {}.'.format(ceil(raiz))) # Arrendonda para cima.
print('Comando math.floor() {}.'.format(math.floor(raiz))) # Arredonda para baixo.

# Biblioteca RANDOM
import random
num = random.random()
num_1 = random.randint(1, 10) # números aleatórios
print(num)
print(num_1)



