import telemetria
import math

def trajetoria():
    v_max, leituras = telemetria.ler_trajetoria()
    x_d, y_d = input().split()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    reconstruidas = telemetria.reconstruir(leituras, corrompidas_detectadas)

    return reconstruidas, x_d, y_d

def distancia_total(reconstruidas):
    ''' Recebe a tupla com as distancias corrigidas e calcula a distância euclediana com a função distancia entre cada par de distâncias e soma todas elas
    '''
    distancias = []
    for i in range(1, len(reconstruidas)):
        t1, x1, y1 = reconstruidas[i-1]
        t2, x2, y2 = reconstruidas[i]
        distancia = telemetria.distancia(x1, y1, x2, y2) #Chama função da telemetria
        distancias.append(distancia)

    distancia_percorrida = 0
    for distancia in distancias:
        distancia_percorrida += distancia
    
    return distancia_percorrida

def distancia_daPartida(reconstruidas):        
    ''' Acha qual é a primeira e a ultima posição, e usa a função distancia() para calcular a distancia euclediana entre elas '''
    ultimo_indice = len(reconstruidas) -1
    t1, x1, y1 = reconstruidas[0]
    t2, x2 ,y2 = reconstruidas[ultimo_indice]

    distancia_extrema = telemetria.distancia(x1,y1,x2,y2) #Chama função da telemetria

    return distancia_extrema

def velocidade_maxima(reconstruidas):
    ''' Calcula a velocidade média entre dois pontos, armazena em uma lista e retorna a maior '''

    velocidades = []
    for i in range(1, len(reconstruidas)):
        ta, xa, ya = reconstruidas[i-1]
        t, x, y = reconstruidas[i]
        v_med = math.sqrt((x - xa)**2 + (y - ya)**2) / (t - ta)
        velocidades.append(v_med)

    maior_vel = velocidades[0]
    for velocidade in velocidades:
        if velocidade > maior_vel:
            maior_vel = velocidade

    return velocidades, maior_vel


def variacao_velocidade(velocidades):
    ''' Recebe a lista de velocidades médias da função velociade_maxima e usa a função max_variacao de telemetria para calcular a maior variação das velocidades médias'''
    maior_variacao_velocidades = telemetria.max_variacao(velocidades)
                                                                        
    return maior_variacao_velocidades

def distancia_aoDestino(reconstruidas, x_d, y_d):
    ''' Recebe a ultima distancia da trajetória corrigida e usa a função distancia() para calcular a distancia euclediana com a posição do destino da sonda ''' 
    ultimo_indice = len(reconstruidas) -1
    t, x, y = reconstruidas[ultimo_indice]
    x_d = float(x_d)
    y_d = float(y_d)
    distancia_destino = telemetria.distancia(x, y, x_d, y_d)

    return distancia_destino

def posicao_estimada(reconstruidas):
    '''Recebe as duas ultimas posições da trajetoria e calcula qual será a estimativa da proxima por (𝑥𝑛+(𝑥𝑛−𝑥𝑛−1),𝑦𝑛+(𝑦𝑛−𝑦𝑛−1)). '''
    ultimo_indice = len(reconstruidas) -1
    penultimo_indice = len(reconstruidas) -2

    tn, xn, yn = reconstruidas[ultimo_indice]
    tn1, xn1, yn1 = reconstruidas[penultimo_indice]

    x_estimado = (xn + (xn - xn1))
    y_estimado = (yn + (yn - yn1))

    return x_estimado, y_estimado


def main():
    reconstruidas, x_d, y_d = trajetoria()
    distancia_percorrida = distancia_total(reconstruidas)
    print(f"Distância total percorrida: {distancia_percorrida:.2f}")

    distancia_extrema = distancia_daPartida(reconstruidas)
    print(f"Distância ao ponto de partida: {distancia_extrema:.2f}")

    velocidades, maior_velo = velocidade_maxima(reconstruidas)
    print(f"Velocidade máxima: {maior_velo:.2f}")

    maior_variacao_velocidades = variacao_velocidade(velocidades)
    print(f"Variação máxima de velocidade: {maior_variacao_velocidades:.2f}")

    distancia_destino = distancia_aoDestino(reconstruidas, x_d, y_d)
    print(f"Distância ao destino: {distancia_destino:.2f}")

    x_estimado, y_estimado = posicao_estimada(reconstruidas)
    print(f"Próxima posição estimada: {x_estimado:.2f} {y_estimado:.2f}")

main()