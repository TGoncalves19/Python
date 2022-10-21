# Desafio 020 - O mesmo professor do desafio 019, quer sortear a ordem de apresentação de trabalhos
# dos alunos e mostre a ordem sorteada.

import random
a1 = str(input('Primeiro aluno (a): '))
a2 = str(input('Segundo Aluno (a): '))
a3 = str(input('Terceiro Aluno (a): '))
a4 = str(input('Quarto Aluno (a): '))
aluno = [a1, a2, a3, a4]
random.shuffle(aluno)
print('A ordem para apresentação é: {}'.format(aluno))