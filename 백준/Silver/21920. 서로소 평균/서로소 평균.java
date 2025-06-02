import java.io.*;
import java.util.*;

public class Main {
    static int X;

    static boolean isDisjoint(int b) {
        int a = X;
        while(b!=0) {
            int tmp = a;
            a = b;
            b = tmp%b;
        }
        if(a==1) return true;
        return false;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[N];
        for(int i=0; i<N; i++) arr[i] = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(br.readLine());

        ArrayList<Integer> disjointArr = new ArrayList<>();

        for(int num: arr) {
            if(isDisjoint(num)) disjointArr.add(num);
        }
        Integer[] array = disjointArr.toArray(new Integer[0]);
        double avg = Arrays.stream(array)
        .mapToInt(Integer::intValue)
        .average()
        .orElse(0);

        System.out.println(avg);
    }
}