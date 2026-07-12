def achar_propramacao(programacao, n):
    '''Com base na quantidade de showns, testa os diferentes casos de possiveis showns a serem realizados, fixando um dois pontos na lista e descobrindo se tem menor duração possivel'''
    print(programacao)
        

def criar_colecao():
    '''Cria uma lista, programacao, e adiciona um dicionario para cada banda com seu tempo de duração'''
    n = int(input())

    programacao = {}
    for n in range(n):
        banda, duracao = input().split(" ")        
        programacao[banda] = duracao
    return n, programacao

def main():
    n, programacao = criar_colecao()
    #print(n)
    #print(programacao)

    achar_propramacao(programacao, n)

main()