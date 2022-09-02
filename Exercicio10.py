vendedor = float(input('Digite seu número de identificação:'))
salario_fixo = float(input('Informe o seu salário fixo:'))
carro_vendido = int(input('Informe a quantidade de carros vendidos:'))
comissao = int(input('Informe o valor da comissão recebida por cada carro vendido:'))
salario_mensal = comissao + salario_fixo
print (f'Seu salário mensal é de: {salario_mensal}')
