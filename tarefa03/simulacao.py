import math

tipo_bac = input()
duracao = int(input())
temp_amb = float(input())
satur = float(input()) #saturação = w
popu_ini = int(input()) #população inicial = n
satur_fin = satur
popu_fin = popu_ini
temporizador = 0

r_max = 1.03526
a = 0.97
b = (1.6*(10**(-10)))

#TAXA AO DEPENDER DA BACTERIA
if tipo_bac == "Psicrófilos":
    temp_ide = 10

elif tipo_bac == "Mesófilos":
    temp_ide = 35

elif tipo_bac == "Termófilo":
    temp_ide = 75
taxa = r_max * math.e**(-((temp_amb - temp_ide)**2 ) / (temp_ide**2))


saturacao = True

while saturacao and temporizador <= duracao:
    popu_ini = popu_fin
    evaporacao = satur_fin * a #aw
    nutrientes = b * popu_ini # bn
    
    if satur_fin < 1 and satur_fin > 0:
        print(f"Após {temporizador} minutos: {popu_fin}")
        popu_fin = math.floor((popu_ini) * (satur_fin) *  (taxa)) #quando w < 1 ele entra na conta, se nao a gente faz a conta sem ele

        satur_fin = (evaporacao) - (nutrientes)

        if nutrientes > evaporacao:
            satur_fin = 0

        elif popu_fin < 1:
            saturacao = False
            print ("População extinta.")



    elif satur_fin >= 1:
        print(f"Após {temporizador} minutos: {popu_fin}")
        
        satur_fin = (evaporacao) - (nutrientes)
        popu_fin = math.floor((popu_ini) *  (taxa)) 

        if nutrientes > evaporacao:
            satur_fin = 0

        if popu_fin < 1:
            saturacao = False
            print ("População extinta.")


    temporizador += 1





