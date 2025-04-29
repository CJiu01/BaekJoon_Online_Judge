import java.io.*;
import java.util.*;

public class Main {

    static Deque<Integer> deque = new LinkedList<>();

    static void push(int num) {
        deque.offer(num);
        return;
    }

    static int pop() {
        Integer num = deque.pollFirst();
        return (num == null ? -1 : num);
    }

    static int size() {
        return deque.size();
    }

    static int empty() {
        return (deque.isEmpty() ? 1 : 0);
    }
    
    static int front() {
        Integer num = deque.peekFirst();
        return (num == null ? -1 : num);
    }

    static int back() {
        Integer num = deque.peekLast();
        return (num == null ? -1 : num);
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        while(N-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            switch (command) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    push(num);
                    break;
                
                case "pop":
                    sb.append(pop()).append("\n");
                    break;

                case "size":
                    sb.append(size()).append("\n");
                    break;

                case "empty":
                    sb.append(empty()).append("\n");
                    break;

                case "front":
                    sb.append(front()).append("\n");
                    break;

                case "back":
                    sb.append(back()).append("\n");
                    break;
            
                default:
                    break;
            }

        }
        System.out.println(sb);
    }
}