def escada():
    digitos = int(input())
    divisor = 1
    divisor_num = 1
    final = 0
    soma_numeros = 0
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
        
        if numero == 1 or ultimo - proximo == 1 or proximo - ultimo == 1:
            # 1 será os escadas e 0 não escada
            final = final *10 + 1
            soma_numeros = soma_numeros * 10000000000000 + numero
        else:
            final = final * 10 + 0
            soma_numeros = soma_numeros * 10000000000000 + numero
        
    while divisor <= final:
        divisor = divisor * 10
    divisor = divisor // 10

    while divisor_num <= soma_numeros:
        divisor_num = divisor_num * 10000000000000
    divisor_num = divisor_num // 10000000000000

    while divisor > 0:
        escada = final // divisor
        impresso = soma_numeros // divisor_num

        if escada == 1:
            print(f"{impresso} é um escada")
        else:
            print(f"{impresso} não é um escada")

        final = final % divisor
        divisor = divisor // 10

        soma_numeros = soma_numeros % divisor_num
        divisor_num = divisor_num // 10000000000000
    # Sei que pode dar problema se o número for muito maior do que foi programado, o dividor_num não ia aguentar numeros muitos maiores
escada()

