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
    for i in texto_lista:
        j = 0
        while max < 0:
            if len(texto_lista[i]) < max:
                lista_grande[j] = lista_grande[j] + texto_lista[i]
                max -= len(texto_lista[i])
            else:
                #adicona itens vazios nas extremidades (a fazer)
                lista_grande.append("")
    print(lista_grande)
    return lista_grande
    #depois apendd esse itens nos indices da lista grande

texto_lista, largura = entradas()
adição(texto_lista, largura) 
