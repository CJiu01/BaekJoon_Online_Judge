import java.io.*;
import java.util.*;

public class Main {
    static int N,K;
    static String[] word;
    static int[] alph = new int[26];
    static boolean[] visited;
    static int maxCount;

    public static void dfs(int depth, int idx) {
        if(depth == K-5) {
            int count=0;
            for(int l=0; l<N; l++) {
                String s = word[l];
                s = s.substring(4, s.length()-4);
                boolean flag = false;
                for(int j=0;j<s.length();j++) {
                    if(!visited[s.charAt(j)-'a']) {
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
        word = new String[N];
        
        for(int i=0; i<N; i++) {
            String s = br.readLine();
            word[i] = s;
        }
       
        if(K==26) {
            maxCount = N;
        } else {
            visited = new boolean[26];
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