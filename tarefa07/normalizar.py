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

def maior_valor():
    '''Acha o maior valor da matriz'''

def menor_valor():
    '''Acha o menor valor da matriz'''

def proporcao_nova():
    '''Cria uma nova proporcao com base no maior valor e no menor valor'''

def nova_matriz():
    '''Com base na nova proporcao, altera a matriz, em cada livra aplica-se essa nova proporção e substitui pela linha antiga'''

def novo_arquivo():
    ''' a partir da nova matriz, cria um arquivo novo, com as linhas alterada'''
    
def main():
    pass



entradas()