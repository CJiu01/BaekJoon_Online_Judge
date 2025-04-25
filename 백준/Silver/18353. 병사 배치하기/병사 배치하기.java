import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> v = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        while(st.hasMoreTokens()) {
            v.add(Integer.parseInt(st.nextToken()));
        }
       
        Collections.reverse(v);

        int[] dp = new int[N];
        Arrays.fill(dp, 1);
        
        // LIS
        for(int i=1;i<N;i++) {
            for(int j=0;j<i;j++) {
                if(v.get(j)<v.get(i)) dp[i]=Math.max(dp[i], dp[j]+1);
            }
        }
        int res = Arrays.stream(dp).max().getAsInt();
        System.out.println(N-res);
    }
}