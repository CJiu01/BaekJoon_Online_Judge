import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        Set<String> set = new HashSet<>();
        for(int i=0; i<n; i++) {
            set.add(br.readLine());
        }
        String[] arr = set.toArray(new String[0]);

        Arrays.sort(arr, Comparator.comparing(String::length).thenComparing(String::compareTo));

        for (String s : arr) {
            sb.append(s).append("\n");
        }
        System.out.println(sb);
    }
}
