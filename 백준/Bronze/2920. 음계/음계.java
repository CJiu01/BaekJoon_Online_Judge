import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int t = 0;
        while (st.hasMoreTokens()) {
            t = Integer.parseInt(st.nextToken());
            if(Math.abs(h-t) != 1) {
                bw.write("mixed");
                break;
            }
            h = t;
        }

        if(h==t) {
            if(h==8) {
                bw.write("ascending");
            } else {
                bw.write("descending");
            }
        }

        br.close();
        bw.close();
    }
}
