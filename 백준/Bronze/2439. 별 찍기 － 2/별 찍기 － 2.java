import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int a = Integer.parseInt(br.readLine());
        for(int i=1; i<=a; i++) {
            bw.write(" ".repeat(a-i) + "*".repeat(i));
            bw.newLine();
        }

        bw.flush();
        bw.close();
        br.close();
    }
}