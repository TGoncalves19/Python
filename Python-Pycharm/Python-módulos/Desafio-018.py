# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.
import math
angulo = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print('O ângulo é {}°, o SENO {:.2f}, o COSSENO {:.2f} e a TANGENTE {:.2f}.'.format(int(angulo), sen, cos, tg))

from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))
print('O ângulo é {}°, o SENO {:.2f}, o COSSENO {:.2f} e a TANGENTE {:.2f}.'.format(int(angulo), sen, cos, tg))