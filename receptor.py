from receptorCRC import *
from receptorHamming import *

def bits_to_letter(bits):
    bit_string = ''.join(str(bit) for bit in bits)
    return chr(int(bit_string, 2))

print("Seleccione el tipo de codificación que desea utilizar:")
print("1. Hamming")
print("2. CRC")

respuesta = input("-> ")

trama = input("Ingrese la trama en binario concatenado con la información adicional: ").strip()

if respuesta == "1":
    error_bit, paridad = receive_messageH(trama)
    if error_bit == 0:
        print("No se detectaron errores. Trama recibida:")
        print(trama)

        
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
        print("Mensaje original:", ''.join(bits_to_letter(message)))

    else:
        print("Se detectaron errores: La trama se descarta.")
