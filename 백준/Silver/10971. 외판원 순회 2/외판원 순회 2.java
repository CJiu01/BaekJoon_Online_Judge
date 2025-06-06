import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] graph;
    static int res = Integer.MAX_VALUE;
    static int start;

    public static void dfs(int fore, int pre, int count, boolean[] visited, int price) {

        if(count == N) {
            if(graph[pre][start] != 0) {
                res = Math.min(res, price+graph[pre][start]);
            }
            return;
        }

        for(int i=0; i<N; i++) {
            if(visited[i] == false) {
                if(graph[pre][i]!=0){
                    visited[i] = true;
                    dfs(pre, i, count+1, visited, price+graph[pre][i]);
                    visited[i] = false;
                }
            }
        }
        return;
    }
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new int[N][N];

        StringTokenizer st;
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i=0; i<N; i++) {
            start = i;
            boolean[] visited = new boolean[N];
            visited[i] = true;
            dfs(i, i, 1, visited, 0);
        }

        System.out.println(res);
    }
}