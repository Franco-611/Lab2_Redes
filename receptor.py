from receptorCRC import *
from receptorHamming import *

def binary_to_ascii(binary_str):
    ascii_str = ""
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        decimal_value = int(byte, 2)
        ascii_char = chr(decimal_value)
        ascii_str += ascii_char

    return ascii_str

def messageDecoding(trama, algorithm_option):

    # print("Seleccione el tipo de codificación que desea utilizar:")
    # print("1. Hamming")
    # print("2. CRC")

    # respuesta = input("-> ")
    respuesta = algorithm_option

    print(trama)
    print(respuesta)
    if respuesta == 1:
        error_bit, paridad = receive_message(trama)
        if error_bit == 0:
            print("No se detectaron errores. Trama recibida:")
            binary_message = decode_hamming_to_data(trama, paridad)
            print("Mensaje original:", binary_to_ascii(binary_message))
            err = "nada"

            
        else:
            corrected_hamming_code = correct_error(trama, error_bit)
            print("Se detectaron errores y se corrigieron.")
            print(f"Posición del bit erróneo: {error_bit}")
            binary_message = decode_hamming_to_data(corrected_hamming_code, paridad)
            print("Mensaje original:", binary_to_ascii(binary_message))
            err = "hamming"
    elif respuesta == 2:
        calculated_crc, message = receive_messageC(trama)

        if 1 not in calculated_crc:
            print("Trama recibida sin errores:", ''.join(trama))
            print("Mensaje original:", ''.join(binary_to_ascii(message)))
            err = "nada"

        else:
            print("Se detectaron errores: La trama se descarta.")
            err = "crc"

    return err