def arquivos_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    #AVISO: POR ENQUANTO SO ESTOU TRANFORMANDO ALGUNS ITENS EM LISTA AQUI, TALVEZ DEPOIS OUTROS PRECISEM VIRAR TAMBÉM
    arquivo_vendas = input()
    arquivo_logs = input()

    lista_hora_vendas = []
    lista_codigos = []

    lista_hora_logs = []
    lista_preco_logs = []
    lista_dino = []
    lista_carro = []


    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
            lista_hora_vendas.append(hora_ven)
            lista_codigos.append(codigo)
        
    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            lista_hora_logs.append(hora_logs)
            lista_preco_logs.append(valor_logs)
            lista_dino.append(dino)
            lista_carro.append(carro)
            
    return lista_hora_vendas, lista_codigos, lista_hora_logs, lista_preco_logs, lista_dino, lista_carro


def horas_vagas_func(lista_hora_vendas, lista_hora_logs):
    ''' Função para Criar uma lista com horas que estão em log, mas nao estao em vendas (horas_vagas)'''
    horas_vagas = []

    for item in lista_hora_logs:
        if item not in lista_hora_vendas:
            horas_vagas.append(item)
           
    return horas_vagas


def items_engracados(lista_codigos):
    ''' 4- função para analisar cada dois itens da lista_codigos e diz se podem existir itens engraçados entre eles. Adiciona esses engraçados em uma lista.'''
    lista_codigos_engracados = []
    quantidade = len(lista_codigos)
    u = 0
    k = 1
    for i in range(quantidade // 2):      
        atual = int(lista_codigos[i + u])
        proximo = int(lista_codigos[i + k])
        u += 2
        k += 1
        while atual < proximo:
            atual = int(atual)
            atual += 1
            codigo_str = str(atual)
            caracteres = len(codigo_str)
            metad_caracteres = caracteres // 2

            if codigo_str[0:metad_caracteres] == codigo_str[metad_caracteres:caracteres]:
                lista_codigos_engracados.append(atual)
                break
        
        

    '''
    i = 0
    atual = int(lista_codigos[i])
    ultimo = int(lista_codigos[len(lista_codigos)-1])
    lista_codigos_engracados = []

    while atual < ultimo:
        atual += 1
        codigo_str = str(atual)
        caracteres = len(codigo_str)
        metad_caracteres = caracteres // 2

        if codigo_str[0:metad_caracteres] == codigo_str[metad_caracteres:caracteres]:
                lista_codigos_engracados.append(atual)
                break

    for i in range(len(lista_codigos)-1):
        proximo = int(lista_codigos[i+1])
        atual_eng = lista_codigos_engracados[i]

        while atual_eng < proximo:
            atual_eng += 1
            codigo_str = str(atual_eng)
            caracteres = len(codigo_str)
            metad_caracteres = caracteres // 2

            if codigo_str[0:metad_caracteres] == codigo_str[metad_caracteres:caracteres]:
                lista_codigos_engracados.append(atual_eng)
                break
        

    
    i = 0
    j = 1
    atual = int(lista_codigos[i])
    proximo = int(lista_codigos[j])
    lista_codigos_engracados = []

    for i in range(len(lista_codigos)-1):
        atual = atual
        
        while atual < proximo:
            atual = int(atual)
            atual += 1
            codigo_str = str(atual)
            caracteres = len(codigo_str)
            metad_caracteres = caracteres // 2

            if codigo_str[0:metad_caracteres] == codigo_str[metad_caracteres:caracteres]:
                lista_codigos_engracados.append(atual)
                        
                break
      '''         
    return lista_codigos_engracados


def achar_brinquedo(lista_hora_logs, horas_vagas, lista_dino, lista_carro):
    '''função que verifica se a quantidade de carro ou de dinossauro (apos o item da lista horas_vagas, quando a hora for igual , pode-se usar uma comparação de horas pelo indice) caso diminuiu de uma lista logs para a outra, se diminuiu adiciona o outro item na lista_brinquedo'''

    lista_brinquedo = []
    for i in range(len(lista_hora_logs)):
        for item in horas_vagas:
            if item == lista_hora_logs[i]:
                "resolve para verificar os brinquedos"
                if lista_dino[i] != lista_dino[i-1]:
                    lista_brinquedo.append("dinossauro")
                elif lista_carro[i] != lista_carro[i-1]:
                    lista_brinquedo.append("carro")           
            else: 
                continue
    return lista_brinquedo

def valor_item(lista_preco_logs, horas_vagas, lista_hora_logs):
    "Função que irá descobrir o preço do item que foi apagado, verificando a hora vaga presente na lista_hora_logs, pelo mesmo indice do lista_hora_vagas, será necessário subtrair o lista_preco_logs[i] pelo lista_preco_logs[i-1]"

    precos_apagados = []

    for i in range(len(lista_hora_logs)):
        atual = float(lista_preco_logs[i])
        proximo = float(lista_preco_logs[i-1])
        for hora in horas_vagas:
            if hora == lista_hora_logs[i]:
                preco = atual - proximo
                precos_apagados.append(preco)

            else:
                continue 

    return precos_apagados

def imprime_resultado(horas_vagas, lista_codigos_engracados, precos_apagados, lista_brinquedo):
    '''7 -  Função para imprimir horas vagas, codigo_eng, brinquedo e valor (de cadad lista correspondente)'''
    

def main():
    '''Realizará todas as funções em ordem para que o problema seja resolvido'''

    lista_hora_vendas, lista_codigos, lista_hora_logs, lista_preco_logs, lista_dino, lista_carro = arquivos_para_lista()
    '''
    print(lista_hora_vendas)
    print(lista_codigos)
    print(lista_hora_logs)
    print(lista_preco_logs)
    '''
    horas_vagas = horas_vagas_func(lista_hora_vendas, lista_hora_logs)
    '''
    print(horas_vagas)
    '''

    lista_codigos_engracados = items_engracados(lista_codigos)
    '''
    print(lista_codigos_engracados)
    '''

    brinquedo = achar_brinquedo(lista_hora_logs, horas_vagas, lista_dino, lista_carro)
    '''
    print(brinquedo)
    '''

    apagados = valor_item(lista_preco_logs, horas_vagas, lista_hora_logs)
    '''
    print(apagados)
    '''
    # talvez seja necessario criar uma função, porque se eles não tiveram a mesma quantidade em tamanho irá dar problema
    for i in range(len(horas_vagas)):
        print(f"{horas_vagas[i]},{lista_codigos_engracados[i]},{brinquedo[i]},{apagados[i]:.2f}")
    
main()

