def sequencia(n, t):
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

def memorizacao(n):
    t = [None for i in range(n+1)] #Cria uma lista vazia para memoriação de elementos que ja foram descobertos (em que o primeiro item nunca é usado)
    return sequencia(n, t)

def main():
    n = int(input())
    saida = memorizacao(n)
    
    print(saida)

main()