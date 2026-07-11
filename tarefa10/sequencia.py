def sequencia(n, t):
    #Casos básicos
    if t[n] is None:
        if n == 1:
            t[n] = 1
        elif n == 2:
            t[n] = 2
        elif n == 3:
            t[n] = 3
        #Caso geral
        else:
            t[n] = sequencia(n-1, t) + (2 * sequencia(n-2, t)) + (3 * sequencia(n-3, t))

    return t[n]

def memorizacao(n):
    t = [None for i in range(n+1)] #Cria uma lista vazia para memoriação de elementos que ja foram descobertos (em que o primeiro item nunca é usado)
    return sequencia(n, t)

def main():
    n = int(input())
    saida = memorizacao(n)
    
    print(saida)

main()