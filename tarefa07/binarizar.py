import normalizar

def normalizacao():
    ''' recebe as funções do normalizar.py para normalizar as matrizes do novo arquivo, tambem devolve a largura, limiar e o nivel de fator'''
    matriz, arquivo_entrada, arquivo_saida, escala, comentario, proporcao, branco = normalizar.entradas()
    largura, limiar, fator = input().split()

    maior_valor, contador_branco_ini = normalizar.encontra_maior_valor(matriz)

    menor_valor, contador_preto_ini = normalizar.encontra_menor_valor(matriz)

    matriz_propor = normalizar.nova_matriz(matriz, maior_valor,menor_valor)

    print(contador_branco_ini)
    print(contador_preto_ini)

    return matriz_propor, largura, limiar, fator

def contar_largura(matriz_propor, largura):
    ''' com base no item atual do loop da matriz, acha os itens em volta desse atual com base na largura e adiciona em uma lista'''
    largura = int(largura)
    lista_largura = []
    soma_li = 0
    soma_co = 0 
    contador = 0
    while contador + 2 < largura:  #deixa o n (contador) no range para percorrer a matriz
        soma_co += 1  #somador das coluna
        soma_li += 1 #somador das linha
        contador += 1

    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            atual = matriz_propor[i][j]
            indice_coluna = j-soma_co
            indice_linha = i-soma_li
            while contador > 0:
                for k in range(largura):
                    for l in range(largura):
                        item_atual = matriz_propor[indice_linha][indice_coluna]
                        lista_largura.append(item_atual)
                        j += 1 #pula uma coluna
                        indice_coluna += soma_co
                    indice_linha += soma_li #pula uma linha     
                contador -= 1
        
    return lista_largura

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

def matriz_binarizada():
    '''analisa o tamanho da matriz com a porcentagem do fator, para verificar se esse atual irá virar preto: ja que ele depende do tamanho da lista dos números ao seu redor ----- > vai adicionando cada atual em uma linha, e essa linha e adicionada em uma matriz nova ao acabar o loop'''

def novo_arquivo():
    pass

def main():
    matriz_propor, largura, limiar, fator = normalizacao()
    #print(matriz_propor)
    #print(largura)
    print(limiar)
    #print(fator)

    
    lista_largura = contar_largura(matriz_propor, largura)
    print(lista_largura)

    lista_menores = contar_limiar(limiar, lista_largura)
    print(lista_menores)

main()
