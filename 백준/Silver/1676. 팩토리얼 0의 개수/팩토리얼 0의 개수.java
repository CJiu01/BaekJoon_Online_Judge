import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int res = 0;

        for(int i=0; i<=n; i++) {
            int cnt = 0;
            int tmp = i;
            while(tmp%5==0 && tmp>0) {
                tmp /= 5;
                cnt += 1;
            }
            res += cnt;
        }
        System.out.println(res);
    }
}