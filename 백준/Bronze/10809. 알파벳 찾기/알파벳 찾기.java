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

        int[] arr = new int[26];
        Arrays.fill(arr, -1);
        String s = br.readLine();

        int tmp = 0;
        for(int i=0; i<s.length(); i++) {
            tmp = (int)s.charAt(i) - 97;
            if(arr[tmp] == -1) {
                arr[tmp] = i;
            }
        }

        for (int i = 0; i < arr.length; i++) {
            bw.write(arr[i]+ " ");
        }

        br.close();
        bw.close();
    }
}
