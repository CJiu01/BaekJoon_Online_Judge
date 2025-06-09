import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] graph;
    static int[] oper;
    static int maxValue = Integer.MIN_VALUE;
    static int minValue = Integer.MAX_VALUE;
    static int k=1;
    
    public static void dfs(int count, int cal) {

        if(count == N) {
            maxValue = Math.max(maxValue, cal);
            minValue = Math.min(minValue, cal);
            return;
        }

        for(int i=0; i<4; i++) {
            if(oper[i] > 0) {
                oper[i]--;

                int next = 0;
                switch (i) {
                    case 0: next = cal+graph[count]; break;
                    case 1: next = cal-graph[count]; break;
                    case 2: next = cal*graph[count]; break;
                    case 3: 
                        if(cal<0) {
                            next = -(-cal/graph[count]);
                        } else {
                            next = cal/graph[count]; 
                        }
                        break;
                }
                dfs(count+1, next);

                // 연산자 개수 복원
                oper[i]++;
            }
        }
        return;
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N];
        oper = new int[4];

        // 숫자 입력
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            graph[i] = Integer.parseInt(st.nextToken());
        }

        // 연산자 개수 입력
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<4; i++) {
            oper[i] = Integer.parseInt(st.nextToken());
        }    

        dfs(1, graph[0]);
        System.out.println(maxValue);
        System.out.println(minValue);

    }
}