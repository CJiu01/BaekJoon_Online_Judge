import java.io.*;
import java.util.*;

public class Main {
    static int combination(int n, int r) {
        if (n == r || r == 0) return 1;
        return combination(n - 1, r - 1) + combination(n - 1, r);
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for(int i=0; i<t; i++) {
            int n = Integer.parseInt(br.readLine());
            HashMap<String, List<String>> hash = new HashMap<>();

            for(int j=0; j<n; j++) {
                st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String type = st.nextToken();

                hash.computeIfAbsent(type, k->new ArrayList<>()).add(name);
            }

            int[] tmp = new int[hash.size()];
            int tmpCnt = 0;

            for (Map.Entry<String, List<String>> entry : hash.entrySet()) {
                int cnt = entry.getValue().size();
                int res = 0;

                for (int k = 0; k <= 1; k++) {
                    res += combination(cnt, k);
                }

                tmp[tmpCnt++] = res;
}
            int product = Arrays.stream(tmp).reduce(1, (a,b) -> a*b);
            System.out.println(product-1);
        }
    }
}