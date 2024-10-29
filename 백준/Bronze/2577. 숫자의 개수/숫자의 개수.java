import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());

        String res = String.valueOf(a*b*c);

        for(int i=0; i<10; i++) {
            int cnt = 0;
            for(int idx=0; idx<res.length(); idx++) {
                if(Integer.parseInt(res.charAt(idx)+"")==i) {
                    cnt++;
                }
            }
            bw.write(cnt+"\n");
        }

        br.close();
        bw.close();
    }
}
