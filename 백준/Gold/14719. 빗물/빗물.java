import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());
        int[] arr = new int[W];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<W; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int res = 0;
        for(int i=1; i<W-1; i++) {
            int left=0;
            int right=0;

            for(int l=0; l<i; l++) {
                left = Math.max(left, arr[l]);
            }

            for(int r=i+1; r<W; r++) {
                right = Math.max(right, arr[r]);
            }

            if(arr[i]<=left && arr[i]<=right) {
                res += (Math.min(left, right)-arr[i]);
            }
        }
        System.out.println(res);
    }
}
