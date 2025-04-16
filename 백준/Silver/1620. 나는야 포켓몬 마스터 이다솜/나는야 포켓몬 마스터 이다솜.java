import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        HashMap<String, Integer> map = new HashMap<>();
        String[] arr = new String[n];
        for(int i=0;i<n;i++) {
            String s = br.readLine();
            map.put(s, i+1);
            arr[i] = s;
        }

        StringBuilder sb = new StringBuilder();
        for(int i=0;i<m;i++) {
            String s = br.readLine();
            if(s.charAt(0)-'0'>9) {
                sb.append(map.get(s)).append("\n");
            } else {
                sb.append(arr[Integer.parseInt(s)-1]).append("\n");
            }
            
        }
        System.out.println(sb);
    }
}