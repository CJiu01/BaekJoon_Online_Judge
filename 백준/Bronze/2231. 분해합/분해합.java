import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int n = Integer.parseInt(input);
        int res = 0;

        int tmp = 0;
        for(int i=0; i<n; i++) {
            String target = String.valueOf(i);
            int[] arr = Arrays.stream(target.split(""))
                            .mapToInt(Integer::parseInt)
                            .toArray();

            tmp = i + Arrays.stream(arr).sum();

            if(tmp==n) {
                res = i;
                break;
            }
        }

        System.out.println(res);
    }
}