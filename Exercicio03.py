tempo_gasto = float(input('Informe o tempo gasto na sua viagem:'))
velocidade_media = int(input('Informe a velocidade média do seu carro durante a viagem:'))
distancia = tempo_gasto * velocidade_media
litros_gastos = distancia / 12
print (f' Você gastou:{litros_gastos} durante sua viagem')