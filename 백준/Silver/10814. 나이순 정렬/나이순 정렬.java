import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String[][] member = new String[n][3];
        for(int i=0;i<n;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            member[i][0] = st.nextToken();
            member[i][1] = st.nextToken();
            member[i][2] = String.valueOf(i);
        }

        Arrays.sort(member, (a,b) -> {
            if(Integer.parseInt(a[0]) == Integer.parseInt(b[0])) {
                return Integer.compare(Integer.parseInt(a[2]), Integer.parseInt(b[2]));
            }
            return Integer.compare(Integer.parseInt(a[0]), Integer.parseInt(b[0]));
        });

        for(String[] row: member) {
            System.out.println(row[0]+" " +row[1]);
        }
    }
}
