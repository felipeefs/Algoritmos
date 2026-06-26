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
    colecao.dic_citacoes = {}

    return colecao


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
    
'''
    print(colecao.lista_dic)
    print(colecao.conj_palavras)
    print(colecao.dic_autores)
    print(colecao.conj_id)
    print(colecao.conj_ref)
'''

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
    for autor, valor in colecao.dic_autores.items():
        for item in colecao.lista_dic:
            for i in item["autores"]:
                if i == autor:
                    colecao.dic_autores[autor] += 1 #o valor de cada chave de autor recebe um cada vez que ele aparece

    #Devolve a chave o valor, no qual a dupla apresenta maior valor (em caso de empate mostrar em ordem alfabetica)
    numero = 0
    principais_autores = set()
    for autor, valor in colecao.dic_autores.items():
        if valor > numero:
            numero = valor

    for autor, valor in colecao.dic_autores.items():
        if valor == numero:
            principais_autores.add(autor)
    principais_autores = sorted(principais_autores)

    return numero, principais_autores


def obter_referencias_orfas(colecao):
    '''Como foi criado um conjunto para todos os IDs, e um conjunto para as referencias; pode-se verificar a diferenca entre elas para ver qual ref não aparece'''
    referencias_orfas = colecao.conj_ref - colecao.conj_id
    referencias_orfas = sorted(referencias_orfas)

    return referencias_orfas

    
def obter_nome_artigo(colecao, id_artigo):
    '''Funciona junto com a função buscar_citacoes'''
    for item in colecao.lista_dic:
        if item["id"] == id_artigo:
            return item["titulo"]


def buscar_citacoes(colecao, id_artigo):
    lista_artigos = []
    for indice, item in enumerate(colecao.lista_dic):
        for i in item["referencias"]:
            if id_artigo == i:
                #descobrir id do artigo a partir do indice
                dic_atual = colecao.lista_dic[indice]
                id_artigo_atual = dic_atual["id"]
                lista_artigos.append(id_artigo_atual)
    lista_artigos = sorted(lista_artigos)
    #colecao.dic_citacoes = sorted(colecao.dic_citacoes)      

    #citacoes_ordenadas = dict(reversed(colecao.dic_citacoes.items()))
    '''lista_artigos = []
    for chave, valor in sorted(colecao.dic_citacoes.items()):
        lista_artigos.append(f"{chave}: {valor}")
    print(lista_artigos)'''
    return lista_artigos
    

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

'''
def main():
    colecao = criar_colecao()
    carregar_arquivo(colecao, "dados/artigos1.json")

    numero_artigos= obter_numero_artigos(colecao)
    print(numero_artigos)

    palavras = obter_palavras(colecao)
    print(palavras)

    numero, principais_autores = obter_principais_autores(colecao)
    print(numero)
    print(principais_autores)

    referencias_orfas = obter_referencias_orfas(colecao)
    print(referencias_orfas)

    lista_artigos = buscar_citacoes(colecao, 112342)
    for i in lista_artigos:
        print(i)
main()'''