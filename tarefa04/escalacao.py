jogos = int(input())
jogadores = []
lista_gols = []
i = 0

while jogos >1:
    jogos -= 1
    nome_jogar, data, gols = input().split()
    gols_num = int(gols)
    lista_gols.append(gols_num)
    
    if jogos == 2:
        nome_jogar = input()

nome_jogar_fin = input()
# if nome_jogar == nome_jogar_fin:

# MELHOR PLACAR RECENTE:
melhor_placar = sum(lista_gols) // jogos
print(f"Melhor placar recente: {melhor_placar}")