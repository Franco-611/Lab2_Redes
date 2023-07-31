def calculate_parity_bits(data_length):
    r = 1
    while 2 ** r < data_length + r + 1:
        r += 1
    return r


def is_power_of_two(n):
    return n & (n - 1) == 0


def detect_error(hamming_code):
    error_bit = 0
    r = calculate_parity_bits(len(hamming_code))
    r = len(hamming_code) - r

    for i in range(r):
        print(i)
        parity_bit = 2 ** i
        if parity_bit <= len(hamming_code):
            ones_count = sum(
                int(hamming_code[j - 1]) for j in range(1, len(hamming_code) + 1) if (j & parity_bit) != 0
            )
            if ones_count % 2 != int(hamming_code[parity_bit - 1]):
                error_bit += parity_bit

    return error_bit


def correct_error(hamming_code, error_bit):
    if error_bit == 0:
        return hamming_code

    hamming_code = list(hamming_code)
    if error_bit <= len(hamming_code):
        hamming_code[error_bit - 1] = "1" if hamming_code[error_bit - 1] == "0" else "0"
    return "".join(hamming_code)


def generate_hamming_code(data, r):
    hamming_code = ["0"] * (len(data) + r)
    data_index, parity_index = 0, 0

    for i in range(1, len(hamming_code) + 1):
        if is_power_of_two(i):
            hamming_code[i - 1] = "_"
            parity_index += 1
        else:
            hamming_code[i - 1] = data[data_index]
            data_index += 1

    for i in range(r):
        parity_bit = 2 ** i
        for j in range(1, len(hamming_code) + 1):
            if j & parity_bit:
                if hamming_code[j - 1] != "_":
                    hamming_code[parity_bit - 1] = str(
                        (int(hamming_code[parity_bit - 1]) + int(hamming_code[j - 1])) % 2
                    )

    return "".join(hamming_code)


def receive_message(encoded_message):
    hamming_code = encoded_message.strip()
    error_bit = detect_error(hamming_code)

    if error_bit == 0:
        print("No se detectaron errores. Trama recibida:")
        print(hamming_code)
    else:
        corrected_hamming_code = correct_error(hamming_code, error_bit)
        print("Se detectaron errores y se corrigieron.")
        print(f"Posición del bit erróneo: {error_bit}")
        print("Trama corregida:")
        print(corrected_hamming_code)


if __name__ == "__main__":
    input_message = input("Ingrese el mensaje en binario con información adicional: ")
    receive_message(input_message)
