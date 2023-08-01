import java.util.Scanner;

public class emisorHamming {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese una trama en binario: ");
        String input = scanner.nextLine();

        // Verificar si la trama ingresada es válida (solo 0s y 1s)
        if (!input.matches("[01]+")) {
            System.out.println("Trama no válida. Ingrese solo 0s y 1s.");
            return;
        }

        // Calcular la cantidad de bits de paridad necesarios
        int r = calculateNumberOfParityBits(input.length());

        // Crear un array de caracteres que contenga la trama y los bits de paridad
        char[] hammingCode = generateHammingCode(input, r);

        System.out.println("El mensaje en binario con la informacion adicional es: ");

        System.out.println(hammingCode);
    }

    private static int calculateNumberOfParityBits(int dataLength) {
        int r = 1;

        // Usamos la fórmula de Hamming para calcular la cantidad de bits de paridad (r)
        while (Math.pow(2, r) < dataLength + r + 1) {
            r++;
        }

        return r;
    }

    private static char[] generateHammingCode(String input, int r) {
        int dataLength = input.length();
        int hammingCodeLength = dataLength + r;
        char[] hammingCode = new char[hammingCodeLength];
        int dataIndex = 0;
        int parityIndex = 0;

        // Llenar el array de hammingCode con "_", esto nos permite mantener los índices consistentes
        for (int i = 1; i <= hammingCodeLength; i++) { // Ajustamos la condición del for
            if (i == (1 << parityIndex)) {
                hammingCode[i - 1] = '_'; // Ajustamos el índice al asignar el valor
                parityIndex++;
            } else {
                // Agregar el bit de la trama original en la posición actual del índice
                hammingCode[i - 1] = input.charAt(dataIndex);
                dataIndex++;
            }
        }

        // Calcular los bits de paridad
        for (int i = 0; i < r; i++) {
            int bitPosition = 1 << i;
            int onesCount = 0;

            // Calcular la cantidad de 1s en cada secuencia de bits correspondiente a cada bit de paridad
            for (int j = bitPosition - 1; j < hammingCodeLength; j += 2 * bitPosition) {
                for (int k = j; k < j + bitPosition && k < hammingCodeLength; k++) {
                    if (hammingCode[k] == '1') {
                        onesCount++;
                    }
                }
            }

            // Establecer el bit de paridad en función del número de 1s
            hammingCode[bitPosition - 1] = (onesCount % 2 == 0) ? '0' : '1';
        }

        return hammingCode;
    }
}
