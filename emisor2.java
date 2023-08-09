import java.util.Random;

public class emisor2 {

    public static String messageEncoding2(int opcion, String mensaje, double probabilidadError) {

        System.out.println("Opcion: " + opcion);

        if (opcion == 1) {
            System.out.println("Has elegido el Algoritmo de Hamming.");
        } else if (opcion == 2) {
            System.out.println("Has elegido el Algoritmo de CRC32.");
        } else {
            System.out.println("Opcion invalida. Saliendo del programa.");
            return null;
        }

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
            hamming = interferenceFunction(hamming, probabilidadError);
            return hamming;
        } else if (opcion == 2) {
            String crc = emisorCRC.calculateCRCWithInput(string_binario);
            System.out.println(crc);
            crc = interferenceFunction(crc, probabilidadError);
            return crc;
        }

        return null;
    }

    // Funcion para simular la interefencia de los datos
    private static String interferenceFunction(String data, double probabilidadError) {
        String newData = "";
        for (int i = 0; i < data.length(); i++) {
            Random random = new Random();
            double randomValue = random.nextDouble();

            if (randomValue <= probabilidadError) {
                if (data.charAt(i) == '1') {
                    newData = newData + "0";
                } else {
                    newData = newData + "1";
                }
            } else {
                newData = newData + data.charAt(i);
            }
        }
        return newData;
    }

    // Resto del código de la clase
}
