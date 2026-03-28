import math

tipo_bac = input()
duracao = float(input())
temp_amb = float(input())
satur = float(input()) #saturação = w
popu_ini = float(input()) #população inicial = n
satur_fin = satur
popu_fin = popu_ini
temporizador = 0

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


saturacao = True
while saturacao:
    print(f"Após {temporizador} minutos: {popu_fin}")

    popu_ini = popu_fin
    evaporacao = satur_fin * a #aw
    nutrientes = b * popu_ini # bn
    satur_fin = (evaporacao) - (nutrientes)
    popu_fin = ((popu_ini) * (satur_fin) *  (taxa))
    
    temporizador += 1
    duracao = duracao - 1
    
    if nutrientes > evaporacao:
        satur_fin = 0

    elif popu_fin < 1 or temporizador > duracao:
        saturacao = False

    

print ("População extinta.")



