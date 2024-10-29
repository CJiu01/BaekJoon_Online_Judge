import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();
        int c = Integer.parseInt(br.readLine());

        int res1 = 0;
        int res2 = 0;


        res2 = Integer.parseInt(a+b) - c;
        res1 = Integer.parseInt(a) + Integer.parseInt(b) - c;

        System.out.println(res1);
        System.out.println(res2);
        
    }
}