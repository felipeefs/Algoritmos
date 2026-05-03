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
                    if texto_lista[k] in quebradores: #Se existir itens com (:) ele quebra a linha
                        lista_grande.append(" ")
                        lista_grande.append("")
                        i += 1 # quando houver o espaço ia ter que ser i += 2
                        k +=1
                        max = max + 1 
                        break             
                    max -= len(texto_lista[k]) 
                    k +=1
               
                else:
                    lista_grande.append("")
                    max = largura
                    break

            else:
                if len(texto_lista[k]) < max:
                    lista_grande[i] = lista_grande[i] + " " + texto_lista[k]
                    if texto_lista[k] in quebradores: #Se existir itens com (:) ele quebra a linha
                        lista_grande.append(" ")
                        lista_grande.append("")
                        i += 1 # quando houver o espaço ia ter que ser i += 2
                        k +=1
                        max = max + 1
                        break
                    max -= len(texto_lista[k]) + 1 # precisa do 1 porque conta os espaços tbm
                    k +=1
   
                else:
                    lista_grande.append("")
                    max = largura
                    break
        i += 1 

    print(lista_grande)
    return lista_grande

def espacos(lista_grande, largura):
    '''Adiciona os espaços nas linhas necessarias'''
    for verso in lista_grande:
        if verso != " ":
            while len(verso) < largura:
                verso += " "
            




texto_lista, largura = entradas()
quebradores = quebrador(texto_lista)
lista_grande = adição(texto_lista, largura, quebradores) 
espacos(lista_grande, largura)

for item in lista_grande:
    print(item)
