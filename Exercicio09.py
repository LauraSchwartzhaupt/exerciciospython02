preco_fabrica = float(input('Digite o valor do computador:'))
imposto = preco_fabrica * 0.45
revenda = preco_fabrica * 0.28
preco_final = imposto + revenda + preco_fabrica
print ('O valor final do computador para revenda é: {}' .format(preco_final) )