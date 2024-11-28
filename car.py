import obd 
import time 
# Conecta ao OBD2 na porta /dev/ttyACM0 (ou outra porta, se necessário)
connection = obd.OBD("/dev/ttyACM0", baudrate=57600) 
if connection.is_connected():
    print("Conectado ao OBD2!") 
    # Comando para ler o RPM do motor 
    cmd = obd.commands.RPM 
    try:
        while True: 
            # Consulta o valor de RPM 
            response = connection.query(cmd)
            if response.is_null():
                print("RPM não disponível") 
            else: 
                print("RPM:", response.value)
            # Intervalo de tempo entre as leituras (em segundos)
        time.sleep(1) 
            # Ajuste o intervalo conforme necessário 
    except KeyboardInterrupt: 
        # Finaliza o loop ao pressionar Ctrl+C 
        print("Monitoramento de RPM interrompido") 
else: 
    print("Falha ao conectar ao OBD2.")