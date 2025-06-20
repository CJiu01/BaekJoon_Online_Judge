import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] arr;
    static int[] dp;

    public static void LIS() {
        for(int i=1; i<N; i++) {
            for(int j=0; j<i; j++) {
                if(arr[j]<arr[i]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N];
        Arrays.fill(dp, 1);

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        LIS();
        int res = Arrays.stream(dp).max().getAsInt();
        System.out.println(res);
    }
}