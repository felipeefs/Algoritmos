jogadores = []
lista_gols = []
lista_assis = []

entradas = True
while entradas:
    try:
        jogad, gols, assis = input().split()
        med_gols = float(gols)
        med_assis = float(assis)
        jogadores.append(jogad)
        lista_gols.append(med_gols)
        lista_assis.append(med_assis)
    except:
        entradas = False

maior_gol = 0
jogad_gol = 0
for i in range(len(lista_gols)):
    if lista_gols[maior_gol] < lista_gols[i]:
        maior_gol = i
        jogad_gol = i

maior_assis = -1 # -1 porque pode começar sendo igual no 0
jogad_assis = -1
for i in range(len(lista_assis)):          
    if i != maior_gol:
        if maior_assis == -1 or lista_assis[maior_assis] < lista_assis[i]:
            maior_assis = i
            jogad_assis = i
   

if lista_assis[maior_assis] > lista_gols[maior_gol]:
    print(f"Melhor dupla tem {jogadores[jogad_assis]} e {jogadores[jogad_gol]} com {lista_gols[maior_gol]} gols esperados.")
else: 
    print(f"Melhor dupla tem {jogadores[jogad_assis]} e {jogadores[jogad_gol]} com {lista_assis[maior_assis]} gols esperados.")
