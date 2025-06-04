import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] wantedWord;
    static int[] chosedWord;
    static Book[] books;
    static int res = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String T = br.readLine();
        N = Integer.parseInt(br.readLine());

        wantedWord = new int['Z'-'A'+1];
        chosedWord = new int['Z'-'A'+1];
        books = new Book[N];

        for(char c: T.toCharArray()) {
            wantedWord[c-'A']++;
        }

        StringTokenizer st;
        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int price = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            books[i] = new Book(price, name);
        }
        dfs(0,0);

        if(res==Integer.MAX_VALUE) System.out.println(-1);
        else System.out.println(res);
    }

    public static void dfs(int depth, int sum) {

        if(depth == N) {
            if(check()) {
                res = Math.min(res, sum);
            }
            return;
        }

        // 선택
        for(int i=0; i<books[depth].name.length(); i++) {
            char c = books[depth].name.charAt(i);
            chosedWord[c-'A']++;
        }
        dfs(depth+1, sum+books[depth].price);

        // 선택x
        for(int i=0; i<books[depth].name.length(); i++) {
            char c = books[depth].name.charAt(i);
            chosedWord[c-'A']--;
        }
        dfs(depth+1, sum);
    }

    public static boolean check() {
        for(int i=0; i<'Z'-'A'+1; i++) {
            if(wantedWord[i] > chosedWord[i]) return false;
        }
        return true;
    }

    static public class Book {
        int price;
        String name;

        Book(int price, String name) {
            this.price = price;
            this.name = name;
        }
    }
}