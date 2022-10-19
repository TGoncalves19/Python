# Desafio 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado.
# A quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
dias = int(input('Informe a quantidade de dias: '))
km = float(input('Informe o Km rodado: '))
custo_total = (km * 0.15) + (dias * 60)
print('A diária do carro foi de {} dias. \nO trajeto pecorrido é de {}Km. \nTotal a pagar é de R$ {:.2f}.'.format(dias, km, custo_total))
