def achar_maximo(lista_num, n):
    if n == 1:
        return lista_num[0]
    elif n == 2:
        if lista_num[n-1] > lista_num[n-2]:
            maior = lista_num[n-1]
        else:
            maior = lista_num[n-2]
        return maior
    else:
        maior_pri = achar_maximo(lista_num[0:n-(n//2)], (n//2))
        if maior_pri > lista_num[n-1]:
            return maior_pri
        else:
            return lista_num[n-1]
            
def main():
    numeros = input()
    lista_num = numeros.split(" ")

    n = len(lista_num)
    maior = achar_maximo(lista_num, n)
    print(maior)

main()