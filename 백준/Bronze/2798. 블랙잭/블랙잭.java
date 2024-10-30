import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String s = br.readLine();
        int[] arr = Arrays.stream(s.split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();

        Arrays.sort(arr);

        int res = 0;
        int tmp = 0;

        for(int i=n-1; i>1; i--) {
            for(int j=i-1; j>0; j--) {
                for(int k=j-1; k>-1; k--) {


                    tmp = arr[i] + arr[j] + arr[k];

                    if(res<tmp && tmp<=m) {
                        res = tmp;
                    }
                }
            }
        }
        System.out.println(res);
    }
}