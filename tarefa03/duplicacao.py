''' entradas: tipo de bacteria / valor da temperatura
1 - inserir tipo da bacteria
2 - inserir valor da temperatura
3- temperatura ideial = 0

se tipo == psicrófilos and temp == 10 and taxa
    mostrar
'''
import math

tipo_bac = input("Tipo de bactéria: ")
temp_amb = float(input("Temperatura ambiente: "))
r_max = 1.03526

#MUDANÇAS DA TEMPERATURA IDEAL DE CADA BACTERIA E CALCULO DA TAXA
if tipo_bac == "Psicrófilos":
    temp_ide = 10
    taxa = r_max **(-1 * (temp_amb - temp_ide)**2 / temp_ide**2)

    if temp_amb < 0:
            print("Temperatura muito baixa, aqueça a incubadora")
    elif temp_amb > 20:
            print("Temperatura muito alta, resfrie a incubadora")
            
elif tipo_bac == "Mesófilos":
    temp_ide = 35
    taxa = r_max **(-1 * (temp_amb - temp_ide)**2 / temp_ide**2)

elif tipo_bac == "Termófilo":
    temp_ide = 75
    taxa = r_max **(-1 * (temp_amb - temp_ide)**2 / temp_ide**2)


