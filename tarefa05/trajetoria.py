import telemetria    
def main():
    v_max, leituras = telemetria.ler_trajetoria()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    reconstrucao = telemetria.reconstruir(leituras, corrompidas_detectadas)
    for t, x ,y in reconstrucao:
        print(f"{t:.0f} {x:.2f} {y:.2f}")
    
main()