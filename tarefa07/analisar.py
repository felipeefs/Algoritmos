import binarizar

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
    indice_i = int(x) 
    indice_j = int(y)
    ponto_central = matriz_binarizada[indice_i][indice_j]

    return ponto_central

def descobrir_distancia():
    ''' Para cada ponto da matriz, descobrir sua distancia em x e y do ponto central, com base nisso, usa-se teo. de pitagoras para descobrir a distancia desse pixel ao centro -----> adiciona cada distancia em uma lista de distancias'''

def descobrir_colonia_bacterias():
    '''Verifica na lista de distancia se a distancia é menor igual ao raio, caso for, a bacteria é valida'''

def descobrir_numero_colonias():
    ''' Faz uma divisão do numero de bacterias com o n_medio, e verifica se precisa de diluição ou não'''

def main():
    arquivo_entrada, largura, limiar, fator, x, y, raio = entradas()
    matriz_binarizada = binarizaracao(arquivo_entrada, largura, limiar, fator)

    #print(matriz_binarizada)

    ponto_central = descobrir_centro(x, y, matriz_binarizada)
    print(ponto_central)

main()
