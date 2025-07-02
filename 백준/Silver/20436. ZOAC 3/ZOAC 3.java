import java.io.*;
import java.util.*;

public class Main {
    static List<List<String>> keyboardLeft = new ArrayList<>();
    static List<List<String>> keyboardRight = new ArrayList<>();

    static int[] left = new int[2];
    static int[] right = new int[2];

        
    static void set(String leftFirst, String rightFirst) {
        keyboardLeft.add(Arrays.asList("q","w","e","r","t"));
        keyboardLeft.add(Arrays.asList("a","s","d","f","g"));
        keyboardLeft.add(Arrays.asList("z","x","c","v"));

        keyboardRight.add(Arrays.asList(" ","y","u","i","o","p"));
        keyboardRight.add(Arrays.asList(" ","h","j","k","l"));
        keyboardRight.add(Arrays.asList("b","n","m"));

        for(int i=0; i<3; i++) {
            if(keyboardLeft.get(i).contains(leftFirst)) {
                left[0] = i;
                left[1] = keyboardLeft.get(i).indexOf(leftFirst);
                break;
            }

        }

        for(int i=0; i<3; i++) {
            if(keyboardRight.get(i).contains(rightFirst)) {
                right[0] = i;
                right[1] = keyboardRight.get(i).indexOf(rightFirst);
                break;
            }
        }
    }

    static int findDir(String c) {

        int row = -1;
        int col = -1;

        for(int i=0; i<3; i++) {
            if(keyboardLeft.get(i).contains(c)) {
                row = i;
                col = keyboardLeft.get(i).indexOf(c);
                break;
            }
        }
        
        int dist = 0;
        if(row == -1) {
            for(int i=0; i<3; i++) {
                if(keyboardRight.get(i).contains(c)) {
                    row = i;
                    col = keyboardRight.get(i).indexOf(c);
                    break;
                }
            }
            dist = moveRight(row, col);
        } else {
            dist = moveLeft(row, col);
        }

        return dist;

    }

    static int moveLeft(int row, int col) {
        int dist = Math.abs(left[0]-row) + Math.abs(left[1]-col);
        left[0] = row;
        left[1] = col;
        return dist;
    }

    static int moveRight(int row, int col) {
        int dist = Math.abs(right[0]-row) + Math.abs(right[1]-col);
        right[0] = row;
        right[1] = col;
        return dist;
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String leftFirst = st.nextToken();
        String rightFirst = st.nextToken();
        String target = br.readLine();

        set(leftFirst, rightFirst);
        int time = 0;
        for(char c: target.toCharArray()) {
            time += (findDir(String.valueOf(c))+1);
        }
        System.out.println(time);
    }
}
