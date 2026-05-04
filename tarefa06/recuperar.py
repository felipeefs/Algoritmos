def arquivos_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    #AVISO: POR ENQUANTO SO ESTOU TRANFORMANDO ALGUNS ITENS EM LISTA AQUI, TALVEZ DEPOIS OUTROS PRECISEM VIRAR TAMBÉM
    arquivo_vendas = input()
    arquivo_logs = input()

    lista_hora_logs = []   
    lista_valor_logs = []
    lista_carros = []
    lista_dinos = []

    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
        
    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            lista_hora_logs.append(hora_logs)
            lista_valor_logs.append(valor_logs)
            lista_carros.append(carro)
            lista_dinos.append(dino)

                  
    return lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos


def logs_emVendas(lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos):
    "Função que vai pegar cada linhas de logs, analisar e ver qual é o horario, brinquedo e valor ---- > colocar em tuplas esse trio"
    #VALORES
    lista_precos = []
    lista_precos.append(float(lista_valor_logs[0])) # o primerio sempre valido
    for i in range(len(lista_valor_logs) -1):
        preco = float(lista_valor_logs[i+1]) - float(lista_valor_logs[i])
        lista_precos.append(preco)

    #BRINQUEDOS
    lista_brinquedos = []
    

    print(lista_precos)


def codigo_engracados():
    "Acha todos os codigos engraçados entre dois numeros na lista de codigo e coloca em uma lista(de 1 em 1)"

def comparar():
    "Irá comparar todas essa nova lista criada pelos logs e se ela for diferente das que estão em vendas, ganhará um codigo engrçado para ser impressa"

lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos = arquivos_para_lista()
logs_emVendas(lista_hora_logs, lista_valor_logs, lista_carros, lista_dinos)
