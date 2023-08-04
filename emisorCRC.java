import java.util.ArrayList;
import java.util.Scanner;

public class emisorCRC {

    private static final int[] CRC_32 = {
        1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1
    };

    private static final int CRC_LENGTH = 33;

    public static String calculateCRCWithInput(StringBuilder mensajeBinario) {
        ArrayList<Integer> message = new ArrayList<>();
        for (int i = 0; i < mensajeBinario.length(); i++) {
            char c = mensajeBinario.charAt(i);
            if (c == '0') {
                message.add(0);
            } else if (c == '1') {
                message.add(1);
            } else {
                System.out.println("Error: La trama debe contener solo 0s y 1s.");
                return null;
            }
        }

        int n = message.size();
        return calculateCRC(message, n);
    }

    private static String calculateCRC(ArrayList<Integer> message, int n) {
        int[] crcMessage = new int[message.size() + CRC_LENGTH];

        for (int i = 0; i < message.size(); i++) {
            crcMessage[i] = message.get(i);
        }

        for (int i = message.size(); i < crcMessage.length; i++) {
            crcMessage[i] = 0;
        }

        int[] tempCRC = new int[CRC_LENGTH];
        // Calcular el CRC tomando en cuenta solo los primeros CRC_LENGTH bits
        for (int i = 0; i < CRC_LENGTH; i++) {
            tempCRC[i] = crcMessage[i];
        }


        // Realizar la operación de división binaria y almacenar el resultado en tempCRC
        for (int i = 0; i < n; i++) {
            if (tempCRC[0] == 1) {

                for (int j = 0; j < CRC_LENGTH; j++) {
                    tempCRC[j] ^= CRC_32[j];
                }
            }

            
            // Desplazar a la izquierda los bits restantes
            for (int j = 0; j < CRC_LENGTH - 1; j++) {
                tempCRC[j] = tempCRC[j + 1];
            }
            tempCRC[CRC_LENGTH - 1] = crcMessage[i + CRC_LENGTH];


        }
        
        for (int i = n; i < crcMessage.length - CRC_LENGTH; i++) {
            crcMessage[i] = message.get(i - n);
        }
        for (int i = crcMessage.length - CRC_LENGTH, j = 0; i < crcMessage.length - 1; i++, j++) {
            crcMessage[i] = tempCRC[j];
        }

        int newLength = crcMessage.length - 1;

        int[] newCrcMessage = new int[newLength];

        for (int i = 0; i < newLength; i++) {
            newCrcMessage[i] = crcMessage[i];
        }

        crcMessage = newCrcMessage;

        String binary_message = "";
        for (int bit : crcMessage) {
            binary_message = binary_message + String.valueOf(bit);
        }

        return binary_message;
    }
}