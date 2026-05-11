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


    return matriz, arquivo_entrada, arquivo_saida, escala, comentario, proporcao, branco

def encontra_maior_valor(matriz):
    '''Acha o maior valor da matriz, o branco .Se achar um branco(255), adiciona no contador_branco_ini)'''
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
    '''Acha o menor valor da matriz, o preto. Se achar um preto (0), adiciona no contador_preto_ini'''
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
    corrigida = ((atual - menor_valor) / (maior_valor - menor_valor)) * 255
    corrigida = int(corrigida) #tira os decimais

    return corrigida

def nova_matriz(matriz, maior_valor, menor_valor):
    '''Com base na nova proporcao, cria uma matriz, em cada linha da antiga aplica-se essa nova proporção para criar uma matriz_proporcional'''
    matriz_propor = []
    m = len(matriz)
    for i in range(m):
        n = len(matriz[i])
        linha = []
        matriz_propor.append(linha)
        for j in range(n):
            atual = int(matriz[i][j])
            corrigida = proporcao_nova(maior_valor, menor_valor, atual)
            linha.append(corrigida)

    return matriz_propor

def acha_brancos_pretos(matriz_propor):
    ''' função que acha a quantidade de numeros brancos(255) e pretos(0) no matriz_propor com um contador'''
    contador_branco_fin = 0
    contador_preto_fin = 0
    m = len(matriz_propor)
    for i in range(m):
        n = len(matriz_propor[i])
        for j in range(n):
            atual = matriz_propor[i][j]
            if atual == 0:
                contador_preto_fin += 1
            if atual == 255: 
                contador_branco_fin += 1

    return contador_branco_fin, contador_preto_fin

def novo_arquivo(matriz_propor, arquivo_saida, escala, comentario, proporcao, branco):
    ''' a partir da nova matriz, cria um arquivo novo, com as linhas alterada'''
    with open(arquivo_saida, "w") as arquivo:
        arquivo.write(escala)
        arquivo.write("\n")
        arquivo.write(comentario)
        arquivo.write("\n")
        arquivo.write(proporcao)
        arquivo.write("\n")
        arquivo.write(branco)
        arquivo.write("\n")

        for lista in matriz_propor:
            for numero in lista:
                arquivo.write(str(numero) + " ")
            arquivo.write("\n")

    
def main():
    matriz, arquivo_entrada, arquivo_saida, escala, comentario, proporcao, branco = entradas()
    maior_valor, contador_branco_ini = encontra_maior_valor(matriz)

    menor_valor, contador_preto_ini = encontra_menor_valor(matriz)

    matriz_propor = nova_matriz(matriz, maior_valor,menor_valor)

    contador_branco_fin, contador_preto_fin = acha_brancos_pretos(matriz_propor)
    
    print(f"{arquivo_entrada}: {contador_preto_ini} pixels pretos e {contador_branco_ini} pixels brancos")
    print(f"{arquivo_saida}: {contador_preto_fin} pixels pretos e {contador_branco_fin} pixels brancos")

    novo_arquivo(matriz_propor, arquivo_saida, escala, comentario, proporcao, branco)

main()