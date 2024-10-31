import java.io.*;
import java.util.*;

public class Main {

    static PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    static Queue<Doc> q = new LinkedList<>();
    static StringBuilder sb = new StringBuilder();
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static int t, n, m;


    public static void main(String[] args) throws IOException {

        t = Integer.parseInt(br.readLine());

        
        for(int i=0; i<t; i++) {

            init();
            input();
            solve();
        }
        System.out.println(sb);
    }

    public static void solve() throws IOException {
        // solve
        int cnt = 1;
        while(true) {

            // 맨 앞의 원소가 우선순위가 가장 높은 경우
            if(pq.peek() == q.peek().priority) {
                // 맨 앞의 원소가 m인 경우
                if(q.peek().idx == m) {
                    sb.append(cnt).append("\n");
                    break;
                } else {
                    pq.poll();
                    q.poll();
                    cnt += 1;
                }
            } else {
                q.add(q.poll());
            }
        }
    }

    public static void init() {
        q.clear();
        pq.clear();
    }

    public static void input() throws IOException {

        StringTokenizer st;

        // input
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for(int j=0; j<n; j++) {
            int num = Integer.parseInt(st.nextToken());
            q.add(new Doc(j, num));
            pq.add(num);
        }
    }

    static class Doc {
        int idx;
        int priority;

        public Doc(int idx, int priority) {
            this.idx = idx;
            this.priority = priority;
        }
    }
}