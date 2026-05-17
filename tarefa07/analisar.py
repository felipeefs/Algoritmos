import binarizar
import math

def entradas():
    arquivo_entrada = input()
    largura, limiar, fator = input().split()
    x, y, raio = input().split()
    n_medio = input()

    return arquivo_entrada, largura, limiar, fator, x, y, raio, n_medio

def binarizaracao(arquivo_entrada, largura, limiar, fator):
    matriz_propor, branco, matriz, proporcao, escala, comentario = binarizar.normalizacao(arquivo_entrada)

    matriz_largura = binarizar.contar_largura(matriz_propor, largura)

    matriz_menores = binarizar.contar_limiar(limiar, matriz_largura)

    matriz_binarizada = binarizar.montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator)

    return matriz_binarizada # Lembrar que todos os itens aqui estão como string

def descobrir_centro(x, y, matriz_binarizada):
    '''A partir das coordenadas x e y, descobre-se o ponto central da matriz'''
    m = len(matriz_binarizada)

    indice_jCentro = int(x)  #colunas
    indice_iCentro = (m - 1) - int(y)  #linhas (precisa inverter)
    ponto_central = matriz_binarizada[indice_iCentro][indice_jCentro]

    return ponto_central, indice_iCentro, indice_jCentro

def descobrir_distancia(matriz_binarizada, indice_iCentro, indice_jCentro, raio):
    ''' Para cada ponto da matriz, descobrir sua distancia em x e y do ponto central, com base nisso, usa-se teo. de pitagoras para descobrir a distancia desse pixel ao centro -----> adiciona cada distancia em uma lista de distancias'''
    lista_distancias = []
    colonia_bacteria = 0

    m = len(matriz_binarizada)
    for i in range(m):
        dist_y = 0 #Vai somando a distancia em y
        indice_i = i
        n = len(matriz_binarizada[i])
        #CALCULO DA DISTANCIA EM X:
        
        dist_y = indice_iCentro - i
       

        for j in range(n):
            dist_x = 0 #Vai somando a distancia em y
            indice_j = j
            atual = matriz_binarizada[i][j]
            #CALCULO DA DISTANCIA EM Y:
            dist_x = indice_jCentro - j


            if atual == "0":
                distancia = math.sqrt((dist_x**2) + (dist_y**2))
                if distancia <= int(raio):
                    colonia_bacteria += 1

    return colonia_bacteria

def descobrir_colonia_bacterias(lista_distancias, raio):
    '''Verifica na lista de distancia se a distancia é menor igual ao raio, caso for, a bacteria é valida'''
    colonia_bacteria = 0
    for distancia in lista_distancias:
        if distancia <= int(raio):
            colonia_bacteria += 1

    return colonia_bacteria            

def descobrir_numero_colonias(colonia_bacteria, n_medio):
    ''' Faz uma divisão do numero de bacterias com o n_medio, e verifica se precisa de diluição ou não'''
    n_colonia = colonia_bacteria / int(n_medio)
    n_colonia = int(n_colonia)

    if n_colonia < 30:
        mensagem = "Placa inadequada, dilua menos a amostra."
    elif 300 > n_colonia > 30:
        mensagem = "Placa adequada para contagem."
    else:
        mensagem = "Placa inadequada, dilua mais a amostra."

       
    return n_colonia, mensagem

def main():
    arquivo_entrada, largura, limiar, fator, x, y, raio, n_medio = entradas()

    matriz_binarizada = binarizaracao(arquivo_entrada, largura, limiar, fator)

    ponto_central, indice_iCentro, indice_jCentro = descobrir_centro(x, y, matriz_binarizada)

    #lista_distancias = descobrir_distancia(matriz_binarizada, indice_iCentro, indice_jCentro)

    colonia_bacteria =  descobrir_distancia(matriz_binarizada, indice_iCentro, indice_jCentro, raio)

    n_colonia, mensagem = descobrir_numero_colonias(colonia_bacteria, n_medio)

    print(f"Número de colônias estimado: {n_colonia}")
    print(mensagem)

main()
