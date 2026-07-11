def achar_divisor(n, d):
    #usar algoritmo de euclides
    r = n % d
    if r == 0:
        return d
    else:
        return achar_divisor(d, r)

def main():
    numeros = input()
    list_num = numeros.split(" ")

    maximo_div = achar_divisor(int(list_num[0]), int(list_num[1]))
    print(maximo_div)
    

main()