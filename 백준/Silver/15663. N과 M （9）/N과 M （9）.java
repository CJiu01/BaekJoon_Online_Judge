import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static List<Integer> graph = new ArrayList<>();
    static Set<List<Integer>> set = new HashSet<>();

    public static void dfs(ArrayList<Integer> list, boolean[] visited) {

        if(list.size() == M) {
            set.add(new ArrayList<>(list));
            return;
        }
            
        for(int i=0; i<N; i++) {
            if(!visited[i]) {
                visited[i] = true;
                list.add(graph.get(i));
                dfs(list, visited);
                list.remove(list.size()-1);
                visited[i] = false;
            }
        }
        return;
    }

    public static List<List<Integer>> customSort(List<List<Integer>> sortedList) {
        sortedList.sort((a,b) -> {
            for(int i=0; i<M; i++) {
                if(!a.get(i).equals(b.get(i))) {
                    return a.get(i)-b.get(i);
                }
            }
            return a.size()-b.size();
        });
        return sortedList;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++) {
            graph.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(graph);

        boolean[] visited = new boolean[N];
        dfs(new ArrayList<>(), visited);

        List<List<Integer>> sortedList = new ArrayList<>(set);
        sortedList = customSort(sortedList);
        for(List<Integer> l: sortedList) {
            for(int num: l) {
                System.out.print(num+" ");
            }
            System.out.println();
        }
    }
}