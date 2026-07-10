def achar_maximo(lista_num, n):
    if n == 1:
        return lista_num[0]
    elif n == 2:
        if lista_num[n-1] > lista_num[n-2]:
            return lista_num[n-1]
        else: 
            return lista_num[n-2]
    else:
        maior = achar_maximo(lista_num[0:n-1], n-1)
        if maior > lista_num[n-1]:
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