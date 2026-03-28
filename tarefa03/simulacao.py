import math

tipo_bac = input()
duracao = float(input())
temp_amb = float(input())
satur = float(input()) #saturação = w
popu_ini = float(input()) #população inicial = n

r_max = 1.03526
a = 0.97
b = (1.6 * (10**(-10)))
satur_ = 0 # w'

#TAXA AO DEPENDER DA BACTERIA
if tipo_bac == "Psicrófilos":
    temp_ide = 10

elif tipo_bac == "Mesófilos":
    temp_ide = 35

elif tipo_bac == "Termófilo":
    temp_ide = 75

taxa = r_max * math.exp(-((temp_amb - temp_ide)**2 ) / (temp_ide**2))
evaporacao = satur * a #aw
nutrientes = b * popu_ini # 


saturacao = True
while saturacao:
    satur_ = (evaporacao) - (nutrientes)
    while popu_ini > 0:
        popu_fin = popu_ini * satur *  taxa
    if nutrientes < evaporacao:
        saturacao = False
        satur = 0

print(satur)

