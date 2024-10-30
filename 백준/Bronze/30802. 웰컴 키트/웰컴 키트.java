import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

       int n = Integer.parseInt(br.readLine());
        
        String input = br.readLine();
        int[] arr = Arrays.stream(input.split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        int T = 0;
        
        for(int i=0; i<arr.length; i++) {
            T += arr[i]/t + (arr[i]%t == 0 ? 0 : 1);
        }
        System.out.println(T);
        System.out.println(n/p+" "+ n%p);
    }
}