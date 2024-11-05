import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder output = new StringBuilder();

        StringTokenizer st = new StringTokenizer(input.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Queue<Integer> queue = new LinkedList<>();
        for(int i=1; i<=n; i++) {
            queue.offer(i);
        }
        int turn = 1;
        output.append("<");

        while(!queue.isEmpty()) {
            if(turn%k != 0) {
                queue.offer(queue.poll());
            } else {
                output.append(queue.poll());
                if(!queue.isEmpty()) {
                    output.append(", ");
                }
            }
            turn += 1;
        }
        output.append(">");
        System.out.println(output);

    }
}