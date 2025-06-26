import java.io.*;
import java.util.*;

public class Main {

    static int N,M;
    static int[] graph;
    static StringBuilder sb = new StringBuilder();

    static void dfs(List<Integer> list, int idx) {

        // 종료조건
        if(list.size() == M) {
            for(Integer i: list) {
                sb.append(i).append(" ");
            }
            sb.append("\n");
            return;
        }

        for(int i=idx; i<N; i++) {
            list.add(graph[i]);
            dfs(list, i+1);
            list.remove(list.size()-1);
        }
        return;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        graph = new int[N];

        for(int i=0; i<N; i++) {
            graph[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(graph);
        dfs(new ArrayList<>(), 0);
        System.out.println(sb);
    }
}