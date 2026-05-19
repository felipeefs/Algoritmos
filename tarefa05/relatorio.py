import telemetria

def trajetoria():
    v_max, leituras = telemetria.ler_trajetoria()
    x_d, y_d = input().split()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    reconstruidas = telemetria.reconstruir(leituras, corrompidas_detectadas)
    print(reconstruidas)

    return reconstruidas, x_d, y_d

def distancia_total(reconstruidas):
    ''' Recebe a tupla com as distancias corrigidas e calcula a distância euclediana com a função distancia entre cada par de distâncias e soma todas elas
    '''
    distancias = []
    for i in range(1, len(reconstruidas)):
        t1, x1, y1 = reconstruidas[i-1]
        t2, x2, y2 = reconstruidas[i]
        distancia = telemetria.distancia(x1, y1, x2, y2)
        distancias.append(distancia)

    distancia_percorrida = 0
    for distancia in distancias:
        distancia_percorrida += distancia
    
    return distancia_percorrida

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
    reconstruidas, x_d, y_d = trajetoria()
    distancia_percorrida = distancia_total(reconstruidas)
    print(distancia_percorrida)

main()