import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Integer.parseInt(br.readLine());
        String input = br.readLine();
        int[] arr = Arrays.stream(input.split(" "))
                            .mapToInt(Integer::parseInt)
                            .toArray();

        int cnt = 0;
        for(int i=0; i<arr.length; i++) {
            int target = arr[i];
            for(int j=2; j<=target; j++) {
                if(target==j) {
                    cnt++;
                } else if(target%j == 0) {
                    break;
                }
            }

        }
        System.out.println(cnt);
    }
}