def criar_colecao():
    n = int(input())

    dic = {}
    for n in range(n):
        banda, duracao = input().split(" ")
        dic[banda] = int(duracao)
        
    return n, dic

def main():
    n, dic = criar_colecao()
    print(n)
    print(dic)

main()