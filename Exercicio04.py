#Faça um algoritmo que leia dois números inteiros ( x e y)
#calcule o quociente e o resto da divisão de x por y e escreva os resultados.
x = int(input('Digite um número:'))
y = int(input('Digite outro número:'))
quoeficiente, resto = divmod(x, y)
print (f'Quociente e Resto da Divisão é: {quoeficiente, resto}')