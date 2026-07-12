def achar_propramacao(bandas,duracoes, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    ponto1 = 1
    ponto2 = 2

    '''dur_1 = 0
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

            menor_duracao = 10000
            print(dur_1, dur_2, dur_3)
            if dur_1 < dur_2 and dur_1 < dur_3 and dur_1 < menor_duracao and dur_1 != 0:
                menor_duracao = dur_1
            elif dur_2 < dur_1 and dur_2 < dur_3 and dur_2 < menor_duracao and dur_2 != 0:
                menor_duracao = dur_2
            elif dur_3 < dur_1 and dur_3 < dur_2 and dur_3 < menor_duracao and dur_3 != 0:
                menor_duracao = dur_3

            dur_1 = 0
            ponto1 += 1
            ponto2 = ponto1 + 1 #ponto2 nunca pode ficar antes do ponto1 
'''
    while ponto1 <= n-1:
        dur_1 = 0
        for item1 in duracoes[0:ponto1]:
            dur_1 += item1

        dur_2 = 0
        for item2 in duracoes[ponto1:ponto2]:
            dur_2 += item2

        dur_3 = 0
        for item3 in duracoes[ponto2: n]:
            dur_3 += item3

           
        menor_duracao = 10000
        print(dur_1, dur_2, dur_3)
        if dur_1 < dur_2 and dur_1 < dur_3 and dur_1 < menor_duracao and dur_1 != 0:
            menor_duracao = dur_1
        elif dur_2 < dur_1 and dur_2 < dur_3 and dur_2 < menor_duracao and dur_2 != 0:
            menor_duracao = dur_2           
        elif dur_3 < dur_1 and dur_3 < dur_2 and dur_3 < menor_duracao and dur_3 != 0:
            menor_duracao = dur_3
        
        ponto1 +=1
        ponto2 = ponto1 + 1




    print(dur_1, dur_2, dur_3, menor_duracao)

def criar_colecao():
    '''Cria uma lista, programacao, e adiciona um dicionario para cada banda com seu tempo de duração'''
    n = int(input())

    bandas = []
    duracoes = []
    for n in range(n):
        banda, menor_duracao = input().split(" ")        
        bandas.append(banda)
        duracoes.append(int(menor_duracao))
    return n, bandas, duracoes

def main():
    n, bandas, duracoes = criar_colecao()
    #print(n)
    #print(programacao)

    achar_propramacao(bandas, duracoes, n)

main()