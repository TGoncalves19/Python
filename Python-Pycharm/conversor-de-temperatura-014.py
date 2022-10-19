#Desafio 014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
c = float(input('Informe a temperatura °C: '))
f = ((9 * c) / 5) + 32
k = c + 273
print('A temperatura é de {:.0f}°C, convertida para Fahrenheit é de: {}°F'.format(c, f))
print('A temperatura é de {:.0f}°C, convertida para Kelvin é de: {}°K'.format(c, k))
