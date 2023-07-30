def calculate_crc3(message, n):
    POLYNOMIAL = 0b1001
    CRC_LENGTH = 3
    crc3 = [0] * CRC_LENGTH
    register = 0x0

    for i in range(n):
        msb = (register >> (CRC_LENGTH - 1)) & 1

        register <<= 1
        register |= message[i]

        if msb == 1:
            register ^= POLYNOMIAL

    for i in range(CRC_LENGTH):
        crc3[i] = (register >> ((CRC_LENGTH - 1) - i)) & 1

    return crc3

def receive_message(input):
    CRC_LENGTH = 3
    n = len(input) - CRC_LENGTH
    message = [int(bit) for bit in input[:n]]
    received_crc = [int(bit) for bit in input[n:]]

    calculated_crc = calculate_crc3(message, n)

    if received_crc == calculated_crc:
        print("Trama recibida sin errores:", ''.join(input))
    else:
        print("Se detectaron errores: La trama se descarta.")

if __name__ == "__main__":
    input_str = input("Ingrese la trama en binario concatenado con la información adicional: ").strip()

    receive_message(input_str)
