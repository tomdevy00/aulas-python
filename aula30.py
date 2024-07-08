"""
CONSTANTE = "Variaveis" que não vão mudar
Muitas condiçoes no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
"""
velocidade = 61 # velocidade atual do carro
local_carro = 80 # local em que o carro esta na estrada

RADAR1 = 60 # velocidade maxima do radar 1
LOCAL1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

velocidadepassouradar1 = velocidade > RADAR1
carropassouradar1 = local_carro >= (LOCAL1 - RADAR_RANGE) and \
    local_carro <= (LOCAL1 + RADAR_RANGE)
carromultadoradar1 = carropassouradar1 and velocidadepassouradar1

if velocidadepassouradar1:
        print('velocidade ultrapassou o limite de velocidade do radar 1')

if carropassouradar1:
        print('carro passou radar1')

