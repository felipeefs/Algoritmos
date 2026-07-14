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
    '''Essas são as condições de recursão que verifica se o atual é preto e pinta as extremidades, caso forem pretas (0)'''
    
    if 0<= i-1 < m and 0 <= j < n:
        if int(matriz[i-1][j]) == 0:
            matriz[i-1][j] = 255
            pintador(matriz, i-1, j, m, n)
            
    if 0<= i < m and 0 <= j-1 < n:
        if int(matriz[i][j-1]) == 0:
            matriz[i][j-1] = 255
            pintador(matriz, i , j - 1, m, n)
            
    if 0<= i < m and 0 <= (j+1) < n:
        if int(matriz[i][j+1]) == 0:
            matriz[i][j+1] = 255
            pintador(matriz, i , j + 1, m, n)

    if 0<= i+1 < m and 0 <= j < n:
        if int(matriz[i+1][j]) == 0:
            matriz[i+1][j] = 255
            pintador(matriz, i+1 , j, m, n)
        
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
