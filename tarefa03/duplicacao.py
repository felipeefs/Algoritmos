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

#TEMPERATURA IDEAL E INDICE DE TEMPERATURA ALTA OU BAIXA
if tipo_bac == "Psicrófilos":
    temp_ide = 10
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2) / (temp_ide**2))

    if temp_amb < 0:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 20:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}")           
            
elif tipo_bac == "Mesófilos":
    temp_ide = 35
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2 ) / (temp_ide**2))

    if temp_amb < 20:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 50:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}")
            
elif tipo_bac == "Termófilo":
    temp_ide = 75
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2) / (temp_ide**2))

    if temp_amb < 50:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 100:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}")           

#CASO EXISTA OU NÃO CRESCIMENTO EXPONENCIAL
if taxa < 1:
        print("Não há crescimento exponencial, ajuste a temperatura.")
else:
        temp_dup = ((math.log10(2)) / math.log10(taxa))
        print (f"Tempo de duplicação: {temp_dup} minutos")
