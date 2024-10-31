import java.io.*;
import java.util.*;

public class Main {
    static int idx = -1;
    static int[] stack = new int[10001];

    public static void main(String[] args) throws IOException {
        init();
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            String method = st.nextToken();

            switch(method) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    idx += 1;
                    stack[idx] = num;
                    break;
                case "pop":
                    if(idx == -1) {
                        sb.append("-1").append("\n");
                    } else {
                        sb.append(stack[idx]).append("\n");
                        idx -= 1;
                    }
                    break;      
                case "size":
                    sb.append(idx+1).append("\n");
                    break;
                case "empty":
                    int empty = (idx == -1) ? 1 : 0;
                    sb.append(empty).append("\n");
                    break;
                case "top":
                    int top = (idx == -1) ? -1 : stack[idx];
                    sb.append(top).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}