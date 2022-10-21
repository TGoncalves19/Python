# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo, calcule e mostre o comprimento da hipotenusa.
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor da cateto adjacente '))
tg = co / ca
print('O comprimento da hipotenusa é {}'.format(tg))
