# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.
import math
angulo = float(input('Digite o valor do ângulo: '))
sen = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
print('O ângulo é {}°, o seno {}, o cosseno {} e a tangente {}.'.format(angulo, sen, cos, tg))