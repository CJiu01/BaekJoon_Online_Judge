import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        StringBuilder sb = new StringBuilder();
        
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        String s = "";

        while((s = br.readLine()) != null && !s.isEmpty()) {
            st = new StringTokenizer(s);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            if(a==0 && b==0 && c==0) {
                break;
            }
            int[] tmp = {a,b,c};
            Arrays.sort(tmp);
            if(tmp[2]*tmp[2] == tmp[0]*tmp[0] + tmp[1]*tmp[1]) {
                sb.append("right").append("\n");
            } else {
                sb.append("wrong").append("\n");
            }
        }

        System.out.println(sb);
        br.close();
    }
}