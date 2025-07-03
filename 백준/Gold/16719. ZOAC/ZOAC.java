import java.io.*;
import java.util.*;

public class Main {
    static List<Character> word = new ArrayList<>();
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    static void find(int left, int right) {

        if(left>right) return;

        int idx = left;
        for(int i=left; i<=right; i++) {
            if(word.get(idx) > word.get(i) && !visited[i]) {
                idx = i;
            }
        }
        visited[idx] = true;

        for(int i=0; i<word.size(); i++) {
            if(visited[i]) sb.append(word.get(i));
        }
        sb.append("\n");

        find(idx+1, right);
        find(left, idx-1);

        return;
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        for(char c: s.toCharArray()) {
            word.add(c);
        }
        visited = new boolean[word.size()];
        find(0,word.size()-1);

        System.out.println(sb);
    }
}