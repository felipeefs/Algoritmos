import math
def escada():
    '''Divide o número por 10, o resto será o ultimo digito (guarda na memoria)
      divide de novo por 10 (guarda na memoria)
      Se a diferenca do modulo desses dois numeros for 1, eles são escadas
    '''
    digitos = int(input())
    diferenca = True
    for i in range(digitos):
        numero = int(input())
        ultimo = numero % 10
        ant_ultimo = numero // 10
        #Mudar para a ant_numero ate ser menor que 10
        while diferenca:
            subtracao = ant_ultimo - ultimo
            subtracao2 = ultimo - ant_ultimo
            if subtracao == 1 or subtracao2 == 1:
                print(f"{numero} é um escada")
                break
            else:
                print(f"{numero} não é um escada")
                break
                 
escada()

