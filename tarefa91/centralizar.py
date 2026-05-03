def entradas():
    "Recebe o nome do arquivo e devolve uma lista para cada palavra, e recebe o a largura das linhas"
    texto = input()
    largura = int(input())
    texto_lista = []
    linhas = []
    with open(texto) as arquivo:
        for linha in arquivo:
            linhas = linha.split()
            for itens in linhas:
                texto_lista.append(itens)
    
    return texto_lista, largura

def adição(texto_lista, largura):
    max = largura
    lista_grande = [""]
    tamanho = len(texto_lista)
    k = 0
    i = 0
    while i < len(lista_grande):
        while k < tamanho:
            if len(texto_lista[k]) < max:
                lista_grande[i] = lista_grande[i] + " " + texto_lista[k]             
                max -= len(texto_lista[k]) + 1 # precisa do 1 porque conta os espaços tbm
                k +=1
            else:
                #adicona itens vazios nas extremidades (a fazer)
                lista_grande.append("")
                max = largura
                break
        i += 1

    print(lista_grande)
    return lista_grande
    #depois apendd esse itens nos indices da lista grande


def espacos(lista_grande):
    for itens in lista_grande:
        print(itens)
    "Adiciona os espaços nas linhas necessarias"


texto_lista, largura = entradas()
lista_grande = adição(texto_lista, largura) 
espacos(lista_grande)
