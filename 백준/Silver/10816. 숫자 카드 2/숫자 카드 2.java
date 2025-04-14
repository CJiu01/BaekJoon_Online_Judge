import java.io.*;
import java.util.*;

public class Main {

    public static int bisectLeft(int[] list, int target) {
        int low=0, high=list.length;
        while(low<high) {
            int mid = (low+high)/2;
            if(list[mid] < target) {
                low = mid+1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    public static int bisectRight(int[] list, int target) {
        int low=0, high=list.length;
        while(low<high) {
            int mid=(low+high)/2;
            if(list[mid]<=target) {
                low = mid+1;
            } else {
                high = mid;
            }
        }
        return low;
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] card = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for(int i=0;i<n;i++) {
            int num = Integer.parseInt(st.nextToken());
            card[i] = num;
        }
        Arrays.sort(card);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        while(st.hasMoreTokens()) {
            int num = Integer.parseInt(st.nextToken());
            bw.write(Integer.toString(bisectRight(card, num)-bisectLeft(card, num)));
            bw.write(" ");
        }
        br.close();
        bw.close();
    }
}