def entradas():
    "Recebe o nome do arquivo e devolve uma lista para cada palavra, e recebe o a largura das linhas"
    texto = input()
    largura = int(input())
    texto_lista = []
    with open(texto) as arquivo:
        for linha in arquivo:
            texto_lista = linha.split()
    
    print(texto_lista)
    return texto_lista, largura

def separador(texto_lista):
    pass


entradas()