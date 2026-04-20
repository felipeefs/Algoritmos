def vendas_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    lista_hora_vendas = []
    lista_codigos = []

    arquivo_vendas = input()
    arquivo_logs = input()
    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
            lista_hora_vendas.append(hora_ven)
            lista_codigos.append(codigo)

    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            
    return lista_hora_vendas, lista_codigos

def logs_para_lista():
    ''' 2- função que recebe os arquivos (logs) e transforma os itens em listas '''

def horas_vagas(lista_hora_vendas, lista_hora_logs):
    ''' Função para Criar uma lista com horas que estão em log, mas nao estao em vendas (horas_vagas)'''

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

    lista_hora_vendas, lista_codigos = vendas_para_lista()
    print(lista_hora_vendas)
    print(lista_codigos)

main()

