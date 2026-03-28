import math

tipo_bac = input("Tipo de bactéria: ")
temp_amb = float(input("Temperatura ambiente: "))
r_max = 1.03526

#TEMPERATURA IDEAL E INDICE DE TEMPERATURA ALTA OU BAIXA:

#PSICRÓFILOS
if tipo_bac == "Psicrófilos":
    temp_ide = 10
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2) / (temp_ide**2))

    if temp_amb < 0:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 20:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}")
        if taxa < 1:  #CASO EXISTA OU NÃO CRESCIMENTO EXPONENCIAL
                print("Não há crescimento exponencial, ajuste a temperatura.")
        else:
              temp_dup = ((math.log10(2)) / math.log10(taxa))
              print (f"Tempo de duplicação: {temp_dup} minutos")        

 #MESÓFILOS           
elif tipo_bac == "Mesófilos":
    temp_ide = 35
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2 ) / (temp_ide**2))

    if temp_amb < 20:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 50:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}")
        if taxa < 1:  #CASO EXISTA OU NÃO CRESCIMENTO EXPONENCIAL
                print("Não há crescimento exponencial, ajuste a temperatura.")
        else:
              temp_dup = ((math.log10(2)) / math.log10(taxa))
              print (f"Tempo de duplicação: {temp_dup} minutos")  

 #TERMÓFILO           
elif tipo_bac == "Termófilo":
    temp_ide = 75
    taxa = r_max * math.exp(-((temp_amb - temp_ide)**2) / (temp_ide**2))

    if temp_amb < 50:
            print("Temperatura muito baixa, aqueça a incubadora.")
    elif temp_amb > 100:
            print("Temperatura muito alta, resfrie a incubadora.")
    else: 
        print(f"Taxa de crescimento por minuto: {taxa}") 
        if taxa < 1:  #CASO EXISTA OU NÃO CRESCIMENTO EXPONENCIAL
                print("Não há crescimento exponencial, ajuste a temperatura.")
        else:
              temp_dup = ((math.log10(2)) / math.log10(taxa))
              print (f"Tempo de duplicação: {temp_dup} minutos")  
