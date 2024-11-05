import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        String input = "";
        while(!(input = br.readLine()).equals(".")) {
            
            sb.append(checkBalanced(input)).append("\n");
            
        }
        System.out.println(sb);
    }

    public static String checkBalanced(String input) {

        Stack<String> stack = new Stack<>();

        for(int i=0; i<input.length(); i++) {
            String target = String.valueOf(input.charAt(i));

            if(target.equals("(") || target.equals("[")) {
                stack.push(target);
            } else if(target.equals(")")) {
                if(stack.isEmpty()) {
                    return "no";
                }
                String preTarget = stack.pop();
                if(!preTarget.equals("(")) {
                    return "no";
                }
            } else if(target.equals("]")) {
                if(stack.isEmpty()) {
                    return "no";
                }
                String preTarget = stack.pop();
                if(!preTarget.equals("[")) {
                    return "no";
                }
            }
        }
        if(!stack.isEmpty()) {
            return "no";
        }
        return "yes";
    }
}