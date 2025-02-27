import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][2];
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr, (a,b) -> {
            if(a[0]==b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });
        for(int[] row: arr) {
            System.out.println(row[0]+" "+row[1]);
        }
    }
}