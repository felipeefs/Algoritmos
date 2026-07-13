def entradas():
    '''Recebe o arquivo e transforma os pixels dela em uma matriz '''
    arquivo_entrada = input()

    with open(arquivo_entrada) as arquivo:
        escala = arquivo.readline().strip()
        comentario = arquivo.readline().strip()
        proporcao = arquivo.readline().strip()
        branco = arquivo.readline().strip()
        matriz = []

        for linha in arquivo:
            linha = ((linha.strip()).split())
            matriz.append(linha)

        return matriz

def pintador(matriz, i, j, m, n):
    '''Essas são as condições de recursão que verifica se o atual é preto e pinta caso as extremidades sejam pretas'''
    #Somadores para a esquerda e direita, conforme sabe-se que a largura é 3
    soma_li = 1
    soma_co = 1
    somador = 1
    for k in range(3): #tres é por conta da quantidade de numeros que estamos comparando em volta do atual
        i_linha = i - (soma_li)
        soma_co = somador
        for c in range(3):
            j_coluna = j - (soma_co)
            if 0<= j_coluna < n and 0 <= i_linha < m:
                percorrido = int(matriz[i_linha][j_coluna])
                if percorrido == 000:
                    matriz[i_linha][j_coluna] = 255
                    pintador(matriz, i_linha, j_coluna, m, n) #O recurso com o indice da linha e coluna atual
            soma_co -=1
        soma_li -= 1
    '''

    NOVA TENTATIVA MAS NAO DEU TEMPO
    if matriz[i-1][j] == 0 and 0<= i-1 < n and 0 <= j < m:
        pintador(matriz, i-1, j, m, n)
        matriz[i-1][j] = 255
    if matriz[i][j-1] == 0 and 0<= i < n and 0 <= j-1 < m:
        pintador(matriz, i , j - 1, m, n)
        matriz[i][j-1] = 255
    if matriz[i][j+1] == 0 and 0<= i < n and 0 <= j+1 < m:
        pintador(matriz, i , j + 1, m, n)
        matriz[i][j+1] = 255
    if matriz[i+1][j] == 0 and 0<= i+1 < n and 0 <= j < m:
        pintador(matriz, i+1 , j, m, n)
        matriz[i+1][j] = 255
'''


def achar_colonias(matriz):
    '''Recebe a matriz e usa recursão para descobrir a quantidade de colonias usando um contador'''
    contador = 0
    #Caso básico (Verifica se o primeiro item é preto, e se os que estão em volta tambem são):
    m = len(matriz)
    for i in range(m):
        n = len(matriz[i])
        for j in range(n):
            if int(matriz[i][j]) == 000:
                contador += 1
                matriz[i][j] = 255
                pintador(matriz, i, j, m, n) #O recurso, que verifica se os pixels em volta também são pretos


    return contador

def main():
    matriz = entradas()
    contador = achar_colonias(matriz)
    print(f"A imagem tem {contador} colônias.")


main()
