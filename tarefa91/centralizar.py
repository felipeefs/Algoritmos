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
    k = 0
    for i in range(len(lista_grande)):
        while max > 0:
            if len(texto_lista[k]) < max:
                lista_grande[i] = lista_grande[i] + " " + texto_lista[k]             
                max -= len(texto_lista[k])
                k +=1
            else:
                #adicona itens vazios nas extremidades (a fazer)
                lista_grande.append("")
                break

    print(lista_grande)
    return lista_grande
    #depois apendd esse itens nos indices da lista grande

texto_lista, largura = entradas()
adição(texto_lista, largura) 


def espacos():
    "Adiciona os espaços nas linhas necessarias"