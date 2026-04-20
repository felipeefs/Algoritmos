def arquivos_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    #AVISO: POR ENQUANTO SO ESTOU TRANFORMANDO ALGUNS ITENS EM LISTA AQUI, TALVEZ DEPOIS OUTROS PRECISEM VIRAR TAMBÉM
    arquivo_vendas = input()
    arquivo_logs = input()

    lista_hora_vendas = []
    lista_codigos = []
    lista_hora_logs = []

    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
            lista_hora_vendas.append(hora_ven)
            lista_codigos.append(codigo)

    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            lista_hora_logs.append(hora_logs)
            
    return lista_hora_vendas, lista_codigos, lista_hora_logs


def horas_vagas_func(lista_hora_vendas, lista_hora_logs):
    ''' Função para Criar uma lista com horas que estão em log, mas nao estao em vendas (horas_vagas)'''
    horas_vagas = []
    j = 0
    atual = lista_hora_logs[j]
    
    for i in lista_hora_vendas:
        if i == atual:
            atual = lista_hora_logs[j+1]
        else:
            horas_vagas.append(atual)

    return horas_vagas


def items_engracados(parametro):
    ''' 4- função para analisar cada item da lista_codigos e diz se podem existir itens engraçados entre eles. Adiciona esses engraçados em uma lista.'''

def listas_certas():
    ''' função para que cada item em horas_vagas consilia-lo a lista_codigos_engracados, ou seja essa função ira criar duas listas(lista_certa_hora e lista_certa_codigo) que terá essa hora e esse codigo – eles estarão no mesmo indice logo fica facil imprimir'''

def achar_brinquedo():
    '''função que verifica se a quantidade de carro ou de dinossauro (apos o item da lista horas_vagas, quando a hora for igual , pode-se usar uma comparação de horas pelo indice) caso diminuiu de uma lista logs para a outra, se diminuiu adiciona o outro item na lista_brinquedo'''

def imprime_resultado():
    '''7 -  Função para imprimir a lista_certa_hora lista_certa_codigo  e  lista_brinquedo'''


def main():
    '''Realizará todas as funções em ordem para que o problema seja resolvido'''

    lista_hora_vendas, lista_codigos, lista_hora_logs = arquivos_para_lista()
    print(lista_hora_vendas)
    print(lista_codigos)
    print(lista_hora_logs)

    horas_vagas = horas_vagas_func(lista_hora_vendas, lista_hora_logs)
    print(horas_vagas)


main()

