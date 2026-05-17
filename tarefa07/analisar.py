import binarizar

def entradas():
    arquivo_entrada = input()
    x, y, raio = input().split()
    n_medio = input()



def binarizaracao():
    matriz_propor, largura, limiar, fator, arquivo_entrada, arquivo_saida, branco, matriz, proporcao, escala, comentario = binarizar.normalizacao()
    x, y, raio = input().split()
    n_medio = input()

    matriz_largura = binarizar.contar_largura(matriz_propor, largura)

    matriz_menores = binarizar.contar_limiar(limiar, matriz_largura)

    matriz_binarizada = binarizar.montar_matriz_binarizada(matriz_propor, matriz_menores, largura, fator)

    return matriz_binarizada, x, y, raio, n_medio


binarizaracao()


def main():
    pass