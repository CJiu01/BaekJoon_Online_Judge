import java.io.*;
import java.util.*;

public class Main {
    static char[] duck;


    public static int countDuck(int front, int rear) {

        int count = 1;
        for(int i=front+1; i<rear; i++) {
            if(duck[i] == 'q') {
                count+=1;
            }
        }
        return count;
    }

    public static boolean isCorrect() {

        String quack = "uack";
        List<Character> list = new ArrayList<>();

        for (char c : duck) {
            list.add(c);
        }

        while(list.indexOf('q') != -1) {
            int start = list.indexOf('q');
            list.remove(start);

            int check = 0;
            for(int j=start; j<list.size(); j++) {
                if(list.get(j) == quack.charAt(check)) {
                    check++;
                    list.remove(j--);
                }
                if(check == 4) break;
            }
            if(check<4) return false;
        }

        return list.isEmpty() ? true : false;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        duck = s.toCharArray();

        int res = 0;
        int idx = 0;
        int last = 0;

        if(!isCorrect()) {
            System.out.println(-1);
            return;
        }
        while(idx < duck.length) {

            if(duck[idx] == 'q') {

                // q와 가장 인접한 k를 찾기 위한 반복문
                for(int i=idx+1; i<duck.length; i++) {
                    if(duck[i]=='k' && i>last) {
                        int tmp = countDuck(idx, i);
                        if (tmp == -1) {
                            System.out.println(-1);
                            return;
                        }
                        res = Math.max(res, tmp);
                        last = i;
                        break;
                    }
                }

            }
            idx++;
        }
        System.out.println(res>0 ? res : -1);
    }
}