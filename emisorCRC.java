import java.util.Scanner;

public class emisorCRC {

    private static final long POLYNOMIAL = 0xEDB88320L; // Modificar que el polinomio sea correcto
    private static final int CRC_LENGTH = 32; 

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la trama en binario: ");
        String input = scanner.nextLine().trim();

        if (input.length() <= CRC_LENGTH) {
            System.out.println("Error: La longitud de la trama debe ser mayor que 3.");
            return;
        }

        int[] message = new int[input.length()];
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (c == '0') {
                message[i] = 0;
            } else if (c == '1') {
                message[i] = 1;
            } else {
                System.out.println("Error: La trama debe contener solo 0s y 1s.");
                return;
            }
        }

        int n = input.length();
        int[] crc32 = calculateCRC32(message, n);
        int[] additionalInfo = new int[CRC_LENGTH];
        for (int i = 0; i < CRC_LENGTH; i++) {
            additionalInfo[i] = crc32[i];
        }

        int[] result = new int[n + CRC_LENGTH];
        System.arraycopy(message, 0, result, 0, n);
        System.arraycopy(additionalInfo, 0, result, n, CRC_LENGTH);

        System.out.print("Resultado (mensaje con la info adicional): ");
        for (int bit : result) {
            System.out.print(bit);
        }
    }

    private static int[] calculateCRC32(int[] message, int n) {
        int[] crc32 = new int[CRC_LENGTH];
        int register = 0x0;

        for (int i = 0; i < n; i++) {
            int msb = (register >> (CRC_LENGTH - 1)) & 1;

            register <<= 1;
            register |= message[i];

            if (msb == 1) {
                register ^= POLYNOMIAL;
            }
        }

        for (int i = 0; i < CRC_LENGTH; i++) {
            crc32[i] = (register >> ((CRC_LENGTH - 1) - i)) & 1;
        }

        return crc32;
    }
}
