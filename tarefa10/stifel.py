def fatorial(n):
    if n == 0:
        return 1
    else:
        m = n - 1
        solucao = fatorial(m)
        resultado = solucao * n

    return resultado

def memorizacao(n, k):
    #caso básico:
    if n == 1:
        return 1
    else:
        stifel = fatorial(n) // (fatorial(k)) * (fatorial(n-k))
    
    return stifel


def main():
    numeros = input()
    list_num = numeros.split(" ")

    resultado = memorizacao(int(list_num[0]), int(list_num[1]))
    print(resultado)
main()