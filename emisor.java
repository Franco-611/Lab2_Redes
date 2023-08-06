import java.util.Scanner;

public class emisor {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Bienvenido al programa emisor");
        System.out.println("Por favor, elige el algoritmo:");
        System.out.println("1. Algoritmo de Hamming");
        System.out.println("2. Algoritmo de CRC32");
        
        int opcion = scanner.nextInt();

        if (opcion == 1) {
            System.out.println("Has elegido el Algoritmo de Hamming.");
        } else if (opcion == 2) {
            System.out.println("Has elegido el Algoritmo de CRC32.");
        } else {
            System.out.println("Opción inválida. Saliendo del programa.");
            return;
        }

        scanner.nextLine(); // Consumir el salto de línea pendiente

        System.out.println("Por favor, ingresa el mensaje a codificar:");
        String mensaje = scanner.nextLine();

        // Codificar el mensaje a binario
        StringBuilder mensajeBinario = new StringBuilder();
        for (char c : mensaje.toCharArray()) {
            String binaryChar = Integer.toBinaryString(c);
            mensajeBinario.append(String.format("%8s", binaryChar).replace(' ', '0'));
        }

        String string_binario = mensajeBinario.toString();
        
        System.out.println("Mensaje codificado en binario: " + string_binario);

        if (opcion == 1) {
            String hamming = emisorHamming.calculateHamming(string_binario);
            System.out.println(hamming);
        } else if (opcion == 2) {
            String crc = emisorCRC.calculateCRCWithInput(string_binario);
            System.out.println(crc);
        }

        scanner.close();
    }
}
