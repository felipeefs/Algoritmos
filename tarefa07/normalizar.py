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




entradas()