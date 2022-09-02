#Faça um algoritmo que calcule e escreva o preço final de um computador, 
#sendo fornecido o preço de fábrica. O preço final do computador é calculado com base
#nos adicionais de: 30% de imposto e 10% de revenda sobre o preço de fábrica:
preco_fabrica = float(input('Digite o valor do computador:'))
imposto = preco_fabrica *0.3
revenda = preco_fabrica *0.1
preco_final = imposto + revenda + preco_fabrica
print ('O valor final do computador para revenda é: {}' .format(preco_final) )