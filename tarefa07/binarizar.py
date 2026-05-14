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
    lista_largura = []
    soma_li = 0
    soma_co = 0 
    cont_largura = largura
    while soma_co + 2 < largura:  #deixa o n (cont_largura) no range para percorrer a matriz
        soma_co += 1  #somador das coluna
        soma_li += 1 #somador das linha

    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            atual = matriz_propor[i][j]

            indice_linha = i-soma_li
            while cont_largura > 0: # esse contador não faz sentido
                for l in range(largura):
                    indice_coluna = j-soma_co
                    for c in range(largura):
                        item_percorrido = matriz_propor[indice_linha][indice_coluna]
                        lista_largura.append(item_percorrido) # PROBLEMA A LISTA LARGURA SEMPRE MUDA PARA CADA ATUAL
                        indice_coluna += soma_co
                    print(lista_largura)
                    indice_linha += soma_li #pula uma linha     
                    cont_largura -= 1

    '''
    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            atual = matriz_propor[i][j]
    '''


        
    return lista_largura, atual

def contar_limiar(limiar, lista_largura):
    ''' Percorre os itens da matriz normalizada, chama a função contar_largura, analisa quantos itens são menores que o limiar e adiciona em uma lista'''
    #Analise dos itens menores que limiar
    lista_menores = []
    for item in lista_largura:
        item = int(item)
        limiar = int(limiar)
        if item < limiar:
            lista_menores.append(item)

    return lista_menores

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

    
    lista_largura, atual = contar_largura(matriz_propor, largura)
    print(lista_largura)
    print(atual)

    lista_menores = contar_limiar(limiar, lista_largura)
    print(lista_menores)

main()
