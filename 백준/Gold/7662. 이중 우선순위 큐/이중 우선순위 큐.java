import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            int k = Integer.parseInt(br.readLine());     
            TreeMap<Integer, Integer> map = new TreeMap<>();

            while(k-- > 0) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String command = st.nextToken();
                int n = Integer.parseInt(st.nextToken());
                switch (command) {
                    case "I":
                        map.put(n, map.getOrDefault(n, 0)+1);
                        break;
                    case "D":
                        if(!map.isEmpty()) {
                            int num;
                            if(n==1) {
                                num = map.lastKey();
                            } else {
                                num = map.firstKey();
                            }
                            map.put(num, map.get(num)-1);
                            if(map.get(num)==0) {
                                map.remove(num);
                            }
                        }
                        break;
                }
            }
            if(map.isEmpty()) {
                sb.append("EMPTY\n");
            } else {
                sb.append(map.lastKey() + " " + map.firstKey()).append("\n");
            }
        }
        System.out.println(sb);
    }
}