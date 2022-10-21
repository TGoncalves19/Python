# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo, calcule e mostre o comprimento da hipotenusa.

# Cálculo matemático
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compriemnto do cateto adjacente: '))
hi = (co** 2 + ca ** 2) **(1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))

# Importando com MATH (math.hypot(), calcular a hipotenusa).
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compriemnto do cateto adjacente: '))
hi = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))