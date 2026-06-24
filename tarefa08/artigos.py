"""
FIXME: Descreva AQUI sucinta e objetivamente como você irá representar a coleção
de artigos. Reveja as instruções no enunciado da tarefa. Todos os dados da
coleção de artigos são passados para as funções por meio de um único parâmetro
colecao. Se sua coleção precisar guardar tipos distintos de dados, então você
pode utilizar um objeto do tipo SimpleNamespace, como no exemplo abaixo.


-Com base no dados dos arquivos dos arquivos.json cria uma lista com dicionarios para cada id, em que as chaves serão: id, titulo, autores, palavra-chave, ano, referencias.
-Uma coleção que guarda as palavras chaves (para realizar as operações booleanas)
-Um dicionario para com os nomes dos autores (para verificar quantas vezes mencionadoss)
-Uma coleção para os IDs
-Uma coleção para as referencias aparecidas
"""

import json
from types import SimpleNamespace


def criar_colecao():
    colecao = SimpleNamespace()
    colecao.lista_dic = []
    colecao.conj_palavras = set()
    colecao.dic_autores = {}
    colecao.conj_id = set()
    colecao.conj_ref = set()

    print(colecao)
    return colecao


def obter_nome_artigo(colecao, id_artigo):

    
    pass


def carregar_arquivo(colecao, nome_arquivo):
    # FIXME: carregue a lista de artigos lidos na sua coleção
    ...

    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)

    #Adiciona todos os dicionarios na lista que esta       
    for item in lista_artigos:
        colecao.lista_dic.append(item) 

    #Adicona todas as palavras chaves em um conjunto
    for item in colecao.lista_dic: 
        for i in item["palavras-chave"]:
            if i not in colecao.conj_palavras:
                colecao.conj_palavras.add(i)

    #Adiciona cada autor em um dicionario especifico (para depois calcular suas ocorrencia)
    for item in colecao.lista_dic:
        for i in item["autores"]:
            if i not in colecao.dic_autores:
                colecao.dic_autores[i] = 0

    #Adiciona IDs em um conjunto
    for item in colecao.lista_dic:
        if item["id"] not in colecao.conj_id:
            colecao.conj_id.add(item["id"])

    #Adiciona as referencias em um conjunto
    for item in colecao.lista_dic:
        for i in item["referencias"]:
            if i not in colecao.conj_ref:
                colecao.conj_ref.add(i)
    

    print(colecao.lista_dic)
    print(colecao.conj_palavras)
    print(colecao.dic_autores)
    print(colecao.conj_id)
    print(colecao.conj_ref)


def obter_numero_artigos(colecao):
    '''Pega a lista de dicionarios, e descobre quantos elementos há nela, essa quantidade representa a quantidade de artigos'''
    numero_artigos = (len(colecao.lista_dic))

    return numero_artigos


def obter_palavras(colecao):
    '''A partir do conjunto de todas as palavras-chaves, as deixa em ordem alfabetica'''
    palavras = sorted(colecao.conj_palavras)

    return palavras


def obter_principais_autores(colecao):
    '''Como se fosse um histograma, a cada vez que o autor for citado, é somado 1 a sua multiplicidade'''
    dic_autores = colecao.dic_autores
    for autor, valor in dic_autores.items():
        print(autor)
        for item in colecao.lista_dic:
            for i in item["autores"]:
                if i == autor:
                    #print(i)
                    dic_autores[autor] += 1 #o valor de cada chave de autor recebe um cada vez que ele aparece
        
    print(dic_autores)


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

    numero_artigos= obter_numero_artigos(colecao)
    print(numero_artigos)

    palavras = obter_palavras(colecao)
    print(palavras)

    obter_principais_autores(colecao)

main()
