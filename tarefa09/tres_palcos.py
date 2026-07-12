def achar_propramacao(bandas,duracoes, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    print(bandas)
    print(duracoes)

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