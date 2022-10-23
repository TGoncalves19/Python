# Manipulando Cadeias de Textos
# Fatiamento
frase = 'Thiago Pereira Gonçalves'  # Essa frase contém 24 caracteres, incluindo o espaço.
# print(frase[9]) #imprimi o caractere nono da frase '__________r...'
# print(frase[7:14]) #imprimi o caractere sétimo ao quinte '_______Pereira_...'
# print(frase[7:24]) #imprimi o caractere sétimo ao vinte e quatro '_______Pereira Gonçalves'
# print(frase[7:14:2]) #imprimi o caractere sétimo ao vinte e quatro, pulando dois em dois '_______P_r_i_a_'
# print(frase[:6]) #imprimi o caractere antes do ': = 0' e termina no sexto 'Thiago_'
# print(frase[15:]) #imprimi o caractere que inicia no quinze até o final '_______________Gonçalves'
# print(frase[15::3]) #imprimi do caractere quinze, pulando três em três '_______________G__ç__V'

# Ánalise
# print(len(frase)) #É o comprimento ou quantidade de caracteres
# print(frase.count('o')) #Conta quantas vezes tem uma letra, neste caso a letra minúscula '_____o__________o_______'
# print(frase.count('o',0,13)) # A quantidade da letra 'o) de zero a treze '_____o________'
# print(frase.find('Gon')) #Identifica em qual caractere começa '_______________Gon'
# print(frase.find('Android')) #Quando a string não existe o resultado é -1.
# print('Thiago' in frase) #Esse comando verifica se existe uma palavra da variável.

# Transformação
# print(frase.replace('Thiago', 'Thais')) #Essa função substitui as palavras.
# print(frase.upper()) #Esse metódo deixa o texto em maísculo.
# print(frase.lower())  #Esse metódo deixa o texto em minúsculo.
# print(frase.capitalize()) #O primeiro caractere em maísculo e o resto em minúsculo.
# print(frase.title()) # Deixa a primeira letra de cada palavra em maíscula.
texto = '   Maria Regina  '
#print(texto)
#print(texto.strip()) #Remove os espaços sobrando do começo e do final.
#print(texto.rstrip()) #Remove os espaços a direita.
#print(texto.lstrip()) #Remove os espaços a esquerda

#Divisão
#print(frase.split()) #Divide as strigs em cada elemento.

#Junção
#print('-'.join(frase)) #Separa os textos 'T-h-i-a-g-o-....'

#Print texto grande
print("""welcome! Are you completely new to programming?
If not then we presume you will be looking for information...""")
