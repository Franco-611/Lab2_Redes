import socket
import receptor

HOST = "127.0.0.1"  # IP, capa de Red. 127.0.0.1 es localhost
PORT = 65432        # Puerto, capa de Transporte
errHamming = 0
errCRC = 0
er = 0


# AF_INET especifica IPv4,
#   tambien hay AF_UNIX para unix sockets y AF_INET6
# SOCK_STREAM especifica TCP,
#   tambien hay SOCK_DGRAM para UDP y otros...
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #bind reserva/asigna tal socket a una IP:puerto especifica
    s.bind((HOST, PORT))
    s.listen()
    while True:
        #accept() bloquea y deja esperando
        conn, addr = s.accept()
        with conn:
            print(f"Conexion Entrante del proceso {addr}")
            while True: #en caso se envien mas de 1024 bytes
                #recibir 1024 bytes
                data = conn.recv(1024)
                if not data:
                    break   #ya se recibio todo
                data = str(data)

                decoded_data = data[2:len(data) - 1]
                values = decoded_data.split(',')

                message = values[0]  
                algorithm_option = int(values[1])

                err = receptor.messageDecoding(message, algorithm_option)
                with open('errores.txt', 'a') as archivo:
                    if err == "hamming":
                        archivo.write("Error Hamming\n")
                    elif err == "crc":
                        archivo.write("Error CRC\n")
                    elif err == "nada":
                        archivo.write("No error\n")

                # print(f"Recibidoo: \n{data!r}\n{data!s}\n{data!a}") #!r !s !a, repr() str() ascii()
                ##echo
                #conn.sendall(data)
