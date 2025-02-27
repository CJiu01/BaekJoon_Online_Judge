import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][4];

        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][2] = i+1;
            arr[i][3] = 0;
        }
        Arrays.sort(arr, (a,b) -> Integer.compare(b[0],a[0]));

        int i=0;
        while(i<n) {
            int k = 0;
            int j = 0;
            while(arr[j][0] > arr[i][0]) {
                if(arr[j][1] > arr[i][1]) {
                    k += 1;
                }
                j+=1;
            }     
            arr[i][3] = k+1;
            i += 1;
        }
        Arrays.sort(arr, (a,b) -> Integer.compare(a[2], b[2]));
        for(int[] row: arr) {
            System.out.print(row[3]+ " ");
        }
    }
}