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

print("Seleccione el tipo de codificación que desea utilizar:")
print("1. Hamming")
print("2. CRC")

respuesta = input("-> ")

trama = input("Ingrese la trama en binario concatenado con la información adicional: ").strip()

if respuesta == "1":
    error_bit, paridad = receive_message(trama)
    if error_bit == 0:
        print("No se detectaron errores. Trama recibida:")
        binary_message = decode_hamming_to_data(trama, paridad)
        print(binary_message)
        print(binary_to_ascii(binary_message))

        
    else:
        corrected_hamming_code = correct_error(trama, error_bit)
        print("Se detectaron errores y se corrigieron.")
        print(f"Posición del bit erróneo: {error_bit}")
        print("Trama corregida:")
        print(corrected_hamming_code)
elif respuesta == "2":
    calculated_crc, message = receive_messageC(trama)

    if 1 not in calculated_crc:
        print("Trama recibida sin errores:", ''.join(trama))
        print("Mensaje original:", ''.join(binary_to_ascii(message)))

    else:
        print("Se detectaron errores: La trama se descarta.")
