import java.io.*;
import java.util.*;

public class Main {
    static int[] select;
    static int res;
    static int n,m;
    static int[][] preference;

    public static void dfs(int idx, int depth) {
        if(depth == 3) {
            // 선택된 인덱스들에 대한 최적의 값을 구해야 함.
            int tmp = findOpt();
            res = Math.max(res, tmp);
            return;
        }

        for(int i=idx; i<m; i++) {
            select[depth] = i;
            dfs(i+1, depth+1);
        }
    }

    public static int findOpt() {

        int prefer = 0;
        for(int i=0; i<n; i++) {
            int max = 0;
            for(int j=0; j<3; j++) {
                max = Math.max(max, preference[i][select[j]]);
            }
            prefer += max;
        }
        return prefer;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        select = new int[3];
        preference = new int[n][m];

        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++) {
                preference[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0, 0);
        System.out.println(res);
    }
}
