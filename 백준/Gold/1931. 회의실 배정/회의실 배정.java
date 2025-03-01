import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];
        StringTokenizer st;
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr, (a,b) -> {
            if(a[0]==b[0]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        int i=1;
        int cnt=0;
        int min=arr[0][1];
        while(i<n) {
            if(arr[i][0]>=min) {
                cnt+=1;
                min=arr[i][1];
            } else {
                if(min>arr[i][1]) {
                    min = arr[i][1];
                }
            }
            i++;
        }
        System.out.println(cnt+1);
    }
}