import java.util.Scanner;

public class XOR {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Introduce un texto: ");
        String texto = scanner.nextLine();
        String textoBinario = textoABinario(texto);
        System.out.println("El texto en binario es: " + textoBinario);

        System.out.print("Introduce una clave: ");
        String clave = scanner.nextLine();
        String claveBinario = textoABinario(clave);
        System.out.println("La clave en binario es: " + claveBinario);

        String textoCifradoBinario = cifrarTexto(textoBinario, claveBinario);
        System.out.println("El texto cifrado en binario es: " + textoCifradoBinario);

        String textoCifrado = binarioATexto(textoCifradoBinario);
        System.out.println("El texto cifrado es: " + textoCifrado);
    }
    public static String textoABinario(String texto) {
        StringBuilder binario = new StringBuilder();
        for (char caracter : texto.toCharArray()) {
            String binarioCaracter = Integer.toBinaryString(caracter);
            binarioCaracter = String.format("%8s", binarioCaracter).replaceAll(" ", "0");
            binario.append(binarioCaracter).append(" ");
        }
        return binario.toString();
    }
    public static String cifrarTexto(String texto, String clave) {
        String[] bloquesTexto = texto.split(" ");
        String[] bloquesClave = clave.split(" ");
        StringBuilder cifrado = new StringBuilder();
        for (int i = 0; i < bloquesTexto.length; i++) {
            int textoBinario = Integer.parseInt(bloquesTexto[i], 2);
            int claveBinario = Integer.parseInt(bloquesClave[i % bloquesClave.length], 2);
            int resultadoXOR = textoBinario ^ claveBinario;
            char caracter = (char) resultadoXOR;
            cifrado.append(Integer.toBinaryString(caracter)).append(" ");
        }
        return cifrado.toString();
    }
    public static String binarioATexto(String binario) {
        StringBuilder texto = new StringBuilder();
        String[] bloquesBinarios = binario.split(" ");
        for (String bloque : bloquesBinarios) {
            int numero = Integer.parseInt(bloque, 2);
            char caracter = (char) numero;
            texto.append(Character.toString(caracter));
        }
        return texto.toString();
    }
}