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

def contar_largura(atual, matriz_propor, largura, i , j):
    ''' com base no item atual do loop da matriz, acha os itens em volta desse atual com base na largura e adiciona em uma lista'''
    largura = int(largura)
    lista_largura = []
    m = 0
    n = 0 
    while n + 2 < largura:  #deixa o n (contador) no range para percorrer a matriz
        n += 1  #somador das coluna
        m += 1 #somador das linha

    item_atual= matriz_propor[i-m][j-n]    
    indice_coluna = j-n
    indice_linha = i-m 
    while n > 0:
        for k in range(largura):
            indice_linha = i-m 
            for k in range(largura):
                item_atual = matriz_propor[indice_linha][indice_coluna]
                lista_largura.append(item_atual)
                j += 1 #pula uma coluna
                indice_coluna = j + n
            indice_linha = i + m #pula uma linha     
        n -= 1
        
    return lista_largura

def contar_limiar(limiar, matriz_propor, largura):
    ''' Percorre os itens da matriz normalizada, chama a função contar_largura, analisa quantos itens são menores que o limiar e adiciona em uma lista'''
    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            atual = matriz_propor[i][j]
            return atual, i ,j
            lista_largura = contar_largura(atual, matriz_propor, largura, i, j)
            '''Continuar'''
            



def matriz_binarizada():
    '''analisa o tamanho da matriz com a porcentagem do fator, para verificar se esse atual irá virar preto: ja que ele depende do tamanho da lista dos números ao seu redor ----- > vai adicionando cada atual em uma linha, e essa linha e adicionada em uma matriz nova ao acabar o loop'''

def novo_arquivo():
    pass

def main():
    matriz_propor, largura, limiar, fator = normalizacao()
    #print(matriz_propor)
    print(largura)
    print(limiar)
    print(fator)

    atual, i, j = contar_limiar(limiar, matriz_propor, largura)
    
    lista_largura = contar_largura(atual, matriz_propor, largura, i, j)
    print(lista_largura)

main()
