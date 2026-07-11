def achar_maximo(lista_num, n):
    if n == 1:
        return lista_num[n - 1]
    else:
        maior = achar_maximo(lista_num, n - 1)
        if int(maior) > int(lista_num[n-1]):
            return maior
        else:
            return lista_num[n-1]

def main():
    numeros = input()
    lista_num = numeros.split(" ")

    n = len(lista_num)
    maior = achar_maximo(lista_num, n)
    print(maior)

main()