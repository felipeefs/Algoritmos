def achar_propramacao(bandas,duracoes, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    ponto1 = 1
    ponto2 = 2

    dur_1 = 0
    while ponto1 <= n - 1:
        for item1 in duracoes[0:ponto1]:
            #print(item1)
            dur_2 = 0
            dur_3 = 0
            dur_1 += item1
            for item2 in duracoes[ponto1:ponto2]:
                dur_2 += item2
                for item3 in duracoes[ponto2:n+1]:
                    dur_3 += item3

                    duracao = 10000
                    print(dur_1)
                    if dur_1 < dur_2 and dur_1 < dur_3 and dur_1 < duracao and dur_1 != 0:
                        duracao = dur_1
                    elif dur_2 < dur_1 and dur_2 < dur_3 and dur_2 < duracao and dur_2 != 0:
                        duracao = dur_2
                    elif dur_3 < dur_1 and dur_3 < dur_2 and dur_3 < duracao and dur_3 != 0:
                        duracao = dur_3

            dur_1 = 0
            ponto1 += 1
            ponto2 = ponto1 + 1 #ponto2 nunca pode ficar antes do ponto1 

    print(dur_1, dur_2, dur_3, duracao)

def criar_colecao():
    '''Cria uma lista, programacao, e adiciona um dicionario para cada banda com seu tempo de duração'''
    n = int(input())

    bandas = []
    duracoes = []
    for n in range(n):
        banda, duracao = input().split(" ")        
        bandas.append(banda)
        duracoes.append(int(duracao))
    return n, bandas, duracoes

def main():
    n, bandas, duracoes = criar_colecao()
    #print(n)
    #print(programacao)

    achar_propramacao(bandas, duracoes, n)

main()