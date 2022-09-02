#Faça um algoritmo que leia 3 números inteiros e:
#Escreva o produto destes números
#Escreva a soma deste números
#Escreva a subtração destes números
#Escreva a soma de todos os resultados acima
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))
multiplicacao = n1 * n2 * n3 
soma = n1 + n2 + n3 
subtracao = n1 - n2 - n3
resultados = (f' {multiplicacao + soma + subtracao}')
print (f'O resultado final é {resultados}')