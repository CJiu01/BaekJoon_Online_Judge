import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            int min = Integer.MAX_VALUE;
            int max = Integer.MIN_VALUE;
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            for (int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (num < min) min = num;
                if (num > max) max = num;
            }
            sb.append(min).append(" ").append(max).append("\n");
        }
        System.out.print(sb);
    }
}