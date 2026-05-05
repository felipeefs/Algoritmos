def arquivos_para_lista():
    arquivo_vendas = input()

    with open(arquivo_vendas) as vendas:
            for linha in vendas:
                hora_ven, codigo, brinq, valor_ven = linha.split(",")
                