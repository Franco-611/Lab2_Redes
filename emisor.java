import java.util.Random;
import java.util.Scanner;

public class emisor {

    public static String messageEncoding() {

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
            return null;
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
            hamming = interferenceFunction(hamming); // Linea que causa la interferencia de los datos
            return hamming;
        } else if (opcion == 2) {
            String crc = emisorCRC.calculateCRCWithInput(string_binario);
            System.out.println(crc);
            crc = interferenceFunction(crc); // Linea que causa la interferencia de los datos
            return crc;
        }

        return null;
    }

    // Funcion para simular la interefencia de los datos
    private static String interferenceFunction(String data){
        String newData = "";
        for(int i = 0; i < data.length(); i++){
            Random random = new Random();
            double randomValue = random.nextDouble();

            if(randomValue <= 0.5){
                if(data.charAt(i) == '1'){
                    newData = newData + "0";
                }
                else{
                    newData = newData + "1";
                }
            }
            else{
                newData = newData + data.charAt(i);
            }
        }
        return newData;
    }

}
