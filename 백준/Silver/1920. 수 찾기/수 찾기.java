import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        int i=0;
        while(st.hasMoreTokens()) {
            arr[i++] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int[] find = new int[m];
        i = 0;
        while(st.hasMoreTokens()) {
            find[i++] = Integer.parseInt(st.nextToken());
            
        }

        Arrays.sort(arr);
        
        for(i=0; i<find.length; i++) {
            int target = find[i];
            int start = 0;
            int end = n-1;
            boolean b = false;
            while(start<=end) {
                int mid = (start+end)/2;
                if(target==arr[mid]) {
                    b = true;
                    break;
                } else if(target>arr[mid]) {
                    start = mid + 1;
                } else {
                    end = mid - 1;
                }
            }
            if(b) System.out.println(1);
            else System.out.println(0);
        }
        
    }
}