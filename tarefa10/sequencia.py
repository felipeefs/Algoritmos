def sequencia(n):
    #Casos básicos
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    #Caso geral
    else:
        return sequencia(n-1) + (2 * sequencia(n-2)) + (3* sequencia(n-3))


def main():
    n = int(input())
    saida = sequencia(n)
    print(saida)

main()