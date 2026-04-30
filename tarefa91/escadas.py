def escada():
    '''analisa se o numero é uma escada  
    1,
    10, 12,
    21, 23,
    aumenta 2 se (for impar), depois aumenta 9(se par)
    '''
    digitos = int(input())

    for i in range(digitos):
        numeros = int(input())
        num_escada = numeros

        if numeros == 1:
            print(f"{num_escada} é um escada")
             
        else:
            while numeros > 1:
                if numeros % 2 != 0:
                    numeros = numeros - 9
                elif numeros % 2 == 0:
                    numeros = numeros -2

            if numeros == 1:
                print(f"{num_escada} é um escada")
            else:
                print(f"{num_escada} não é um escada")

    return num_escada
      
escada()

