jogos = int(input())
jogadores = []
lista_gols = []
lista_datas = []
lista_finais = []
i = 0

#ENTRADA DOS JOGADORES, DATAS E GOLS:
while i < jogos:
    nome_jogar, data, gols = input().split()
    gols_num = int(gols)
    lista_gols.append(gols_num)
    jogadores.append(nome_jogar)
    lista_datas.append(data)
    i += 1

lista_finais = input().split()

# MELHOR PLACAR RECENTE
data_atual = lista_datas[0] #data atual começa na primeira data
soma_data = 0
placar = 0
for i in range(jogos):
    if data_atual == lista_datas[i]:
        soma_data += lista_gols[i]
    else: #data atual e soma mudando
        if soma_data > placar:
            placar = soma_data
        data_atual = lista_datas[i]
        soma_data = lista_gols[i]
        
if soma_data > placar:
    placar = soma_data
print(f"Melhor placar recente: {placar}")

# GOLS ESPERADOS
gols_esp = 0
for jogad_finais in lista_finais:
    soma_gols = 0
    divisao = 0
    media = 0
    for i in range(jogos):
        if jogad_finais == jogadores[i]:
            soma_gols += lista_gols[i]
            divisao += 1 
    if divisao > 0:
        media = soma_gols / divisao
    else:
        media = 0
    gols_esp += media

print(f"Número de gols esperados: {gols_esp}")
