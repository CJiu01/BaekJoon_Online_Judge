import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] graph;
    static int[] oper;
    static int maxValue = Integer.MIN_VALUE;
    static int minValue = Integer.MAX_VALUE;
    static int k=1;
    
    public static void dfs(int count, boolean[] visited, int cal) {

        if(count == N-1) {
            maxValue = Math.max(maxValue, cal);
            minValue = Math.min(minValue, cal);
            return;
        }

        for(int i=0; i<N-1; i++) {
            if(visited[i] == false) {
                visited[i] = true;

                switch (oper[i]) {
                    case 0:
                        dfs(count+1, visited, cal+graph[k++]);
                        break;
                    case 1:
                        dfs(count+1, visited, cal-graph[k++]);
                        break;
                    case 2:
                        dfs(count+1, visited, cal*graph[k++]);
                        break;
                    case 3:
                        dfs(count+1, visited, cal/graph[k++]);
                        break;
                    default:
                        break;
                }
                k--;
                visited[i] = false;
            }
        }
        return;
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N];
        oper = new int[N-1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            graph[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int m=0;
        for(int i=0; i<4; i++) {
            int tmp = Integer.parseInt(st.nextToken());
            for(int l=0; l<tmp; l++) {
                oper[m++] = i;
            }
        }    
        boolean[] visited = new boolean[N-1];
        dfs(0, visited, graph[0]);
        System.out.println(maxValue);
        System.out.println(minValue);

    }
}