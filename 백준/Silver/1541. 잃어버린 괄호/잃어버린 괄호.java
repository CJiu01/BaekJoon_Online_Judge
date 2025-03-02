import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(),"+-",true);

        List<Integer> number = new ArrayList<>();
        List<Character> oper = new ArrayList<>();

        while(st.hasMoreTokens()) {
            String token = st.nextToken();

            if(token.equals("+") || token.equals("-")) 
                oper.add(token.charAt(0));
            else number.add(Integer.parseInt(token));
        }

        int i = 0;        
        while(i<oper.size()) {
            if(oper.get(i).equals('-')) {
                i++;
                int tmpSum = number.remove(i);
                while(i<oper.size() && oper.get(i) == '+') {
                    oper.remove(i);
                    tmpSum += number.remove(i);
                }
                oper.remove(i-1);
                int k = number.remove(i-1);
                number.add(i-1,k-tmpSum);
                i=0;
            } else {
                i++;
            }
        }
        int res = number.remove(0);
        while(!oper.isEmpty()) {
            Character op = oper.remove(0);
            if(op=='+') res += number.remove(0);
            else res -= number.remove(0);
        }
        System.out.println(res);
    }
}