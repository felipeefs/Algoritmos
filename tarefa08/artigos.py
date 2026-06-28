"""
-Com base no dados dos arquivos dos arquivos.json cria uma lista com dicionarios para cada id, em que as chaves serão: id, titulo, autores, palavra-chave, ano, referencias.
-Uma coleção que guarda as palavras chaves (para realizar as operações booleanas)
-Um dicionario para com os nomes dos autores (para verificar quantas vezes mencionadoss)
-Uma coleção para os IDs
-Uma coleção para as referencias aparecidas
-Cria um dicionario para adicionar palavra-chave (chave), e um conjunto de IDs (valor) 
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
    colecao.dic_chave = {}

    return colecao


def carregar_arquivo(colecao, nome_arquivo):
    # FIXME: carregue a lista de artigos lidos na sua coleção
    ...

    with open(nome_arquivo) as arquivo:
        lista_artigos = json.load(arquivo)

    #Adiciona todos os dicionarios na lista que esta       
    for dic in lista_artigos:
        colecao.lista_dic.append(dic) 

    #Adicona todas as palavras chaves em um conjunto
    for dic in colecao.lista_dic: 
        for i in dic["palavras-chave"]:
            if i not in colecao.conj_palavras:
                colecao.conj_palavras.add(i)

    #Adiciona cada autor em um dicionario especifico (para depois calcular suas ocorrencia)
    for dic in colecao.lista_dic:
        for i in dic["autores"]:
            if i not in colecao.dic_autores:
                colecao.dic_autores[i] = 0

    #Adiciona IDs em um conjunto
    for dic in colecao.lista_dic:
        if dic["id"] not in colecao.conj_id:
            colecao.conj_id.add(dic["id"])

    #Adiciona as referencias em um conjunto
    for dic in colecao.lista_dic:
        for i in dic["referencias"]:
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
        for dic in colecao.lista_dic:
            for i in dic["autores"]:
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
    for dic in colecao.lista_dic:
        if dic["id"] == id_artigo:
            return dic["titulo"]

def achar_id_artigo_atual(indice, colecao):
    '''Função criada para achar o id atual com base no indice em que o dicionario está na sua lista'''
    dic_atual = colecao.lista_dic[indice]
    id_artigo_atual = dic_atual["id"]

    return id_artigo_atual

def buscar_citacoes(colecao, id_artigo):
    '''A partir de id_artigo, descobre percorrendo a lista de dicionarios o id do dicionario (a partir de uma nova função) daquele que cita esse id_artigo'''
    lista_artigos = []
    for indice, dic in enumerate(colecao.lista_dic):
        for i in dic["referencias"]:
            if id_artigo == i:
                #descobrir id do artigo a partir do indice
                id_artigo_atual = achar_id_artigo_atual(indice, colecao)
                lista_artigos.append(id_artigo_atual)
    lista_artigos = sorted(lista_artigos)
                
    return lista_artigos
    

def buscar_palavras(colecao, consulta):
    '''Com base em um novo dicionario de palavras chaves; acha todos os ids de dicionarios que possuem essa palavra chave a adicona um conjunto desses ids nos valor do dicionario ---> depois faz a interceção para verificar quais ids possuem as mesmas palavras'''
    matriz_ids = []
    m = (len(consulta))
    for i in range(m):
        cont = 0
        n = len(consulta[i])
        for j in range(n):
            conj_ids = set()
            palavra = consulta[i][j]
            cont +=1

            for indice, dic in enumerate(colecao.lista_dic):
                for k in dic["palavras-chave"]:
                    if k == palavra:
                        id_atual = achar_id_artigo_atual(indice, colecao)
                        conj_ids.add(id_atual)
            colecao.dic_chave[palavra] = conj_ids

        if cont >= 0:
            matriz_ids.append(colecao.dic_chave[consulta[i][cont-2]] & colecao.dic_chave[consulta[i][cont-1]])
        else:
            matriz_ids.append(colecao.dic_chave[consulta[i][j]])

    #Como os conjuntos não podem ser acessador por indices, itera a matriz:
    ids_finais = []
    for lista in matriz_ids:
        for id in lista:
            if id not in ids_finais:
                ids_finais.append(id)
    return ids_finais
     

def inserir_artigo(colecao, id_artigo, titulo, autores, ano, palavras, referencias):
    '''Cria um dicionario vazio, vai adicionando os novos parametros nesse dicionario que será implementado na lista final de dicionario (colecao.lista_dic), se for adiciona returna True, se não for retorna False'''
    novo_dic = {}
    #verifica se o id já existe no dicionario
    for dic in colecao.lista_dic:
        if dic["id"] == id_artigo:
            return False

    #adiciona novo dicionario  
    novo_dic["id"] = id_artigo
    novo_dic["titulo"] = titulo
    novo_dic["autores"] = autores
    novo_dic["palavras-chaves"] = palavras
    novo_dic["ano"] = ano
    novo_dic["referencias"] = referencias
    colecao.lista_dic.append(novo_dic) #adicionando
    return True

def remover_artigo(colecao, id_artigo):
    '''Percorre a lista de dicionarios procurando o id_artigo, se ele estiver presente em um dicionario: remove esse dicionario e devolve True, se não devolve False'''

    for dic in colecao.lista_dic:
        if dic["id"] == id_artigo:
            del dic
            return True

    return False


def alterar_palavras(colecao, id_artigo, palavras_novas):
    '''Procura o dicionario na lista, em que o id_artigo corresponde ao id do dicionario e muda as palavras-chaves desse id'''
    for dic in colecao.lista_dic:
        if dic["id"] == id_artigo:
            dic["palavras-chaves"] = palavras_novas
            return True
    
    return False


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
    #print(numero_artigos)

    palavras = obter_palavras(colecao)
    #print(palavras)

    numero, principais_autores = obter_principais_autores(colecao)
    #print(numero)
    #print(principais_autores)

    referencias_orfas = obter_referencias_orfas(colecao)
    #print(referencias_orfas)

    lista_artigos = buscar_citacoes(colecao, 112342)
    lista_artigos= reversed(lista_artigos)
   

    consulta = [
        ["Algoritmos", "Inteligência Artificial"],
        ["Bancos de Dados"]
    ]

    buscar_palavras(colecao, consulta)

main()'''