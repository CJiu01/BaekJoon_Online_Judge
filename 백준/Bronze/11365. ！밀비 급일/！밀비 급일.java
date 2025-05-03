import java.io.*;
import java.util.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    static void decrypt(String input) {

        String res = "";
        int len = input.length();
        for(int i=1; i<=len; i++) {
            res += input.charAt(len-i);
        }
        sb.append(res).append("\n");
    }

    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String input = br.readLine();
            if(input.equals("END")) break;

            decrypt(input);
        }
        System.out.print(sb);
    }
}