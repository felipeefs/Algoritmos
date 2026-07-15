def frequencia_1(list_num, x, inicio, fim):
    #Caso básico(para a esquerda):
    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2

    if x == int(list_num[meio]):
        freq_1 = frequencia_1(list_num, x, inicio, meio - 1)
        if freq_1 == -1:
            return meio
        else:
            return freq_1

    #Caso geral
    elif x > int(list_num[meio]):
        return frequencia_1(list_num, x, inicio, meio - 1)
    else:
        return frequencia_1(list_num, x, meio + 1, fim)


def frequencia_2(list_num, x, inicio, fim):
    #Caso básico(para a direita):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if x == int(list_num[meio]):
        freq_2 = frequencia_2(list_num, x, meio + 1, fim)
        if freq_2 == -1:
            return meio
        else:
            return freq_2

    #Caso geral
    elif x > int(list_num[meio]):
        return frequencia_2(list_num, x, inicio, meio - 1)
    else:
        return frequencia_2(list_num, x, meio + 1, fim)


def main():
    numeros = input()
    list_num = numeros.split(" ")
    n = len(list_num)

    inicio = 0
    fim = n-1

    x = int(input())

    #Condições das frequencias
    freq_1 = frequencia_1(list_num, x, inicio, fim)
    if freq_1 == -1:
        print(0)
    else:
        freq_2 = frequencia_2(list_num, x, inicio, fim)
        frequencia = freq_2 - freq_1 + 1
        print(frequencia)
main()
