import java.io.*;

public class Main {
    public static boolean endNumber(int n) {
        int cnt = 0;
        String s = String.valueOf(n);
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i)=='6') {
                cnt += 1;
            } else {
                cnt = 0;
            }

            if(cnt==3) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int i = 0;
        int number = 666;
        while(true) {
            if(endNumber(number)) {
                i+=1;
            }
            if(n==i) break;
            number += 1;

        }
        System.out.println(number);
    }
}