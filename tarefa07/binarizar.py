import normalizar

def entradas():
    arquivo_entrada, arquivo_saida= normalizar.entradas()
    largura, limiar, fator = input().split()

    return arquivo_entrada, arquivo_saida, largura, limiar, fator

def normalizacao(arquivo_entrada):
    ''' recebe as funções do normalizar.py para normalizar as matrizes do novo arquivo, tambem devolve a largura, limiar e o nivel de fator'''
    matriz, escala, comentario, proporcao, branco = normalizar.criar_matriz(arquivo_entrada)

    maior_valor, contador_branco_ini = normalizar.encontra_maior_valor(matriz)

    menor_valor, contador_preto_ini = normalizar.encontra_menor_valor(matriz)

    matriz_propor = normalizar.nova_matriz(matriz, maior_valor,menor_valor)

    return matriz_propor, branco, matriz, proporcao, escala, comentario

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
    ''' Percorre os itens da matriz largura, ve em cada lista dentro dessa matriz quais numeros são menores que o limiar e adicona em uma lista menores, que estará presente na matriz_menores'''
    #Analise dos itens menores que limiar
    matriz_menores = []
    limiar = int(limiar)

    m = len(matriz_largura)
    for i in range(m):
        n = len(matriz_largura[i])
        lista_menores = []
        matriz_menores.append(lista_menores)
        for j in range(n):
            atual = matriz_largura[i][j]
            if atual <= limiar:
                lista_menores.append(atual)
    
    return matriz_menores

def montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator):
    '''analisa o tamanho de cada lista em matriz_menores com a porcentagem do fator, para verificar se esse atual irá virar preto: ja que ele depende do tamanho da lista dos números ao seu redor ----- > vai adicionando cada atual em uma linha, e essa linha e adicionada em uma matriz nova ao acabar o loop'''

    matriz_binarizada = []
    lista_cores = []
    largura = int(largura)
    fator = float(fator)
    denominador = largura**2

    m = len(matriz_menores)
    for i in range(m):
        n = len(matriz_menores[i])
        porcentagem = n / denominador
        if porcentagem >= fator:
            lista_cores.append("0") #preto
        else:
            lista_cores.append("255") #branco
    k = 0
    for i in range(len(matriz_propor)):
        linha = []
        matriz_binarizada.append(linha)
        for j in range(len(matriz_propor[i])):
            linha.append(lista_cores[k])
            k += 1


    return matriz_binarizada


def novo_arquivo_binarizado(matriz_binarizada, arquivo_saida, escala, comentario, proporcao, branco):
    with open(arquivo_saida, "w") as arquivo:
        arquivo.write(escala)
        arquivo.write("\n")
        arquivo.write(comentario)
        arquivo.write("\n")
        arquivo.write(proporcao)
        arquivo.write("\n")
        arquivo.write(branco)
        arquivo.write("\n")

        for lista in matriz_binarizada:
            for numero in lista:
                arquivo.write(str(numero + " "))
            arquivo.write("\n")



def main():
    arquivo_entrada, arquivo_saida, largura, limiar, fator = entradas()

    matriz_propor, branco, matriz, proporcao, escala, comentario = normalizacao(arquivo_entrada)

    matriz_largura = contar_largura(matriz_propor, largura)

    matriz_menores = contar_limiar(limiar, matriz_largura)

    matriz_binarizada = montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator)

    contador_branco_in, contador_preto_in = normalizar.acha_brancos_pretos(matriz)
    print(f"{arquivo_entrada}: {contador_preto_in} pixels pretos e {contador_branco_in} pixels brancos")
    contador_branco_fin, contador_preto_fin = normalizar.acha_brancos_pretos(matriz_binarizada)
    print(f"{arquivo_saida}: {contador_preto_fin} pixels pretos e {contador_branco_fin} pixels brancos")

    novo_arquivo_binarizado(matriz_binarizada, arquivo_saida, escala, comentario, proporcao, branco)

if __name__ == "__main__": 
    main()
