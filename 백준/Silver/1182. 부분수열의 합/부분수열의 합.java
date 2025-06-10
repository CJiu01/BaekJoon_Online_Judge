import java.io.*;
import java.util.*;

public class Main {
    static int N,S;
    static List<Integer> graph = new ArrayList<>();
    static int count;

    public static void dfs(List<Integer> list, int idx) {

        if(idx>N) {
            return;
        }
        if(!list.isEmpty()) {
            int sum = 0;
            for(int num: list) {    
                sum += num;
            }
            if(sum == S) count += 1;
        }
        for(int i=idx; i<graph.size(); i++) {
            list.add(graph.get(i));
            dfs(list, i+1);
            list.remove(list.size()-1);
        }
        return;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()) {
            graph.add(Integer.parseInt(st.nextToken()));
        }

        dfs(new ArrayList<>(), 0);
        System.out.println(count);
    }
}