import java.io.*;
import java.util.*;

public class Main {

    static StringBuilder sb = new StringBuilder();


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr);


        sb.append(Math.round(Arrays.stream(arr).sum()/(double)n)).append("\n");
        sb.append(arr[n/2]).append("\n");
        maxRepeatsValue(n,arr);
        sb.append(arr[n-1]-arr[0]).append("\n");

        System.out.println(sb);

    }
    
    // 최빈값
    private static void maxRepeatsValue(int n,int[] arr) {
        int max = 0;
        boolean flag = false;
        ArrayList<Integer> maxRepeats = new ArrayList<>();
        int[] repeat = new int[8001]; // 정수의 절댓값은 4,000을 넘지 않는다. 0을 포함하여 8001개의 정수가 입력될 수 있다.


        for(int i=0; i<n; i++) {
            repeat[arr[i]+4000] += 1;

            if(repeat[arr[i]+4000]>max) {
                maxRepeats.clear();
                flag = false;

                maxRepeats.add(arr[i]);
                max = repeat[arr[i]+4000];
            } else if(repeat[arr[i]+4000]==max) {
                maxRepeats.add(arr[i]);
                flag = true;
            }
        }

        if(flag) {
            sb.append(maxRepeats.get(1)).append("\n");
        } else {
            sb.append(maxRepeats.get(0)).append("\n");
        }
    }
}