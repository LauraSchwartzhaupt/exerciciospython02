#Elabore um algoritmo para calcular e escrever 
#o preço final de um computador,
#sendo fornecido o preço de fábrica
#o preço final do computador é calculado com base nos adicionais
#45% de imposto e 28% de revenda sobre o preço de fábrica:
preco_fabrica = float(input('Digite o valor do computador:'))
imposto = preco_fabrica * 0.45
revenda = preco_fabrica * 0.28
preco_final = imposto + revenda + preco_fabrica
print ('O valor final do computador para revenda é: {}' .format(preco_final) )