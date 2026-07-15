def frequencia(list_num, x, inicio, fim):
    #Caso básico:
    if inicio > fim:
        return 0
    
    meio = (inicio + fim) // 2

    if x == int(list_num[meio]):
        return 1
        
    #Caso geral
    elif x > int(list_num[meio]):
        freq = frequencia(list_num, x, meio + 1, fim)
        return freq 
    else:
        freq = frequencia(list_num, x, inicio, meio - 1)
        return freq 


def main():
    numeros = input()
    list_num = numeros.split(" ")
    n = len(list_num)

    inicio = 0
    fim = n-1

    x = int(input())

    freq = frequencia(list_num, x, inicio, fim)
    print(freq)

main()
