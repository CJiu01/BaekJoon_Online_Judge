import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());

        while(T-- > 0) {

            HashMap<String, Integer> hm = new HashMap<>();

            int N = Integer.parseInt(br.readLine());

            while(N-- > 0) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                st.nextToken();
                String type = st.nextToken();
                if(hm.containsKey(type)) {
                    hm.put(type, hm.get(type)+1);
                } else {
                    hm.put(type, 1);
                }
            }

            int result = 1;
            for(int val:hm.values()) {
                result *= (val+1);
            }
            sb.append(result-1).append("\n");
        } 
        System.out.println(sb);
    }
}