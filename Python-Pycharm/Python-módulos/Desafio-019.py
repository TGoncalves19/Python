# Desafio 019 - Um professor quer sortear um dos seus quatros para apagar o quadro. Faça um programa que
# ajude ele, lendo o nome deles e escrevendo o nome escolhido.

import random
a1 = str(input('Primeiro aluno (a): '))
a2 = str(input('Segundo Aluno (a): '))
a3 = str(input('Terceiro Aluno (a): '))
a4 = str(input('Quarto Aluno (a): '))
sorteio = [a1, a2, a3, a4]
escolhido = random.choice(sorteio)
print('O aluno (a) sorteado foi {}.'.format(escolhido))