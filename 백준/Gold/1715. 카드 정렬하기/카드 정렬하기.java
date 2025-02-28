import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i=0; i<n; i++) {
            pq.add(Integer.parseInt(br.readLine()));
        }

        int ans = 0;
        while(pq.size()>1) {
            int m1 = pq.remove();

            int m2 = pq.remove();

            pq.add(m1+m2);
            ans += m1+m2;
        }
        System.out.println(ans);    
    }
}