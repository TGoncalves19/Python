# Operadores Aritméticos
# 1- () parênteses
# 2- ** potência
# 3- *, /, //, % multiplicação, divisão, divisão inteiro, divisão resto
# 4- +, - soma, subtração

# n1 = int(input('Digite um valor: '))
# n2 = int(input('Outro valor: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
# print('A divisão inteira {} e potência {}'.format(di,e))

# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
# n1 = int(input('Digite um número: '))
# a = n1 + 1
# s = n1 -1
# print('Analisando o valor: {}, o seu sucessor é: {}, e seu antecessor é: {}'.format(n1, a, s))

# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
#n1 = int(input('Digite um número: '))
#d = n1 * 2
#t = n1 * 3
#r = n1 ** (1 / 2)  # pode utilizar o comando pow(n1, (1/2))
#print('O dobro é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}'.format(d, t, r))

# Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
#nota1 = float(input('Primeira nota: '))
#nota2 = float(input('Segunda nota: '))
#media = (nota1 + nota2) / 2
#print('A primeira nota: {:.1f} e a segunda nota: {:.1f} \nA média final é: {:.1f}'.format(nota1, nota2, media))
#if media > 6:
 #print('Aprovado')
#else:
 #print('Reprovado')

# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#metro = int(input('Digite uma distância em metros: '))
#cm = metro * 100
#mm = metro * 1000
#print('{} metros. \n{} Cetímetros. \n{} Milímetros.'.format(metro, cm, mm))

# Desafio 009 - Faça um programa que leia um número interio qualquer e mostre na tela a sua tabuada.
#tab = int(input('Digite um número: '))
#print('-' * 14)
#print('{:2} x {:2} = {:2}'.format(0, tab, tab * 0))
#print('{:2} x {:2} = {:2}'.format(1, tab, tab * 1))
#print('{:2} x {:2} = {:2}'.format(2, tab, tab * 2))
#print('{:2} x {:2} = {:2}'.format(3, tab, tab * 3))
#print('{:2} x {:2} = {:2}'.format(4, tab, tab * 4))
#print('{:2} x {:2} = {:2}'.format(5, tab, tab * 5))
#print('{:2} x {:2} = {:2}'.format(6, tab, tab * 6))
#print('{:2} x {:2} = {:2}'.format(7, tab, tab * 7))
#print('{:2} x {:2} = {:2}'.format(8, tab, tab * 8))
#print('{:2} x {:2} = {:2}'.format(9, tab, tab * 9))
#print('{:2} x {:2} = {:2}'.format(10, tab, tab * 10))
#print('-' * 14)

# Desafio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#reais = float(input('Digite a quantidade de reais (R$): '))
#dolar = float(input('Digite a cotação do dólar (US$): '))
#total = reais / dolar
#print('Você tem US$ {:.2f} dólares'.format(total))

# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
#altura = float(input('Digite a altuta (m): '))
#largura = float(input('Digite a largura (m): '))
#rendimento = float(input('Digite o redimento da tinta conforme o fabricante (m²): '))
#area = altura * largura
#area_pintura = area / rendimento
#print('A altura da parede é: {} m, a largura da parede é: {} m, no total de: {} m². \nA quantidade de tinta para pintura é: {:.2f}L.'.format(altura, largura, area, area_pintura))

# Desafio 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo novo preço com 5% de deconto.
#valor_produto = float(input('Digite o valor de produto (R$): '))
#desconto = float(input('Digite o desconto (%): '))
#valor_novo = valor_produto - (valor_produto * (desconto / 100))
#print('O produto custa R$: {:.2f} reais, com desconto de: {:.0f}% ficou em R$: {:.2f} reais'.format(valor_produto, desconto, valor_novo))

# Desafio 013 - Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento.
#salario = float(input('Digite o sálario atual (R$): '))
#salario_aumento = float(input('Digite o valor do reajuste (%): '))
#novo_salario = salario + (salario * (salario_aumento / 100))
#print('O sálario atual é (R$): {:.2f}, o reajuste previsto foi de: {:.0f}%. \nO novo sálario é (R$): {:.2f} reais'.format(salario, salario_aumento, novo_salario))
