import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int res = gcd(a,b);
        sb.append(res).append("\n").append(a*b/res);

        System.out.println(sb.toString());

        br.close();
    }

    private static int gcd(int a, int b) {
        if(b==0) {
            return a;
        }
        return gcd(b, a%b);
    }
}