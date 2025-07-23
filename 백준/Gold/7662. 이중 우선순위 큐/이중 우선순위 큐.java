import java.io.*;
import java.util.*;

public class Main {

    static Map<Integer, Integer> map;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            int k = Integer.parseInt(br.readLine());

            Queue<Integer> ascendingPq = new PriorityQueue<>();
            Queue<Integer> decendingPq = new PriorityQueue<>(Collections.reverseOrder());   
            map = new HashMap<>();

            while(k-- > 0) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String command = st.nextToken();
                int n = Integer.parseInt(st.nextToken());
                switch (command) {
                    case "I":
                        ascendingPq.offer(n);
                        decendingPq.offer(n);
                        map.put(n, map.getOrDefault(n, 0)+1);
                        break;
                    case "D":
                        if(!map.isEmpty()) {
                            if(n==1) {
                                delete(decendingPq);
                            } else {
                                delete(ascendingPq);
                            }
                        }

                        break;
                }
            }
            if(map.isEmpty()) {
                sb.append("EMPTY").append("\n");
            } else {
                int res = delete(decendingPq);
                sb.append(res + " ");
                if(!map.isEmpty()) res = delete(ascendingPq);
                sb.append(res).append("\n");
            }
        }

        System.out.println(sb);
    }

    static int delete(Queue<Integer> q) {
        int n;
        while(true) {
            n = q.poll();

            int value = map.getOrDefault(n, 0);
            if(value==0) continue;
            else if(value==1) map.remove(n);
            else map.put(n, value-1);
            break;
        }
        return n;
    }
}