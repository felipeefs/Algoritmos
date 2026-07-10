def achar_maximo(lista_num, n):
    if n == 1:
        return lista_num[0]
    elif n == 2:
        if int(lista_num[n-1]) > int(lista_num[n-2]):
            return lista_num[n-1]
        else:
            return lista_num[n-2]
    else:
        meio = n//2
        max1 = achar_maximo(lista_num[0:meio], meio)
        max2 = achar_maximo(lista_num[0:meio+1], meio+1)

        if max1 > max2:
            return max1
        else:
            return max2
            
def main():
    numeros = input()
    lista_num = numeros.split(" ")
    print(lista_num)

    n = len(lista_num)
    maior = achar_maximo(lista_num, n)
    print(maior)

main()