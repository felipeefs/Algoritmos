def achar_propramacao(programacao, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    dur_palco1 = 0
    dur_palco2 = 0
    dur_palco3 = 0
    
    ponto1 = 1
    ponto2 = 2
    for bandas1 in programacao[0: ponto1]:
        dur_palco1 += bandas1["duracao"]
        for bandas2 in programacao[ponto1: ponto2]:
            dur_palco2 += bandas2["duracao"]
            for bandas3 in programacao[ponto2: n-1]:
                dur_palco3 += bandas3["duracao"]
    print(dur_palco1, dur_palco2, dur_palco3)


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