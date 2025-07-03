import java.io.*;
import java.util.*;

public class Main {

    static Map<Character, int []> map1 = new HashMap<>();
    static Map<Character, int []> map2 = new HashMap<>();

    static void set() {
        map1.put('q', new int[] {0,0});
        map1.put('w', new int[] {0,1});
        map1.put('e', new int[] {0,2});
        map1.put('r', new int[] {0,3});
        map1.put('t', new int[] {0,4});
        map1.put('a', new int[] {1,0});
        map1.put('s', new int[] {1,1});
        map1.put('d', new int[] {1,2});
        map1.put('f', new int[] {1,3});
        map1.put('g', new int[] {1,4});
        map1.put('z', new int[] {2,0});
        map1.put('x', new int[] {2,1});
        map1.put('c', new int[] {2,2});
        map1.put('v', new int[] {2,3});

        map2.put('y', new int[] {0,5});
        map2.put('u', new int[] {0,6});
        map2.put('i', new int[] {0,7});
        map2.put('o', new int[] {0,8});
        map2.put('p', new int[] {0,9});
        map2.put('h', new int[] {1,5});
        map2.put('j', new int[] {1,6});
        map2.put('k', new int[] {1,7});
        map2.put('l', new int[] {1,8});
        map2.put('b', new int[] {2,4});
        map2.put('n', new int[] {2,5});
        map2.put('m', new int[] {2,6});

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        set();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] left = map1.get(st.nextToken().charAt(0));
        int[] right = map2.get(st.nextToken().charAt(0));
        String target = br.readLine();

        int time = 0;
        for(char c: target.toCharArray()) {
            int[] arr = new int[2];
            if(map1.containsKey(c)) {
                arr = map1.get(c);
                time += Math.abs(arr[0] - left[0]) + Math.abs(arr[1] - left[1]);
                left = arr;
            } else {
                arr = map2.get(c);
                time += Math.abs(arr[0] - right[0]) + Math.abs(arr[1] - right[1]);
                right = arr;
            }
            time+=1;
        }
        System.out.println(time);
    }
}