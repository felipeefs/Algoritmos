import normalizar

def normalizacao():
    ''' recebe as funções do normalizar.py para normalizar as matrizes do novo arquivo, tambem devolve a largura, limiar e o nivel de fator'''
    matriz, arquivo_entrada, arquivo_saida, escala, comentario, proporcao, branco = normalizar.entradas()
    largura, limiar, fator = input().split()

    maior_valor, contador_branco_ini = normalizar.encontra_maior_valor(matriz)

    menor_valor, contador_preto_ini = normalizar.encontra_menor_valor(matriz)

    matriz_propor = normalizar.nova_matriz(matriz, maior_valor,menor_valor)

    return matriz_propor, largura, limiar, fator

def contar_largura(matriz_propor, largura):
    ''' com base no item atual do loop da matriz, acha os itens em volta desse atual com base na largura e adiciona em uma lista'''

    largura = int(largura)
    largura_cont = largura
    matriz_largura = []
    soma_li = 0
    soma_co = 0
    somador = 0
    if largura > 1:
        while largura_cont > 1:
            largura_cont -= 2
            soma_co += 1  #somador das coluna
            soma_li += 1 #somador das linha
            somador += 1
    print(somador)
    
    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            #atual = matriz_propor[i][j]
            #DESCOBRE ITENS NA LARGURA:
            lista_largura = []
            matriz_largura.append(lista_largura)
            soma_li = somador #reseta as variaveis a cada item percorrido
            for k in range(largura):
                i_linha = i - (soma_li)
                soma_co = somador #reseta as variaveis a cada item percorrido
                for c in range(largura):
                    j_coluna = j - (soma_co)
                    if 0 <= j_coluna < n and 0 <= i_linha < m: # Se o indice for negativo, não existe esse item na matriz_propor
                        percorrido = matriz_propor[i_linha][j_coluna]
                        lista_largura.append(percorrido)
                    soma_co -= 1 #Vai diminuindo, lembrando que ao diminuir, pelos sinais a subtração vai tranformar em uma soma
                soma_li -= 1    
    
    return matriz_largura

def contar_limiar(limiar, matriz_largura):
    ''' Percorre os itens da matriz normalizada, chama a função contar_largura, analisa quantos itens são menores que o limiar e adiciona em uma lista'''
    #Analise dos itens menores que limiar



def matriz_binarizada(lista_menores, atual, largura, fator):
    '''analisa o tamanho da matriz com a porcentagem do fator, para verificar se esse atual irá virar preto: ja que ele depende do tamanho da lista dos números ao seu redor ----- > vai adicionando cada atual em uma linha, e essa linha e adicionada em uma matriz nova ao acabar o loop'''

    tamanho = len(lista_menores)
    porcentagem = tamanho / largura

    if porcentagem >= fator:
        atual = 0 # preto
    else:
        atual = 255 # branco


def novo_arquivo():
    pass

def main():
    matriz_propor, largura, limiar, fator = normalizacao()
    #print(matriz_propor)
    #print(largura)
    print(limiar)
    #print(fator)

    
    matriz_largura = contar_largura(matriz_propor, largura)
    print(matriz_largura)


main()
