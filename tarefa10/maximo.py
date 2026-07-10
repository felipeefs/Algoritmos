def achar_maximo(lista_num, n):
    if n == 1:
        return lista_num[n]
    elif n == 2:
        if lista_num[n] > lista_num[n+1]:
            return lista_num[n]
        else:
            return lista_num[n]
    else:
        maior = achar_maximo(lista_num[n-1], n-1)
        if maior > lista_num[n]:
            return maior
        else: 
            return lista_num[n]

def main():
    numeros = input()
    lista_num = numeros.split(" ")

    n = len(lista_num)
    maior = achar_maximo(lista_num, n)
    print(maior)

main()