import java.io.*;
import java.util.*;

public class Main {
    static Deque<Integer> deque;
    static boolean isReversed;

    static List<Integer> parseToList(String str) {
        str = str.substring(1, str.length() - 1);
        List<Integer> result = new ArrayList<>();

        if (!str.isEmpty()) {
            for (String s : str.split(",")) {
                result.add(Integer.parseInt(s));
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String command = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String array = br.readLine();

            deque = new ArrayDeque<>(parseToList(array));
            isReversed = false;
            boolean error = false;

            for (char c : command.toCharArray()) {
                if (c == 'R') {
                    isReversed = !isReversed;
                } else if (c == 'D') {
                    if (deque.isEmpty()) {
                        error = true;
                        break;
                    }
                    if (isReversed) {
                        deque.pollLast();
                    } else {
                        deque.pollFirst();
                    }
                }
            }

            if (error) {
                System.out.println("error");
            } else {
                StringBuilder sb = new StringBuilder();
                sb.append("[");
                while (!deque.isEmpty()) {
                    sb.append(isReversed ? deque.pollLast() : deque.pollFirst());
                    if (!deque.isEmpty()) sb.append(",");
                }
                sb.append("]");
                System.out.println(sb);
            }
        }
    }
}