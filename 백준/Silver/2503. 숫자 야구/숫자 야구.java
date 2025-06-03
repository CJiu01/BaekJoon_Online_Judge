import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[] check = new boolean[988];

        for(int i=123; i<=987; i++) {
            String num = String.valueOf(i);
            if(num.charAt(0)=='0' || num.charAt(1)=='0' || num.charAt(2)=='0') continue;
            if(num.charAt(0) == num.charAt(1) || num.charAt(0) == num.charAt(2) || num.charAt(1) == num.charAt(2)) continue;
            check[i] = true;
        }

        while(N-->0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char[] input = st.nextToken().toCharArray();
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());

            for(int i=123; i<=987; i++) {
                char[] candi = (i+"").toCharArray();
                int sn = strike;
                int bn = ball;

                if(!check[i]) continue;

                for(int k=0; k<3; k++) {
                    for(int l=0; l<3; l++) {
                        // check strike
                        if((k==l) && input[k]==candi[l]) sn--;

                        // check ball
                        if((k!=l) && input[k]==candi[l]) bn--;
                    }
                }

                if(sn!=0 || bn!=0) check[i] = false;
            }
        }

        int res=0;
        for(int i=123; i<=987; i++) {
            if(check[i]) res+=1;
        }
        System.out.println(res);
    }
}