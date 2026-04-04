jogos = int(input())
jogadores = []
lista_gols = []
lista_datas = []
j = 0 # lista atual
i = 0

while i < jogos:
    nome_jogar, data, gols = input().split()
    gols_num = int(gols)
    lista_gols.append(gols_num)
    jogadores.append(nome_jogar)
    lista_datas.append(data)
    i += 1

jogad_finais = input().split()

# MELHOR PLACAR RECENTE
data_atual = lista_datas[0] #data atual começa na primeira data
soma_data = 0
placar = 0
for i in range(jogos):
    if data_atual == lista_datas[i]:
        soma_data += lista_gols[i]
    else: #data atual e soma mudando 
        data_atual = lista_datas[i]
        soma_data = lista_gols[i]
        if soma_data > placar:
            placar = soma_data

if soma_data > placar:
    placar = soma_data
print(f"Melhor placar recente: {placar}")

# GOLS ESPERADOS
gols_esp = 0
jogad_atual = jogadores[0]
soma_gols = 0
divisao = 0
for i in range(jogos):
    if jogad_atual == jogadores[i]:
        soma_gols += lista_gols[i]
