import obd

baudrates = [9600, 38400, 57600, 115200]
ports = obd.scan_serial()

print("portas",ports)
obd.logger.setLevel(obd.logging.DEBUG)
for rate in baudrates:
    print(f"Tentando conectar com baudrate: {rate}")
    connection = obd.OBD("/dev/ttyACM0", baudrate=rate)
    
    if connection.is_connected():
        print(f"Conectado com sucesso com baudrate: {rate}")
        cmd = obd.commands.RPM 
        while True: 
            # Consulta o valor de RPM 
            response = connection.query(cmd)
            print(response)
        break
    else:
        print(f"Falha ao conectar com baudrate: {rate}")



