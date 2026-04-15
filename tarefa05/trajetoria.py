import telemetria
    
def main():
    v_max, leituras = telemetria.ler_trajetoria()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    recontrucao = telemetria.reconstruir(leituras, corrompidas_detectadas)
    print(recontrucao)
main()