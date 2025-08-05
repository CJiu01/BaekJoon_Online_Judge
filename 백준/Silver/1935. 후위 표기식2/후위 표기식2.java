import java.io.*;
import java.util.*;

public class Main {
    public static int[] value;

    static double plus(double a, double b) {
        return a+b;
    }
    static double minus(double a, double b) {
        return b-a;
    }
    static double mul(double a, double b) {
        return a*b;
    }
    static double divide(double a, double b) {
        return b/a;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String input = br.readLine();

        value = new int[n];
        Stack<Double> stack = new Stack<>();
        int i=0;


        while(i<n) {
            value[i++] = Integer.parseInt(br.readLine());
        }

        i=0;

        int[] convertedInput = new int[input.length()];

        while(i<input.length()) {
            char c = input.charAt(i);

            if(c-'1' >= 0) {
                convertedInput[i] = value[c-'A'];
            } else {
                switch(c) {
                    case '+':
                        convertedInput[i] = -1;
                        break;
            
                    case '-':
                        convertedInput[i] = -2;
                        break;

                    case '*':
                        convertedInput[i] = -3;
                        break;

                    case '/':
                        convertedInput[i] = -4;
                        break;
                }
            }
            i++;
        }

        i=0;
        while(i<convertedInput.length) {
            int tar = convertedInput[i++];

            if(tar >= 0) {
                stack.push(Double.valueOf(tar));
                continue;
            }
         

            double res = 0;
            switch (tar) {
                case -1:
                    res = plus(stack.pop(), stack.pop());
                    stack.push(res);
                    break;
            
                case -2:
                    res = minus(stack.pop(), stack.pop());
                    stack.push(res);         
                    break;

                case -3:
                    res = mul(stack.pop(), stack.pop());
                    stack.push(res);   
                    break;

                case -4:
                    res = divide(stack.pop(), stack.pop());
                    stack.push(res);    
                    break;
            }
            
        }
        System.out.printf("%.2f\n",stack.pop());

    }
}