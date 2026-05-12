import normalizar

def main():
    matriz, arquivo_entrada, arquivo_saida, escala, comentario, proporcao, branco = normalizar.entradas()

    maior_valor, contador_branco_ini = normalizar.encontra_maior_valor(matriz)

    menor_valor, contador_preto_ini = normalizar.encontra_menor_valor(matriz)

    matriz_propor = normalizar.nova_matriz(matriz, maior_valor,menor_valor)


main()
