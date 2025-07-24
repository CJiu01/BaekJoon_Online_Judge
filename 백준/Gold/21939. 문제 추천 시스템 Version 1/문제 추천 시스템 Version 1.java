import java.io.*;
import java.util.*;

public class Main {

    // 난이도,[문제]
    static TreeMap<Integer, TreeSet<Integer>> map = new TreeMap<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;

        while(n-- > 0) {
            st = new StringTokenizer(br.readLine());
            int value = Integer.parseInt(st.nextToken());
            int key = Integer.parseInt(st.nextToken());
            add(value, key);
        }

        int m = Integer.parseInt(br.readLine());
        while(m-- > 0) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            switch (command) {
                case "recommend":
                    int num = recommend(Integer.parseInt(st.nextToken()));
                    sb.append(num).append("\n");
                    break;
                case "add":
                    add(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
                    break;
                case "solved":
                    solved(Integer.parseInt(st.nextToken()));
                    break;
            }
        }

        System.out.println(sb);
    }

    static public int recommend(int type) {
        int res;
        if(type == 1) {
            res = map.get(map.lastKey()).last();
        } else {
            res = map.get(map.firstKey()).first();
        }
        return res;
    }

    static public void add(int number, int level) {
        map.computeIfAbsent(level, k->new TreeSet<>()).add(number);
    }

    static public void solved(int number) {
        for (Map.Entry<Integer, TreeSet<Integer>> entry : map.entrySet()) {
            TreeSet<Integer> set = entry.getValue();
            if (set.remove(number)) {
                if (set.isEmpty()) {
                    map.remove(entry.getKey());
                }
                break;
            }
        }
    }
}