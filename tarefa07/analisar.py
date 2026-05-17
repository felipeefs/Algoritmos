import binarizar
import math

def entradas():
    arquivo_entrada = input()
    largura, limiar, fator = input().split()
    x, y, raio = input().split()
    n_medio = input()

    return arquivo_entrada, largura, limiar, fator, x, y, raio

def binarizaracao(arquivo_entrada, largura, limiar, fator):
    matriz_propor, branco, matriz, proporcao, escala, comentario = binarizar.normalizacao(arquivo_entrada)

    matriz_largura = binarizar.contar_largura(matriz_propor, largura)

    matriz_menores = binarizar.contar_limiar(limiar, matriz_largura)

    matriz_binarizada = binarizar.montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator)

    return matriz_binarizada # Lembrar que todos os itens aqui estão como string

def descobrir_centro(x, y, matriz_binarizada):
    ''' A partir das coordenadas x e y, descobre-se o ponto central da matriz'''
    indice_iCentro = int(x) 
    indice_jCentro = int(y)
    ponto_central = matriz_binarizada[indice_iCentro][indice_jCentro]

    return ponto_central, indice_iCentro, indice_jCentro

def descobrir_distancia(matriz_binarizada, indice_iCentro, indice_jCentro):
    ''' Para cada ponto da matriz, descobrir sua distancia em x e y do ponto central, com base nisso, usa-se teo. de pitagoras para descobrir a distancia desse pixel ao centro -----> adiciona cada distancia em uma lista de distancias'''
    lista_distancias = []
    m = len(matriz_binarizada)

    for i in range(m):
        dist_x = 0 #Vai somando a distancia em x
        indice_i = i
        n = len(matriz_binarizada[i])
        #CALCULO DA DISTANCIA EM X:
        if indice_i < indice_iCentro:
            while indice_i < indice_iCentro:
                indice_i += 1
                dist_x += 1
        else: 
            while indice_i > indice_iCentro:
                indice_i -= 1
                dist_x += 1

        for j in range(n):
            dist_y = 0 #Vai somando a distancia em y
            indice_j = j
            #CALCULO DA DISTANCIA EM Y:
            if indice_j < indice_jCentro:
                while indice_j < indice_jCentro:
                    indice_j += 1
                    dist_y += 1
            else: 
                while indice_j > indice_jCentro:
                    indice_j -= 1
                    dist_y += 1

            distancia = math.sqrt((dist_x**2) + (dist_y**2))
            lista_distancias.append(distancia)

    return lista_distancias

def descobrir_colonia_bacterias():
    '''Verifica na lista de distancia se a distancia é menor igual ao raio, caso for, a bacteria é valida'''

def descobrir_numero_colonias():
    ''' Faz uma divisão do numero de bacterias com o n_medio, e verifica se precisa de diluição ou não'''

def main():
    arquivo_entrada, largura, limiar, fator, x, y, raio = entradas()
    matriz_binarizada = binarizaracao(arquivo_entrada, largura, limiar, fator)

    #print(matriz_binarizada)

    ponto_central, indice_iCentro, indice_jCentro = descobrir_centro(x, y, matriz_binarizada)
    print(ponto_central)

    lista_distancias = descobrir_distancia(matriz_binarizada, indice_iCentro, indice_jCentro)
    print(lista_distancias)

main()
