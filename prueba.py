def calculate_crc32(message, n):
    POLYNOMIAL = 0b100000100110000010001110110110111
    CRC_LENGTH = 32
    crc32 = 0xFFFFFFFF
    for i in range(n):
        crc32 ^= message[i]
        for _ in range(8):
            if crc32 & 1:
                crc32 = (crc32 >> 1) ^ POLYNOMIAL
            else:
                crc32 >>= 1
    return crc32

def receive_message(input):
    CRC_LENGTH = 32
    n = len(input) - CRC_LENGTH
    print(n)
    message = [int(bit) for bit in input[:n]]
    received_crc = int(input[n:], 2)
    print(received_crc)

    print("Mensaje original:", ''.join(str(bit) for bit in message))
    print("Mensaje Original: 1101101010101111000010101111001111110000110010101010011001100101")
    print("CRC recibido:", bin(received_crc))

    calculated_crc = calculate_crc32(message, n)

    print("CRC calculado:", bin(calculated_crc))

    if received_crc == calculated_crc:
        print("Trama recibida:", ''.join(input))
    else:
        print("Se detectaron errores: La trama se descarta.")

if __name__ == "__main__":
    input_str = input("Ingrese la trama en binario concatenado con la información adicional: ").strip()
    print(len(input_str))
    receive_message(input_str)
