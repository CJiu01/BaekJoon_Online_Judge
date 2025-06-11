import java.io.*;
import java.util.*;

public class Main {
    static int N,K;
    static String[] words;
    static boolean[] visited;
    static int maxCount = Integer.MIN_VALUE;

    public static void dfs(int depth, int idx) {

        if(depth == K-5) {
            int count=0;
            for(int l=0; l<N; l++) {
                boolean flag = false;
                for(int j=0;j<words[l].length();j++) {
                    if(!visited[words[l].charAt(j)-'a']) {
                        flag = true;
                        break;
                    }
                }
                if(!flag) count += 1;
            }
            maxCount = Math.max(count, maxCount);
            return;
        }

        for(int i=idx; i<26; i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(depth+1, i+1);
                visited[i] = false;
            }
        }
        return;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        words = new String[N];
        visited = new boolean[26];
        
        for(int i=0; i<N; i++) {
            String s = br.readLine();
            s = s.replace("anta", "");
            s = s.replace("tica", "");
            words[i] = s;
        }
    
        if(K<5) {
            maxCount = 0;
        } else if(K==26) {
            maxCount = N;
        } else {
            visited['a'-'a'] = true;
            visited['c'-'a'] = true;
            visited['i'-'a'] = true;
            visited['n'-'a'] = true;
            visited['t'-'a'] = true;
            dfs(0, 0);
        }
        System.out.println(maxCount);
    }
}
