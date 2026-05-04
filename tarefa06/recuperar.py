def arquivos_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    #AVISO: POR ENQUANTO SO ESTOU TRANFORMANDO ALGUNS ITENS EM LISTA AQUI, TALVEZ DEPOIS OUTROS PRECISEM VIRAR TAMBÉM
    arquivo_vendas = input()
    arquivo_logs = input()

    lista_codigos = []
    lista_hora_vendas = []
    lista_brinquedos_vendas = []
    lista_valor_vendas = []

    lista_hora_logs = []   
    lista_valor_logs = []
    lista_carros = []
    lista_dinos = []

    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
            lista_codigos.append(codigo)
            lista_hora_vendas.append(hora_ven)
            lista_brinquedos_vendas.append(brinq)
            lista_valor_vendas.append(valor_ven)
        
    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            lista_hora_logs.append(hora_logs)
            lista_valor_logs.append(valor_logs)
            lista_carros.append(carro)
            lista_dinos.append(dino)

                  
    return lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos, lista_codigos, lista_hora_vendas, lista_brinquedos_vendas, lista_valor_vendas


def logs_emVendas(lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos):
    "Função que vai pegar cada linhas de logs, analisar e ver qual é o horario, brinquedo e valor ---- > colocar em tuplas esse trio"
    #VALORES
    lista_precos = []
    #lista_precos.append(float(lista_valor_logs[0]))
    for i in range(len(lista_valor_logs) -1):
        preco = float(lista_valor_logs[i+1]) - float(lista_valor_logs[i])
        lista_precos.append(preco)

    #BRINQUEDOS
    lista_brinquedos = []
    for i in range(1,len(lista_carros)):
        if lista_carros[i] != lista_carros[i-1]:
            lista_brinquedos.append("carro")
        elif lista_dinos[i] != lista_dinos[i-1]:
            lista_brinquedos.append("dinossauro")
            
    #JUNTOS NA TUPLA
    lista_vendas_logs = []
    for i in range(len(lista_hora_logs) -1):
        venda = (lista_hora_logs[i+1], lista_brinquedos[i], lista_precos[i])
        lista_vendas_logs.append(venda)

    print(lista_vendas_logs)
    return lista_vendas_logs



def vendas_emTuplas(lista_hora_vendas, lista_brinquedos_vendas, lista_valor_vendas):
    "Vai pegar as linhas de vendas (exceto a primeira sempre valida) e coloca em uma lista de tuplas, para ser comparada depois na função que compara"
    #HORAS
    lista_horas = []
    for i in range(1, len(lista_hora_vendas)): #pula o primeiro porque sempre é valido
        lista_horas.append((lista_hora_vendas[i]))

    #Brinquedos
    lista_brinquedos = []
    for i in range(1, len(lista_brinquedos_vendas)):
        lista_brinquedos.append(lista_brinquedos_vendas[i])

    #PRECO DAS VENDAS
    precos = []
    for i in range(1, len(lista_valor_vendas)):
        precos.append(float(lista_valor_vendas[i]))

    #TUPLAS
    lista_vendas_tuplas = []
    for i in range(len(lista_hora_vendas) -1):
        vendas_tuplas = (lista_horas[i], lista_brinquedos[i], precos[i])
        lista_vendas_tuplas.append(vendas_tuplas)

    print(lista_vendas_tuplas)
    return lista_vendas_tuplas


def codigo_engracados(lista_codigos):
    "Acha todos os codigos engraçados entre dois numeros na lista de codigo e coloca em uma lista(de 1 em 1)"
    lista_codigosEngracados = []
    for i in range(1, len(lista_codigos)):
        atual = int(lista_codigos[i-1])
        proximo = int(lista_codigos[i])
        while atual < proximo:
            atual += 1
            codigo_str = str(atual)
            caracteres = len(codigo_str)
            metad_caracteres = caracteres // 2

            if codigo_str[0:metad_caracteres] == codigo_str[metad_caracteres:caracteres]:
                lista_codigosEngracados.append(atual)

    print(lista_codigosEngracados)   

def comparar(lista_vendas):
    "Irá comparar toda essa nova lista criada pelos logs e se ela for diferente das que estão em vendas, ganhará um codigo engrçado para ser impressa"
    



lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos, lista_codigos, lista_hora_vendas, lista_brinquedos_vendas, lista_valor_vendas = arquivos_para_lista()

logs_emVendas(lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos)

codigo_engracados(lista_codigos)

vendas_emTuplas(lista_hora_vendas, lista_brinquedos_vendas, lista_valor_vendas)
