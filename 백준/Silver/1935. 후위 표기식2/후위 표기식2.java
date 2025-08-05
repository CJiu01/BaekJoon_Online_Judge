import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String input = br.readLine();

        double[] value = new double[n];

        for(int i=0; i<n; i++) {
            value[i] = Double.parseDouble(br.readLine());
        }

        Stack<Double> stack = new Stack<>();
        for(char c: input.toCharArray()) {
            if('A'<= c && c <= 'Z') {
                double d = value[c-'A'];
                stack.push(d);
            } else {
                double b = stack.pop();
                double a = stack.pop();
                double res = 0;

                switch (c) {
                    case '+': res = a+b; break;
                    case '-': res = a-b; break;
                    case '*': res = a*b; break;
                    case '/': res = a/b; break;                
                }
                stack.push(res);
            }
        }
        System.out.printf("%.2f",stack.pop());
    }
}