def divide_trama(trama, polinomio):
    # Asegurarse de que el polinomio no comience con 0
    while polinomio[0] == 0 and len(polinomio) > 1:
        polinomio.pop(0)

    # Realiza la división binaria
    for i in range(len(trama) - len(polinomio) + 1):
        if trama[i] == 1:
            for j in range(len(polinomio)):
                trama[i + j] ^= polinomio[j]

    return trama


def string_to_binary_list(s):
    return [int(bit) for bit in s]

def receive_messageC(input):
    CRC_LENGTH = 32
    n = len(input) - CRC_LENGTH
    message = [int(bit) for bit in input[:n]]
    received_crc = int(input[n:], 2)

    #print("Mensaje original:", ''.join(str(bit) for bit in message))

    polinomio_str = "100000100110000010001110110110111"
    #polinomio_str = "1001"

    # Convertir la trama y el polinomio en listas de dígitos binarios
    trama = string_to_binary_list(input)
    polinomio = string_to_binary_list(polinomio_str)

    calculated_crc = divide_trama(trama, polinomio)

    return calculated_crc, message
    # if 1 not in calculated_crc:
    #     print("Trama recibida sin errores:", ''.join(input))
    # else:
    #     print("Se detectaron errores: La trama se descarta.")

if __name__ == "__main__":
    input_str = input("Ingrese la trama en binario concatenado con la información adicional: ").strip()
    receive_messageC(input_str)
