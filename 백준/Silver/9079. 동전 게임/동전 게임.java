import java.io.*;
import java.util.*;

public class Main {
    static int[][] maze = new int[3][3];
    static boolean[] visited;

    static void changeRow(int row) {
        for(int i=0; i<3; i++) {
            maze[row][i] = (maze[row][i]==0) ? 1 : 0;
        }
    }

    static void changeCol(int col) {
        for(int i=0; i<3; i++) {
            maze[i][col] = (maze[i][col]==0) ? 1 : 0;
        }
    }

    static void changeCross(int dir) {
        for(int i=0; i<3; i++) {
            if(dir==0) {
                maze[i][i] = (maze[i][i]==0) ? 1: 0;
            } else {
                maze[i][2-i] = (maze[i][2-i]==0) ? 1: 0;
            }
        }
    }

    static boolean isCorrect() {
        int first = maze[0][0];
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                if(first != maze[i][j]) return false;
            }
        }
        return true;
    }

    static int changeMazeToInt() {
        int now = 0;
        for(int i=0; i<3; i++) {
            for(int j=0; j<3; j++) {
                now = 2*now + maze[i][j];
            }
        }
        return now;
    }

    static void changeIntToMaze(int a) {
        for(int i=2; i>=0; i--) {
            for(int j=2; j>=0; j--) {
                maze[i][j] = a%2;
                a /= 2;
            }
        }
    }

    static int bfs() {

        Queue<List<Integer>> queue = new LinkedList<>();
        int first = changeMazeToInt();
        queue.add(Arrays.asList(first,0));
        visited[first] = true;

        while(!queue.isEmpty()) {
            List<Integer> list = queue.poll();
            int val = list.get(0);
            int cnt = list.get(1); 

            changeIntToMaze(val);
            if(isCorrect()) {
                return cnt;
            }



            // 행 변환
            for(int i=0; i<3; i++) {
                changeRow(i);
                int next = changeMazeToInt();
                if(!visited[next]) {
                    queue.add(Arrays.asList(next, cnt+1));
                    visited[next] = true;
                }
                changeRow(i);
            }

            // 열 변환
            for(int i=0; i<3; i++) {
                changeCol(i);
                int next = changeMazeToInt();
                if(!visited[next]) {
                    queue.add(Arrays.asList(next, cnt+1));
                    visited[next] = true;
                }
                changeCol(i);
            }

            // 대각선 변환
            for(int i=0; i<2; i++) {
                changeCross(i);
                int next = changeMazeToInt();
                if(!visited[next]) {
                    queue.add(Arrays.asList(next, cnt+1));
                    visited[next] = true;
                }
                changeCross(i);
            }

        }
        return -1;

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        while(t-- > 0) {
            for(int i=0; i<3; i++) {
                st = new StringTokenizer(br.readLine());

                for(int j=0; j<3; j++) {
                    String s = st.nextToken();
                    if(s.equals("H")) {
                        maze[i][j] = 0;
                    } else {
                        maze[i][j] = 1;
                    }
                }
            }
            visited = new boolean[512];
            sb.append(bfs()).append("\n");
        }

        System.out.println(sb);
    }
}
