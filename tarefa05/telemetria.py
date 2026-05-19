import math

def ler_trajetoria():
    """
    Lê os dados de telemetria da entrada padrão.
    A entrada contém o número N de leituras, a velocidade máxima V_max
    e N linhas com instante t, coordenada x e coordenada y.
    Devolve a velocidade máxima e uma lista de tuplas (t, x, y).

    Exemplo de uso: v_max, leituras = ler_trajetoria()
    """
    n_leituras = int(input())
    v_max = float(input())
    i = 0
    leituras = []
    while n_leituras > i:
        t, x, y = input().split()
        t = float(t)
        x = float(x)
        y = float(y)
        i += 1
        leituras_tupla = (t, x, y) 
        leituras.append(leituras_tupla) 
    return v_max, leituras

def distancia(x1, y1, x2, y2):
    """
    Recebe as coordenadas de dois pontos (x1, y1) e (x2, y2).
    Devolve a distância euclidiana entre eles.

    Exemplo: distancia(0, 0, 3, 4) devolve 5.0.
    """
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia
    
def detectar_corrompidas(leituras, v_max):
    """
    Recebe uma lista de tuplas (t, x, y) representando as leituras
    de telemetria e a velocidade máxima da sonda.
    Devolve uma lista de booleanos de mesmo tamanho, onde True
    indica que a leitura correspondente é corrompida.
    A primeira e a última leitura são sempre válidas (False).

    Exemplo de uso: corrompidas = detectar_corrompidas(leituras, v_max)
    """
    corrompidas = []
    ta, xa, ya = leituras[0] #começa na primeira posição e vai passando quando for uma posição valida

    for i in range(len(leituras)):

        if i == 0 or i == len(leituras) - 1: #diferente da primeira hora e ultima hora (leituras sempre validas)
            corrompidas.append(False)
        else:
            t, x, y = leituras[i]
            v_med = math.sqrt((x - xa)**2 + (y - ya)**2) / (t - ta)
            if v_med > v_max:
                corrompidas.append(True)
            else:
                corrompidas.append(False)
                ta, xa, ya = t, x, y #Se não é corrompida o t_a, x_a e y_a recebem a posição atual que é valida
    return corrompidas

def interpolar(xa, ya, ta, xb, yb, tb, t):
    """
    Recebe as coordenadas e instantes de dois pontos válidos
    (xa, ya) no instante ta e (xb, yb) no instante tb,
    e o instante t de uma leitura corrompida (ta < t < tb).
    Devolve um par x, y com as coordenadas interpoladas.

    Exemplo: interpolar(0, 0, 0, 10, 10, 4, 2) devolve 5.0, 5.0.
    """
    x = xa + ((xb - xa) * ((t - ta) / (tb - ta)))
    y = ya + ((yb - ya) * ((t - ta) / (tb - ta)))
    return x, y


def reconstruir(leituras, corrompidas):
    """
    Recebe uma lista de tuplas (t, x, y) representando as leituras
    de telemetria e uma lista de booleanos indicando quais leituras
    são corrompidas.
    Devolve uma nova lista de tuplas (t, x, y) com a trajetória
    corrigida, substituindo leituras corrompidas por valores
    interpolados.

    Exemplo de uso: corrigida = reconstruir(leituras, corrompidas)
    """
    corrigida = []
    ta, xa, ya = leituras[0]
    
    for i in range(len(leituras)):
        if not corrompidas[i]: # Se for False
            corrigida.append(leituras[i])
            ta, xa ,ya = leituras[i]        #Atualização das varialveis "a"
            
        else:
            j = i + 1
            t, x, y = leituras[i]
            while corrompidas[j]:           #Loop para as variaveis "b" ganharem seu valor
                j += 1   
            tb, xb, yb = leituras[j]

            x_corri, y_corri = interpolar(xa, ya, ta, xb, yb, tb, t)
            nova_tupla = (t, x_corri, y_corri)
            corrigida.append(nova_tupla)
            
    return corrigida


def max_variacao(valores):
    """
    Recebe uma lista de números (com pelo menos dois elementos).
    Devolve a maior diferença absoluta entre dois elementos
    consecutivos da lista.

    Exemplo: max_variacao([1.0, 3.0, 2.0, 5.0]) devolve 3.0,
    pois |5.0 - 2.0| = 3.0 é a maior variação consecutiva.
    """
    lista_subtracao = []
    for i in range(len(valores) -1 ):
        j = i + 1
        if valores[i] < valores[j]:
            subtracao = valores[j] - valores [i]
        else:
            subtracao = valores[i] - valores [j]
        lista_subtracao.append(subtracao)
    
    diferenca = 0
    for i in range(len(lista_subtracao) - 1):
        j = i + 1
        if lista_subtracao[i] > lista_subtracao[j]:
            diferenca = lista_subtracao[i]
        else:
            diferenca = lista_subtracao[j]

    return diferenca
            