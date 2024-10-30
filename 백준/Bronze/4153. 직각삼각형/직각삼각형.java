import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
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
                bw.write("right");
                bw.newLine();
            } else {
                bw.write("wrong");
                bw.newLine();
            }
        }

        bw.close();
        br.close();
    }
}