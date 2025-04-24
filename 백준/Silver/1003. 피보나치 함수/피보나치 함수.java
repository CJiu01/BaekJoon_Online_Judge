import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] d = new int[41][3];

        for(int i=0; i<41; i++) {
            Arrays.fill(d[i], 0);
        }

        d[0][0] = 0;
        d[0][1] = 1;
        d[0][2] = 0;

        d[1][0] = 1;
        d[1][1] = 0;
        d[1][2] = 1;

        // DP
        // bottom-up
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++) {
            int num = Integer.parseInt(br.readLine());
            
            for(int j=2; j<=num; j++) {
                d[j][0] = d[j-1][0] + d[j-2][0];
                d[j][1] = d[j-1][1] + d[j-2][1];
                d[j][2] = d[j-1][2] + d[j-2][2];
            }
            sb.append(d[num][1] + " "+ d[num][2]).append("\n");
        }
        System.out.println(sb);
    }
}