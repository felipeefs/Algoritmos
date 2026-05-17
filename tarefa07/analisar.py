import binarizar

def entradas():
    arquivo_entrada = input()
    largura, limiar, fator = input().split()
    x, y, raio = input().split()
    n_medio = input()

    return arquivo_entrada, largura, limiar, fator

def binarizaracao(arquivo_entrada, largura, limiar, fator):
    matriz_propor, branco, matriz, proporcao, escala, comentario = binarizar.normalizacao(arquivo_entrada)

    matriz_largura = binarizar.contar_largura(matriz_propor, largura)

    matriz_menores = binarizar.contar_limiar(limiar, matriz_largura)

    matriz_binarizada = binarizar.montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator)

    return matriz_binarizada # Lembrar que todos os itens aqui estão como string


def main():
    arquivo_entrada, largura, limiar, fator = entradas()
    matriz_binarizada = binarizaracao(arquivo_entrada, largura, limiar, fator)

    print(matriz_binarizada)

main()
