def achar_divisor(list_num):
    #Caso básico (achar máximo divisor de UM número)
    for n in range(int(list_num[0]), 0, -1):
        if n % int(list_num[0]) == 0:
            return n
    



def main():
    numeros = input()
    list_num = numeros.split(" ")

    maximo_div = achar_divisor(list_num)
    print(maximo_div)
    
main()