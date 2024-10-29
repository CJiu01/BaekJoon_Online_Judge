import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;



public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        int[] res = new int[42];
        Arrays.fill(res, -1);

        int cnt = 0;
        for(int i=0; i<10; i++) {
            int input = Integer.parseInt(br.readLine());
            int tmp = input%42;
            if(res[tmp]==-1) {
                cnt++;
                res[tmp]=0;
            }
        }
        bw.write(String.valueOf(cnt));
        br.close();
        bw.close();
    }
}
