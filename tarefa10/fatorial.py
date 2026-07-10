def fatorial(num):
    if num == 0:
        fat = 1
    
    else:
        m = num - 1 
        resultado = fatorial(m)
        fat = num * resultado
    
    return fat

def main():
    num = int(input())
    resposta = fatorial(num)
    print(resposta)

main()