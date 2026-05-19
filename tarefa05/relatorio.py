import telemetria

def trajetoria():
    v_max, leituras = telemetria.ler_trajetoria()
    corrompidas_detectadas = telemetria.detectar_corrompidas(leituras, v_max)
    reconstrucao = telemetria.reconstruir(leituras, corrompidas_detectadas)
        