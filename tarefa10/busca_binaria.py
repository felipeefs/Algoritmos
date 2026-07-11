def frequencia(list_num, x, n):
    #Caso básico:
    if n == 1:
        if x == int(list_num[n-1]):
            return 1
        else:
            return 0
    #Caso geral
    else:
        freq = frequencia(list_num, x, n-1)
        if int(list_num[n-1]) == x:
            return freq + 1
        else:
            return freq

def main():
    numeros = input()
    list_num = numeros.split(" ")
    n = len(list_num)

    x = int(input())

    freq = frequencia(list_num, x, n)
    print(freq)

main()
