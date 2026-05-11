def entradas():
    '''Recebe as entradas e transforma os números em listas que são adicionadas em uma matriz '''
    arquivo_entrada = input()
    arquivo_saida = input()

    with open(arquivo_entrada) as arquivo:
        escala = arquivo.readline().strip()
        comentario = arquivo.readline().strip()
        proporcao = arquivo.readline().strip()
        branco = arquivo.readline().strip()
        matriz = []
        for linha in arquivo:
            linha = ((linha.strip()).split( ))
            matriz.append((linha))  #Ta adicionando cada linha em uma lista, depois essa lista é adicionada em matrizes

    print(escala)
    print(comentario)
    print(proporcao)
    print(branco)
    print(matriz)
    return matriz

def encontra_maior_valor(matriz):
    '''Acha o maior valor da matriz, o branco .Se achar um branco(255), adiciona no contador_branco_ini)
     ESSA FUNÇÃO PODE SER USADA DE NOVO PARA CALCULAR A QUANTIDADE DE BRANCOS NA MATRIZ CORRIGIDA'''
    contador_branco_ini = 0
    maior_valor = int(matriz[0][0]) # adiciona o primeiro valor com base, para passar nos loops e se mudado
    m = len(matriz)
    for i in range(m):
        n =  len(matriz[i])
        for j in range(n):
            atual = int(matriz[i][j])
            if atual > maior_valor:
                maior_valor = atual
            if atual == 255:
                contador_branco_ini += 1

    return maior_valor, contador_branco_ini

def encontra_menor_valor(matriz):
    '''Acha o menor valor da matriz, o preto. Se achar um preto (0), adiciona no contador_preto_ini
    ESSA FUNÇÃO PODE SER USADA DE NOVO PARA CALCULAR A QUANTIDADE DE PRETOS NA MATRIZ CORRIGIDA'''
    contador_preto_ini = 0
    menor_valor = int(matriz[0][0]) # adiciona o primeiro valor com base, para passar nos loops e se mudado
    m = len(matriz)
    for i in range(m):
        n =  len(matriz[i])
        for j in range(n):
            atual = int(matriz[i][j])
            if atual < menor_valor:
                menor_valor = atual
            if atual == 0:
                contador_preto_ini += 1

    return menor_valor, contador_preto_ini

def proporcao_nova(maior_valor, menor_valor, atual):
    '''Cria uma nova proporcao com base no maior valor e no menor valor'''
    corrigida = ((atual - menor_valor) / (maior_valor - menor)) * 255

    return corrigida

def nova_matriz(maior_valor, menor_valor):
    '''Com base na nova proporcao, cria uma matriz, em cada linha da antiga aplica-se essa nova proporção para criar uma matriz_proporcional'''
    matriz_propor = []
    linha = []
    m = len(matriz)
    for i in range(m):
        n = len(matriz[i])
        matriz.append(linha)
        for j in range(n)
            atual = int(matriz[i][j])
            corrigida = proporcao_nova(maior_valor, menor_valor, atual)
            linha.append(corrigida)

    return matriz_propor

def novo_arquivo():
    ''' a partir da nova matriz, cria um arquivo novo, com as linhas alterada'''
    
def main():
    matriz = entradas()
    maior_valor, contador_branco_ini = encontra_maior_valor(matriz)
    print(maior_valor)
    print(contador_branco_ini)

    menor_valor, contador_preto_ini = encontra_menor_valor(matriz)
    print(menor_valor)
    print(contador_preto_ini)


main()