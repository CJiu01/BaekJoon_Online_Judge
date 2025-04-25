import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] dp = new int[N+1];
        dp[1] = 0;

        for(int i=2; i<=N; i++) {
            int[] arr = new int[3];
            Arrays.fill(arr, 1000000);
            if(i%3==0) {
                arr[0] = dp[i/3];
            }
            if(i%2==0) {
                arr[1] = dp[i/2];
            }
            arr[2] = dp[i-1];
            int min = Arrays.stream(arr).min().getAsInt();
            dp[i] = min+1;
        }
        System.out.println(dp[N]);
    }
}