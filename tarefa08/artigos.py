"""
FIXME: Descreva AQUI sucinta e objetivamente como você irá representar a coleção
de artigos. Reveja as instruções no enunciado da tarefa. Todos os dados da
coleção de artigos são passados para as funções por meio de um único parâmetro
colecao. Se sua coleção precisar guardar tipos distintos de dados, então você
pode utilizar um objeto do tipo SimpleNamespace, como no exemplo abaixo.


Com base no dados dos arquivos dos arquivos.json cria uma lista com dicionarios para cada id, em que as chaves serão: id, titulo, autores, palavra-chave, ano, referencias.

Quando for necessário buscar por palavras-chaves será necessário usar coleções (para realizar as operações booleanas)
"""

import json
from types import SimpleNamespace


def criar_colecao():
    # FIXME: modifique conforme a sua descrição acima
    #colecao = SimpleNamespace({'key': 0})
    colecao = SimpleNamespace()
    '''colecao.dado1 = ... #dado seria uma chave, e os ... seriam os valores
    colecao.dado2 = ...
    ...'''
    colecao.lista_dic = []
    colecao.conj_palavras = set()

    '''melhor criar uma coleçao para cada item la colecao. '''

    print(colecao)
    return colecao


def obter_nome_artigo(colecao, id_artigo):

    
    pass


def carregar_arquivo(colecao, nome_arquivo):
    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)
        
    #print(lista_artigos)
    # FIXME: carregue a lista de artigos lidos na sua coleção
    ...

    for item in lista_artigos:
        colecao.lista_dic.append(item) #adiciona todos os dicionarios na lista que esta na colecao

    for item in colecao.lista_dic: 
        for i in item["palavras-chave"]:
            if i not in colecao.conj_palavras:
                colecao.conj_palavras.add(i)

    print(colecao.lista_dic)
    print(colecao.conj_palavras)

def obter_numero_artigos(colecao):
    pass


def obter_palavras(colecao):
    pass


def obter_principais_autores(colecao):
    pass


def obter_referencias_orfas(colecao):
    pass


def buscar_citacoes(colecao, id_artigo):
    pass


def buscar_palavras(colecao, consulta):
    pass


def inserir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
    pass


def remover_artigo(colecao, id_artigo):
    pass


def alterar_palavras(colecao, id_artigo, palavras_novas):
    pass


def alterar_referencias(colecao, id_artigo, referencias_novas):
    pass


def gravar_arquivo(colecao, nome_arquivo):
    # FIXME: prepare uma lista de arquivos no formato do arquivo JSON
    lista_artigos = ...
    ...

    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista_artigos, arquivo, indent=2, ensure_ascii=False)


def main():
    colecao = criar_colecao()
    carregar_arquivo(colecao, "dados/artigos1.json")

main()
