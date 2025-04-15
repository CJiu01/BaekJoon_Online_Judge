import java.io.*;
import java.util.*;

class CustomQueue<T> {
    LinkedList<T> queue = new LinkedList<>();

    void push(T num) {
        queue.offer(num);
    }

    T pop() {
        return queue.poll();
    }

    int size() {
        return queue.size();
    }

    int empty() {
        return queue.isEmpty() ? 1 : 0;
    }

    T front() {
        return queue.peek();
    }

    T back() {
        return queue.peekLast();
    }
}

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        CustomQueue<Integer> queue = new CustomQueue();

        for(int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());

            String command = st.nextToken();
            Integer res = null;
            switch (command) {
                case "push":
                    int num = Integer.parseInt(st.nextToken());
                    queue.push(num);        
                    break;
                case "pop":
                    res = queue.pop();
                    break;
                case "size":
                    res = queue.size();
                    break;
                case "empty":
                    res = queue.empty();
                    break;
                case "front":
                    res = queue.front();
                    break;
                case "back":
                    res = queue.back();
                    break;
            }
            if(!command.equals("push")) {
                sb.append((res==null) ? -1 : res).append("\n");
            }
        }
        System.out.println(sb);
        br.close();

    }
}