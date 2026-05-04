def arquivos_para_lista():
    '''1 – função que recebe os arquivos selecionados (vendas) e depois tranforma os itens em listas, separando cada item pelas virgulas com o split()
    '''
    #AVISO: POR ENQUANTO SO ESTOU TRANFORMANDO ALGUNS ITENS EM LISTA AQUI, TALVEZ DEPOIS OUTROS PRECISEM VIRAR TAMBÉM
    arquivo_vendas = input()
    arquivo_logs = input()

    with open(arquivo_vendas) as vendas:
        for linha in vendas:
            hora_ven, codigo, brinq, valor_ven = linha.split(",")
        
    with open(arquivo_logs) as logs:
        for linha in logs:
            hora_logs, dino, carro, valor_logs = linha.split(",")
            
            
    return 


def logs_emVendas():
    "Função que vai pegar cada linhas de logs, analisar e ver qual é o horario, brinquedo e valor"

def codigo_engracados():
    "Acha todos os codigos engraçados entre dois numeros na lista de codigo e coloca em uma lista(de 1 em 1)"

def comparar():
    "Irá comparar todas essa nova lista criada pelos logs e se ela for diferente das que estão em vendas, ganhará um codigo engrçado para ser impressa"
    

