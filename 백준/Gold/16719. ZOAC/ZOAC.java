import java.io.*;
import java.util.*;

public class Main {
    static List<Character> word = new ArrayList<>();
    static boolean[] visited;

    // 전달받은 리스트에서 가장 앞 문자의 인덱스 반환
    public static void find(int idx) {
        if(idx>=word.size() || checkVisitedAll(idx)) {
            return;
        }

        int front = idx;
        for(int i=idx+1; i<word.size(); i++) {
            if(word.get(front) > word.get(i) && !visited[i]) {
                front = i;
            }
        }
        visited[front] = true;

        for(int i=0; i<word.size(); i++) {
            if(visited[i]) {
                System.out.print(word.get(i));
            }
        }
        System.out.println();

        int i=front+1;
        while(!checkVisitedAll(i)) {
            if(!visited[i]) {
                find(i);

            }
        }
        return;
    }

    static boolean checkVisitedAll(int idx) {
        for(int i=idx; i<word.size(); i++) {
            if(!visited[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        for(char c: s.toCharArray()) {
            word.add(c);
        }
        visited = new boolean[word.size()];
        while (!checkVisitedAll(0)) {
            find(0);    
        }
    }
}