import java.io.*;
import java.util.*;

public class Main {
    static int N,M;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();

    static void dfs(ArrayList<Integer> list) {
        if(list.size() == M) {
            for(int num: list) sb.append(num).append(" ");
            sb.append("\n");
            return;
        }

        for(int i=0; i<N; i++) {
            if(list.contains(arr[i])) continue;
            list.add(arr[i]);
            dfs(list);
            list.remove(list.size()-1);
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        dfs(new ArrayList<>());
        System.out.println(sb);
    }
}