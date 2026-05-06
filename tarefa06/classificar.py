def arquivos_para_lista():
    arquivo_vendas = input()

    lista_brinquedos = []
    lista_horas = []
    lista_valor_vendas = []

    with open(arquivo_vendas) as vendas:
            for linha in vendas:
                hora_ven, codigo, brinq, valor_ven = linha.split(",")
                lista_brinquedos.append(brinq)
                lista_horas.append(hora_ven)
                lista_valor_vendas.append(valor_ven)

    return lista_horas, lista_brinquedos, lista_valor_vendas


def horas_sem_minutos(lista_horas):
    '''Função que irá tirar todos os minutos das horas, em lista_horas. Por exemplo, deixa o 14h30 em 14h'''
    lista_sem_minutos = []
    for item in lista_horas:
        hora = item.split("h")
        lista_sem_minutos.append(hora[0])
        
    return lista_sem_minutos

def horas_sem_repeticao(lista_sem_minutos):
    '''Analisa todos os itens em lista sem minutos e adiona em uma lista sem repeti-las'''
    lista_sem_repeticao = []
    atual = lista_sem_minutos[0]
    lista_sem_repeticao.append(atual)

    for item in lista_sem_minutos:
        if item != atual:
            lista_sem_repeticao.append(item)
            atual = item

    return lista_sem_repeticao

def soma_valores(lista_sem_minutos, lista_sem_repeticao, lista_brinquedos, lista_valor_vendas):
    '''Analisa os itens em lista_sem_repeticao com o lista_sem_minutos, quando forem iguais, analisar o indice e ver se é um dino ou um carro. Se for dino adiciona em soma_dino, se carro: adiciona em soma_carro  ADICIONA EM UMA LISTA QUANDO TERMINAR DE SOMAR PARA CADA HORA.     Tambem, ao mesmo tempo que adiciona o valor na lista, adiciona o tempo em lista_carro_certa ou lista_dino_certa'''
    lista_somaDino = []
    lista_somaCarro = []
    lista_horaDino = []
    lista_horaCarro = []

    i = 0    
    for hora in lista_sem_repeticao:
        soma_dino = 0
        soma_carro = 0
        comparacao = True
        while comparacao and i != len(lista_sem_minutos):
            if hora == lista_sem_minutos[i]: 
                if lista_brinquedos[i] == "dinossauro":
                    soma_dino += float(lista_valor_vendas[i])
                else: 
                    soma_carro += float(lista_valor_vendas[i])
                    
            else:  
                comparacao = False
                break
            i +=1 #atualiza para o proximo se ainda forem iguais
        if soma_dino != 0: 
            lista_somaDino.append(soma_dino)
            lista_horaDino.append(hora)
        if soma_carro != 0: 
            lista_somaCarro.append(soma_carro)
            lista_horaCarro.append(hora)

    '''
    print(lista_horaCarro)
    print(lista_somaCarro)

    print(lista_horaDino)
    print(lista_somaDino)
    '''
    return lista_horaCarro, lista_somaCarro, lista_horaDino, lista_somaDino


def ordem_descrescente(lista_horaCarro, lista_somaCarro, lista_horaDino, lista_somaDino):
    "Pega as listas de valores e coloca em ordem descrescente de valores. Ao mesmo tempo que voce muda ela, voce muda as listas de lista_somaCarro e lista_somaDino----- fazer algo em relação ao empate tambem"

    for i in range(len(lista_somaCarro)):
        maior_indice = i
        for j in range(i, len(lista_somaCarro)):
            if lista_somaCarro[j] > lista_somaCarro[maior_indice]:
                maior_indice = j
        #Trocas Carros
        maior_item = lista_somaCarro[maior_indice]
        menor_item = lista_somaCarro[i]
        hora_certa = lista_horaCarro[maior_indice]
        hora_trocada = lista_horaCarro[i]

        lista_somaCarro[i] = maior_item            
        lista_horaCarro[i] = hora_certa
        lista_somaCarro[maior_indice] = menor_item
        lista_horaCarro[maior_indice] = hora_trocada

        
    for i in range(len(lista_somaDino)):
        maior_indice = i
        for j in range(i, len(lista_somaDino)):
            if lista_somaDino[j] > lista_somaDino[maior_indice]:
                maior_indice = j
        #Trocas Dinos
        maior_item = lista_somaDino[maior_indice]
        menor_item = lista_somaDino[i]
        hora_certa = lista_horaDino[maior_indice]
        hora_trocada = lista_horaDino[i]

        lista_somaDino[i] = maior_item            
        lista_horaDino[i] = hora_certa
        lista_somaDino[maior_indice] = menor_item
        lista_horaDino[maior_indice] = hora_trocada
        
    return lista_horaCarro, lista_somaCarro, lista_horaDino, lista_somaDino

def impressoes(lista_horaCarro_f, lista_somaCarro_f, lista_horaDino_f, lista_somaDino_f):
    pass

def main():
    lista_horas, lista_brinquedos, lista_valor_vendas = arquivos_para_lista()

    lista_sem_minutos = horas_sem_minutos(lista_horas)

    lista_sem_repeticao = horas_sem_repeticao(lista_sem_minutos)
                    
    lista_horaCarro, lista_somaCarro, lista_horaDino, lista_somaDino = soma_valores(lista_sem_minutos, lista_sem_repeticao, lista_brinquedos, lista_valor_vendas)

    lista_horaCarro_f, lista_somaCarro_f, lista_horaDino_f, lista_somaDino_f = ordem_descrescente(lista_horaCarro, lista_somaCarro, lista_horaDino, lista_somaDino)

    print("Carros:")
    for i in range(len(lista_somaCarro_f)):
        print(f"{lista_horaCarro_f[i]}h: {lista_somaCarro_f[i]:.2f}")

    print("\nDinossauros:")
    for i in range(len(lista_somaDino_f)):
        print(f"{lista_horaDino_f[i]}h: {lista_somaDino_f[i]:.2f}")

main()
