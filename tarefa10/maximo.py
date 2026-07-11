def achar_maximo(lista_num, n):
    #Caso Basico (primeiro lista com um elemento, esse unico elemento é o maior)
    if n == 1:
        return lista_num[n - 1]
    #Caso Geral
    else:
        maior = achar_maximo(lista_num, n - 1)
        if int(maior) > int(lista_num[n-1]): #O ultimo da lista deve sempre ser comparado com o resto
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