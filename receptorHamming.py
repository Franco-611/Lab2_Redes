def calculate_parity_bits(data_length):
    r = 1
    while 2 ** r < data_length + r + 1:
        r += 1
    return r


def detect_error(hamming_code):
    r = calculate_parity_bits(len(hamming_code))
    r = len(hamming_code) - r
    paridad = []

    final = []

    for i in range(r):
        parity_bit = 2 ** i
        if parity_bit <= len(hamming_code):
            paridad.append(parity_bit)
            ones_count = 0
            temp = []
            for j in range(1, len(hamming_code) + 1):

                if (j & parity_bit) != 0:
                    ones_count += int(hamming_code[j - 1])
                    temp.append(hamming_code[j - 1])


            conteo = temp.count('1')

            if conteo % 2 == 0:
                final.append(0)
            else:
                final.append(1)


            hay_solo_ceros = True
            decimal_value = 0

            for elemento in final:
                if elemento != 0:
                    hay_solo_ceros = False
                decimal_value = decimal_value * 2 + elemento

    if hay_solo_ceros:
        return 0, paridad
    else:
        return decimal_value, paridad


def correct_error(hamming_code, error_bit):
    if error_bit == 0:
        return hamming_code

    hamming_code = list(hamming_code)
    if error_bit <= len(hamming_code):
        hamming_code[error_bit - 1] = "1" if hamming_code[error_bit - 1] == "0" else "0"
    return "".join(hamming_code)

def decode_hamming_to_data(hamming_code, paridad):
    r = calculate_parity_bits(len(hamming_code))
    r = len(hamming_code) - r
    data_bits = []
    
    for i in range(1, len(hamming_code) + 1):
        if i not in paridad:
            data_bits.append(hamming_code[i - 1])
    
    decoded_message = ''.join(data_bits)
    return decoded_message[::-1]


def receive_message(encoded_message):
    hamming_code = encoded_message.strip()
    error_bit, paridad= detect_error(hamming_code)
    return error_bit, paridad

if __name__ == "__main__":
    input_message = input("Ingrese el mensaje en binario con información adicional: ")
    receive_message(input_message)
