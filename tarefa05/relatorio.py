import telemetria

def trajetoria():
    v_max, leituras = telemetria.ler_trajetoria()
    x_d, y_d = input().split()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    reconstrucao = telemetria.reconstruir(leituras, corrompidas_detectadas)
    print(reconstrucao)

    return reconstrucao, x_d, y_d

trajetoria()

def distancia_total():
    ''' Recebe a tupla com as distancias corrigidas e calcula a distância euclediana com a função distancia entre cada par de distâncias
    '''

def distancia_daPartida():        
    ''' Acha qual é a primeira e a ultima posição, e usa a função distancia() para calcular a distancia euclediana entre elas '''

def velocidade_maxima():
    ''' Calcula a velocidade média entre dois pontos, armazena em uma lista e retorna a maior '''

def variacao_velocidade():
    ''' Recebe a lista de velocidades médias da função velociade_maxima e usa a função max_variacao de telemetria para calcular a maior variação das velocidades médias'''

def distancia_aoDestino():
    ''' Recebe a ultima distancia da trajetória corrigida e usa a função distancia() para calcular a distancia euclediana com a posição do destino da sonda ''' 

def posicao_estimada():
    '''Recebe as duas ultimas posições da trajetoria e calcula qual será a estimativa da proxima por (𝑥𝑛+(𝑥𝑛−𝑥𝑛−1),𝑦𝑛+(𝑦𝑛−𝑦𝑛−1)). '''

def main():
    pass