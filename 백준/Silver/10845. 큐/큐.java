import java.io.*;
import java.util.*;

class CustomQueue {
    LinkedList<Integer> queue = new LinkedList<>();

    void push(int num) {
        queue.offer(num);
    }

    int pop() {
        if(queue.isEmpty()) {
            return -1;
        }
        return queue.poll();
    }

    int size() {
        return queue.size();
    }

    int empty() {
        return queue.isEmpty() ? 1 : 0;
    }

    int front() {
        if(queue.isEmpty()) {
            return -1;
        }
        return queue.peek();
    }

    int back() {
        if(queue.isEmpty()) {
            return -1;
        }
        return queue.peekLast();
    }
}

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        CustomQueue queue = new CustomQueue();

        for(int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());

            String command = st.nextToken();
            switch (command) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    queue.push(num);        
                    break;
                case "pop":
                    sb.append(queue.pop()+"\n");
                    break;
                case "size":
                    sb.append(queue.size()+"\n");
                    break;
                case "empty":
                    sb.append(queue.empty()+"\n");
                    break;
                case "front":
                    sb.append(queue.front()+"\n");
                    break;
                case "back":
                    sb.append(queue.back()+"\n");
                    break;
                default:
                    break;
            }
        }
        System.out.println(sb);
    }
}