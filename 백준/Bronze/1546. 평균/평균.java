import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int[] arr = Arrays.stream(s.split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        int max = Arrays.stream(arr).max().getAsInt();
        double sum = 0;
        for(int i=0; i<arr.length; i++) {
            sum += (double)arr[i]/max*100;
        }
        System.out.println(sum/n);
    }
}