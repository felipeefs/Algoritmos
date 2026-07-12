


def criar_colecao():
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

main()