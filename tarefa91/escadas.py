import math
def escada():
    '''Divide o número por 10, o resto será o ultimo digito (guarda na memoria)
      divide de novo por 10 (guarda na memoria)
      Se a diferenca do modulo desses dois numeros for 1, eles são escadas
    '''
    digitos = int(input())
    for i in range(digitos): 
        numero = int(input())
        ultimo = numero % 10
        proximo = numero // 10
        if proximo > 10:
            while proximo > 10:
                p_ultimo = proximo % 10
                if ultimo - p_ultimo == 1 or p_ultimo - ultimo == 1:               
                    ultimo = p_ultimo
                    proximo = proximo // 10
                    continue
                else:
                    break
                        
        if numero == 1:
            print(f"{numero} é um escada")    
        elif ultimo - proximo == 1 or proximo - ultimo == 1:
            print(f"{numero} é um escada")
        else:
            print(f"{numero} não é um escada")

      
escada()

