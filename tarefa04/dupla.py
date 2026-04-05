lista_gols = []
lista_assis = []

entradas = True
while entradas:
    try:
        jogad, gols, assis = input().split()
        med_gols = float(gols)
        med_assis = float(assis)
        lista_gols.append(med_gols)
        lista_assis.append(med_assis)
    except:
        entradas = False

maior_gol = lista_gols[0]
for i in lista_gols:
    if maior_gol < i:
        maior_gol = i
    else:
        maior_gol = maior_gol
print(maior_gol)

maior_assis = lista_assis[0]
for i in lista_assis:           #ARRUMAR ISSO PQ NAO PODE SER DO MESMO JOGADOR O MAIOR NUMERO
    if maior_assis < i:
        maior_assis = i
    else:
        maior_assis = maior_assis
print(maior_assis)


