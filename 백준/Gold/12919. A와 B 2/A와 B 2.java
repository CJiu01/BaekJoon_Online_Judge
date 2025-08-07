import java.io.*;
import java.util.*;

public class Main {
    static String S,T;
    static int lengthS;
    static int res = 0;

    public static void simulate(String t, int lastIdx) {
        if(lastIdx == lengthS) {
            if(S.equals(t)) {
                res = 1;
            }
            return;
        }
        if(t.charAt(lastIdx)=='A') {
            String tmp = t.substring(0,lastIdx);
            simulate(tmp, lastIdx-1);
        }

        String tmp = new StringBuilder(t).reverse().toString();
        if(tmp.charAt(lastIdx)=='B') {
            tmp = tmp.substring(0, lastIdx);
            simulate(tmp, lastIdx-1);
        }
        return;

    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        S = br.readLine();
        T = br.readLine();
    }

    public static void main(String[] args) throws IOException  {

        init();
        lengthS = S.length()-1;
        simulate(T, T.length()-1);
        System.out.println(res);
        
    }
}