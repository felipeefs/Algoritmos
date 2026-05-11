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
    '''Acha o maior valor da matriz, o branco .Se achar um branco(255), adiciona no contador_branco)'''
    contador_branco = 0
    maior_valor = int(matriz[0][0]) # adiciona o primeiro valor com base, para passar nos loops e se mudado
    m = len(matriz)
    for i in range(m):
        n =  len(matriz[i])
        for j in range(n):
            j = int(j)
            if j > maior_valor:
                maior_valor = j

    return maior_valor

def encontra_menor_valor(matriz):
    '''Acha o menor valor da matriz, o preto. Se achar um preto (0), adiciona no contador_preto'''
    contador_preto = 0

def proporcao_nova():
    '''Cria uma nova proporcao com base no maior valor e no menor valor'''

def nova_matriz():
    '''Com base na nova proporcao, altera a matriz, em cada livra aplica-se essa nova proporção e substitui pela linha antiga'''

def novo_arquivo():
    ''' a partir da nova matriz, cria um arquivo novo, com as linhas alterada'''
    
def main():
    matriz = entradas()
    maior_valor = encontra_maior_valor(matriz)
    print(maior_valor)


main()