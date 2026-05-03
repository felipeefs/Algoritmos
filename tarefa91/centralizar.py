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
    
    print(texto_lista)
    return texto_lista, largura

def quebrador(texto_lista):
    "Função que analisa se uma palavra é quebradora, uma quebradora é uma palavra que tem dois pontos (:) nela, e após ela quebar, ela adiciona uma linha em branco embaixo"
    quebradores = []
    for item in texto_lista:
        if ":" in item:
            quebradores.append(item)

    return quebradores            

def adição(texto_lista, largura, quebradores):
    max = largura
    lista_grande = [""]
    tamanho = len(texto_lista)
    k = 0
    i = 0
    while i < len(lista_grande):
        while k < tamanho:
            if lista_grande[i] == "": #Para não começar com espaço inicial

                if len(texto_lista[k]) < max:
                    lista_grande[i] = lista_grande[i] + texto_lista[k]             
                    max -= len(texto_lista[k]) 
                    k +=1
                elif texto_lista[k] in quebradores and len(texto_lista[k]) > max:
                    lista_grande[i] = lista_grande[i] + texto_lista[k]             
                    lista_grande.append(" ")
                    lista_grande.append("")
                    max = largura
                    k +=1
                    i += 1
                    break
                else:
                    #adicona itens vazios nas extremidades (a fazer)
                    lista_grande.append("")
                    max = largura
                    break

            else:
                if len(texto_lista[k]) < max:
                    lista_grande[i] = lista_grande[i] + " " + texto_lista[k]             
                    max -= len(texto_lista[k]) + 1 # precisa do 1 porque conta os espaços tbm
                    k +=1
                elif texto_lista[k] in quebradores and len(texto_lista[k]) > max:
                    lista_grande[i] = lista_grande[i] + texto_lista[k]             
                    lista_grande.append(" ")
                    lista_grande.append("")
                    max = largura
                    k +=1
                    i += 1
                    break    
                else:
                    #adicona itens vazios nas extremidades (a fazer)
                    lista_grande.append("")
                    max = largura
                    break
        i += 1 # quando houver o espaço ia ter que ser i += 2

    print(lista_grande)
    return lista_grande
    #depois apendd esse itens nos indices da lista grande


def espacos(lista_grande):
    for itens in lista_grande:
        print(itens)
    "Adiciona os espaços nas linhas necessarias"


texto_lista, largura = entradas()
quebradores = quebrador(texto_lista)
lista_grande = adição(texto_lista, largura, quebradores) 
#espacos(lista_grande)

print(quebradores)
