import java.util.Random;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class socketEmisor2 {

    public static String generateRandomMessage(int length) {
        String characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        Random random = new Random();
        StringBuilder sb = new StringBuilder(length);

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            sb.append(characters.charAt(index));
        }

        return sb.toString();
    }

    public static void main(String[] args) throws IOException, UnknownHostException, InterruptedException {
        if (args.length != 3) {
            System.out.println("Usage: java socketEmisor <messageLength> <errorProbability> <algorithmOption> <algorithm>");
            return;
        }

        int messageLength = Integer.parseInt(args[0]);
        double errorProbability = Double.parseDouble(args[1]);
        int algorithmOption = Integer.parseInt(args[2]);

        String HOST = "127.0.0.1";
        int PORT = 65432;

        OutputStreamWriter writer = null;

        System.out.println("Emisor Java Sockets\n");

        Socket socketCliente = new Socket(InetAddress.getByName(HOST), PORT);

        System.out.println("Enviando Data\n");
        writer = new OutputStreamWriter(socketCliente.getOutputStream());

        String message = generateRandomMessage(messageLength);

        System.out.println("Mensaje a codificar: " + message);
        
        String encodedMessage = emisor2.messageEncoding2(algorithmOption, message, errorProbability);

        String combinedValue = encodedMessage + "," + algorithmOption;

        writer.write(combinedValue);
        writer.flush();
        Thread.sleep(100);

        System.out.println("Liberando Sockets\n");
        writer.close();
        socketCliente.close();
    }
}
