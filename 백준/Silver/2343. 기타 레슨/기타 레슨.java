import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];

        int end=0;
        int start=0;
        for(int i=0;i<n;i++) {
            int num = sc.nextInt();
            if(num>start) start = num;
            arr[i] = num;
            end += num;
        }

        int mid =0;
        while(start<=end) {
            mid = (start+end)/2;
            int sum=0;
            int cnt=0;
            for(int i=0;i<n;i++) {
                if(sum+arr[i]>mid) {
                    sum=0;
                    cnt+=1;
                }
                sum += arr[i];
            }
            if(sum>0) cnt +=1;

            if(cnt>m) start = mid+1;
            else end = mid-1;
        }

        System.out.println(start);
        }
    }