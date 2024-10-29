import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int maxIdx = 0;
        int arr[] = new int[9];

        for(int i=0; i<9; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            
            if(arr[i]>arr[maxIdx]) {
                maxIdx = i;
            }
        }

        System.out.println(arr[maxIdx]);
        System.out.println(maxIdx+1);
    }
}