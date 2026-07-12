def achar_propramacao(programacao, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    ponto1 = 1
    ponto2 = 2
    for bandas1 in programacao[0: ponto1]:
        for bandas2 in programacao[ponto1: ponto2]:
            print(bandas1["banda"])
            print(bandas2["banda"])


def criar_colecao():
    '''Cria uma lista, programacao, e adiciona um dicionario para cada banda com seu tempo de duração'''
    n = int(input())

    programacao = []
    for n in range(n):
        banda, duracao = input().split(" ")

        dic = {}
        dic["banda"] = banda
        dic["duracao"] = int(duracao)
        programacao.append(dic)
        
    return n, programacao

def main():
    n, programacao = criar_colecao()
    print(n)
    print(programacao)

    achar_propramacao(programacao, n)

main()