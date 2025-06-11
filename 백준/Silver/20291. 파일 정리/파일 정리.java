import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static HashMap<String, Integer> map = new HashMap<>();


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++) {
            String input = br.readLine();
            input = input.split("\\.")[1];
            map.put(input, map.getOrDefault(input, 0)+1);
        }

        int num = map.size();
        String[][] dic = new String[num][2];
        int i=0;
        for(String s: map.keySet()) {
            dic[i][0] = s;
            dic[i][1] = String.valueOf(map.get(s));
            i++;
        }

        Arrays.sort(dic, new Comparator<String[]>() {
            public int compare(String[] a, String[] b) {
                return a[0].compareTo(b[0]); 
            }
        });

        for(String[] s: dic) {
            System.out.println(s[0]+ " "+s[1]);
        }
    }
}