import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        
        for(int i=0; i<n; i++) {
            String s = br.readLine();

            int res = 0;
            int point = 1;
            for(int j=0; j<s.length(); j++) {

                if(String.valueOf(s.charAt(j)).equals("O")) {
                    res += point++;
                } else {
                    point = 1;
                }
            }

            bw.write(String.valueOf(res));
            bw.newLine();
        }

        br.close();
        bw.close();
        
    }
}