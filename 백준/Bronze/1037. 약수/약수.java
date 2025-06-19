import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] divisor = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        while(st.hasMoreTokens()) {
            int tmp = Integer.parseInt(st.nextToken());
            max = Integer.max(max, tmp);
            min = Integer.min(min, tmp);
        }
        System.out.println(min*max);
    }
}