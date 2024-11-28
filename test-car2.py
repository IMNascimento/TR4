import obd
import time

# Conecte-se ao adaptador OBD2
connection = obd.OBD("/dev/ttyACM0")  # Altere para a porta correta, como /dev/ttyUSB0

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
            time.sleep(1)  # Ajuste o intervalo conforme necessário

    except KeyboardInterrupt:
        print("Monitoramento de RPM interrompido")

else:
    print("Falha ao conectar ao OBD2.")
