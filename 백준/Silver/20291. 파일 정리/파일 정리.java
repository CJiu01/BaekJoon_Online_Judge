import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        HashMap<String,Integer> map = new HashMap<>();

        while(N-->0) {
            st = new StringTokenizer(br.readLine(), ".");
            st.nextToken();
            String s = st.nextToken();
            map.put(s,map.getOrDefault(s, 0)+1);
        }

        ArrayList<String> list = new ArrayList<>(map.keySet());
        Collections.sort(list);

        for(String s: list) {
            sb.append(s).append(" ").append(map.get(s)).append('\n');
        }
        bw.write(sb.toString());

        br.close();
        bw.flush();
        bw.close();
    }
}