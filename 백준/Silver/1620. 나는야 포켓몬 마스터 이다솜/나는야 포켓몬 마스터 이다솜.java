import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> mapToInt = new HashMap<>();
        Map<Integer, String> mapToString = new HashMap<>();

        for(int i=1; i<=n; i++) {
            String s = br.readLine();
            mapToInt.put(s, i);
            mapToString.put(i, s);
        }
        while(m-- > 0) {
            String s = br.readLine();
            if('0'<=s.charAt(0) && s.charAt(0)<='9') sb.append(mapToString.get(Integer.parseInt(s))).append("\n");
            else sb.append(mapToInt.get(s)).append("\n");
        }

        System.out.println(sb);

    }
}