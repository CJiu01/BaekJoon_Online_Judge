import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuffer sb = new StringBuffer();
        while(true) {
            String s = br.readLine();

            if(s.equals("0")) { break; }

            if(s.equals(new StringBuffer(s).reverse().toString())) {
                sb.append("yes");
            } else {
                sb.append("no");
            }

            sb.append("\n");

        }
        System.out.println(sb);
        
    }
}