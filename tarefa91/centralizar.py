def entradas():
    "Recebe o nome do arquivo e devolve uma lista para cada palavra, e recebe o a largura das linhas"
    texto = input()
    largura = int(input())
    texto_lista = []
    with open(texto) as arquivo:
        for linha in arquivo:
            texto_lista = linha.split()
    
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
                max -= len(texto_lista[k])
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

texto_lista, largura = entradas()
adição(texto_lista, largura) 


def espacos():
    "Adiciona os espaços nas linhas necessarias"