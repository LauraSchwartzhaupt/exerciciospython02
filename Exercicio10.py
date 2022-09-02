#Uma revendedora de carros usdados paga aos funcionários vendedores
#um salário fixo por mês, mais uma comissão por cada carro vendido.
#Escreva um algoritmo que leia o número do vendedor, o seu salário fixo,
#o número de carros por ele vendidos, e o valor que recebe por carro vendido, 
#e calcula o salário mensal do vendedor, escrevendo-o juntamente com  o seu número de identificação:
vendedor = float(input('Digite seu número de identificação:'))
salario_fixo = float(input('Informe o seu salário fixo:'))
carro_vendido = int(input('Informe a quantidade de carros vendidos:'))
comissao = int(input('Informe o valor da comissão recebida por cada carro vendido:'))
salario_mensal = comissao + salario_fixo
print (f'Seu salário mensal é de: {salario_mensal}')
