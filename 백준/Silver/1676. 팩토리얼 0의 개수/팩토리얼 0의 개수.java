import java.io.*;
import java.math.BigInteger;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        String s = factorial(BigInteger.valueOf(n)).toString();

        int len = s.length();

        int i;
        for(i = 0; i < len; i++) {
            if(s.charAt(len - i - 1) != '0') {
                break;
            }
        }
        System.out.println(i); 
    }

    public static BigInteger factorial(BigInteger k) {
        if (k.equals(BigInteger.ONE) || k.equals(BigInteger.ZERO)) {
            return BigInteger.ONE;
        }
        return k.multiply(factorial(k.subtract(BigInteger.ONE)));
    }
}
