import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String input = br.readLine();
            if(input.equals("0")) { break; }
            
            int[] arr = Arrays.stream(input.split(""))
                                .mapToInt(Integer::parseInt)
                                .toArray();
            int n = arr.length;
            String res = "yes";

            for(int i=0; i<n/2; i++) {
                if(arr[i]!=arr[n-i-1]) {
                    res = "no";
                    break;
                }
            }

            System.out.println(res);
        }
        
    }
}