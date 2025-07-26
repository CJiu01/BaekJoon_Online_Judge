import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Queue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()) {
                queue.offer(Integer.parseInt(st.nextToken()));
            }

        }
        while(n-- > 1){
            queue.poll();
        }
        System.out.println(queue.poll());
    }
}