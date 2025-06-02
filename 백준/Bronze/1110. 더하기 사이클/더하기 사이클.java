import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        String N = br.readLine();
        String newNum = N;

        int cnt = 0;
        if(Integer.parseInt(newNum)<10) {
            newNum = 0+newNum;
        }
        while(true) {
            int a = Integer.parseInt(newNum.charAt(0)+"");
            int b = Integer.parseInt(newNum.charAt(1)+"");

            String plus = a+b+""; 
            newNum = b+ "" + plus.charAt(plus.length()-1);
            cnt += 1;

            if(N.equals(Integer.parseInt(newNum)+"")) break;
        }
        System.out.println(cnt);
    }
}